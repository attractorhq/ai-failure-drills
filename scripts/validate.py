#!/usr/bin/env python3
"""Validate drill structure, local links, and the printable pack."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


EXPECTED_DRILL_COUNT = 8
REQUIRED_HEADINGS = (
    "## Learning objectives",
    "## Setup",
    "## Roles",
    "## Timeline",
    "## Decision points",
    "## Debrief",
    "## Expected follow-up",
    "## Advanced variant",
)
DRILL_ID_PATTERN = re.compile(
    r"^\s*-\s+\*\*Drill ID:\*\*\s+`([a-z0-9]+(?:-[a-z0-9]+)*)`\s*$",
    re.MULTILINE,
)
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")
PRINT_ID_PATTERN = re.compile(r'data-drill-id="([a-z0-9]+(?:-[a-z0-9]+)*)"')


@dataclass(frozen=True)
class ValidationError:
    path: Path
    message: str

    def display(self, root: Path) -> str:
        try:
            shown_path = self.path.relative_to(root)
        except ValueError:
            shown_path = self.path
        return f"ERROR {shown_path}: {self.message}"


def read_text(path: Path, errors: list[ValidationError]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(ValidationError(path, f"cannot read UTF-8 text: {exc}"))
        return ""


def validate_drills(root: Path, errors: list[ValidationError]) -> set[str]:
    drills_dir = root / "drills"
    drill_files = sorted(drills_dir.glob("*.md")) if drills_dir.is_dir() else []

    if len(drill_files) != EXPECTED_DRILL_COUNT:
        errors.append(
            ValidationError(
                drills_dir,
                f"expected {EXPECTED_DRILL_COUNT} Markdown drills, found {len(drill_files)}",
            )
        )

    seen: dict[str, Path] = {}
    for path in drill_files:
        text = read_text(path, errors)
        if not text.startswith("# Drill "):
            errors.append(ValidationError(path, "first line must start with '# Drill '"))

        id_match = DRILL_ID_PATTERN.search(text)
        if id_match is None:
            errors.append(
                ValidationError(
                    path,
                    "missing a kebab-case '- **Drill ID:** `example-id`' field",
                )
            )
        else:
            drill_id = id_match.group(1)
            if drill_id in seen:
                first_path = seen[drill_id].relative_to(root)
                errors.append(
                    ValidationError(
                        path,
                        f"duplicate Drill ID '{drill_id}' (first used in {first_path})",
                    )
                )
            else:
                seen[drill_id] = path

        for heading in REQUIRED_HEADINGS:
            if not re.search(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE):
                errors.append(ValidationError(path, f"missing required heading '{heading}'"))

        inject_count = len(re.findall(r"^### Inject \d+\b", text, re.MULTILINE))
        if inject_count < 3:
            errors.append(
                ValidationError(path, f"expected at least 3 injects, found {inject_count}")
            )

    return set(seen)


def validate_readme_index(
    root: Path, drill_ids: set[str], errors: list[ValidationError]
) -> None:
    readme_path = root / "README.md"
    readme = read_text(readme_path, errors)
    for drill_path in sorted((root / "drills").glob("*.md")):
        relative = drill_path.relative_to(root).as_posix()
        if f"]({relative})" not in readme:
            errors.append(
                ValidationError(readme_path, f"drill index does not link to '{relative}'")
            )

    if drill_ids and "FACILITATOR_GUIDE.md" not in readme:
        errors.append(
            ValidationError(readme_path, "missing link to FACILITATOR_GUIDE.md")
        )


def validate_local_links(root: Path, errors: list[ValidationError]) -> None:
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = read_text(path, errors)
        for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
            target = raw_target.strip("<>")
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc or target.startswith("#"):
                continue

            decoded_path = unquote(parsed.path)
            if not decoded_path:
                continue
            resolved = (
                root / decoded_path.lstrip("/")
                if decoded_path.startswith("/")
                else path.parent / decoded_path
            ).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(
                    ValidationError(path, f"local link escapes repository: '{target}'")
                )
                continue
            if not resolved.exists():
                errors.append(
                    ValidationError(path, f"local link target does not exist: '{target}'")
                )


def validate_print_pack(
    root: Path, drill_ids: set[str], errors: list[ValidationError]
) -> None:
    print_path = root / "print" / "facilitator-pack.html"
    html = read_text(print_path, errors)
    if not html:
        return

    print_ids = PRINT_ID_PATTERN.findall(html)
    print_id_set = set(print_ids)

    for drill_id in sorted(drill_ids - print_id_set):
        errors.append(
            ValidationError(
                print_path, f"printable pack is missing Drill ID '{drill_id}'"
            )
        )
    for drill_id in sorted(print_id_set - drill_ids):
        errors.append(
            ValidationError(
                print_path, f"printable pack has unknown Drill ID '{drill_id}'"
            )
        )
    for drill_id in sorted(print_id_set):
        if print_ids.count(drill_id) != 1:
            errors.append(
                ValidationError(
                    print_path,
                    f"Drill ID '{drill_id}' must appear exactly once in the pack",
                )
            )

    required_markers = ('lang="en"', "<main", "@page", "@media print")
    for marker in required_markers:
        if marker not in html:
            errors.append(
                ValidationError(print_path, f"missing printable HTML marker '{marker}'")
            )


def validate(root: Path) -> list[ValidationError]:
    root = root.resolve()
    errors: list[ValidationError] = []
    drill_ids = validate_drills(root, errors)
    validate_readme_index(root, drill_ids, errors)
    validate_local_links(root, errors)
    validate_print_pack(root, drill_ids, errors)
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate AI Failure Drills repository content."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of scripts/)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(error.display(args.root), file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"Validated {EXPECTED_DRILL_COUNT} drills, local links, and printable pack."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
