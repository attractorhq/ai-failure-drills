"""Tests for the dependency-free content validator."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate import REQUIRED_HEADINGS, validate


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        (self.root / "drills").mkdir()
        (self.root / "print").mkdir()
        self.write_valid_fixture()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def drill_text(self, number: int, drill_id: str) -> str:
        sections = "\n\n".join(f"{heading}\n\nContent." for heading in REQUIRED_HEADINGS)
        return (
            f"# Drill {number:02d}: Scenario {number}\n\n"
            f"- **Drill ID:** `{drill_id}`\n\n"
            f"{sections}\n\n"
            "### Inject 1 — now\n\nFirst.\n\n"
            "### Inject 2 — later\n\nSecond.\n\n"
            "### Inject 3 — last\n\nThird.\n"
        )

    def write_valid_fixture(self) -> None:
        links: list[str] = []
        ids: list[str] = []
        for number in range(1, 9):
            drill_id = f"scenario-{number}"
            path = self.root / "drills" / f"{number:02d}-scenario.md"
            path.write_text(self.drill_text(number, drill_id), encoding="utf-8")
            links.append(f"- [Scenario {number}](drills/{path.name})")
            ids.append(drill_id)

        (self.root / "FACILITATOR_GUIDE.md").write_text(
            "# Facilitator guide\n", encoding="utf-8"
        )
        (self.root / "README.md").write_text(
            "# Test drills\n\n"
            "[Guide](FACILITATOR_GUIDE.md)\n\n"
            + "\n".join(links)
            + "\n",
            encoding="utf-8",
        )
        sections = "".join(
            f'<section data-drill-id="{drill_id}"></section>' for drill_id in ids
        )
        (self.root / "print" / "facilitator-pack.html").write_text(
            '<html lang="en"><style>@page{} @media print{}</style>'
            f"<main>{sections}</main></html>",
            encoding="utf-8",
        )

    def messages(self) -> list[str]:
        return [error.message for error in validate(self.root)]

    def test_valid_repository_passes(self) -> None:
        self.assertEqual([], validate(self.root))

    def test_missing_heading_is_actionable(self) -> None:
        path = self.root / "drills" / "01-scenario.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("## Debrief", "## Review"),
            encoding="utf-8",
        )

        self.assertIn("missing required heading '## Debrief'", self.messages())

    def test_duplicate_id_is_rejected(self) -> None:
        path = self.root / "drills" / "02-scenario.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("scenario-2", "scenario-1"),
            encoding="utf-8",
        )

        self.assertTrue(
            any("duplicate Drill ID 'scenario-1'" in message for message in self.messages())
        )

    def test_missing_local_link_target_is_rejected(self) -> None:
        readme = self.root / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8") + "\n[Missing](materials/missing.md)\n",
            encoding="utf-8",
        )

        self.assertIn(
            "local link target does not exist: 'materials/missing.md'",
            self.messages(),
        )

    def test_print_pack_must_match_drill_ids(self) -> None:
        path = self.root / "print" / "facilitator-pack.html"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                'data-drill-id="scenario-8"', 'data-drill-id="unknown-drill"'
            ),
            encoding="utf-8",
        )

        messages = self.messages()
        self.assertIn("printable pack is missing Drill ID 'scenario-8'", messages)
        self.assertIn("printable pack has unknown Drill ID 'unknown-drill'", messages)


if __name__ == "__main__":
    unittest.main()
