# Contributing

Corrections, facilitation experience, and focused new scenarios are welcome.
Open a “Propose a scenario” issue before writing a new drill.

Every file in `drills/` must contain:

- one unique `Drill ID`;
- learning objectives;
- setup;
- roles;
- a timeline with at least three injects;
- decision points;
- debrief questions;
- expected follow-up; and
- an advanced variant.

Keep company and user details fictional. A drill should test decisions and
coordination, not depend on a particular provider or require participant
coding.

Before opening a pull request, run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

If a drill changes, update its matching section in the printable HTML pack.
Follow the [Code of Conduct](CODE_OF_CONDUCT.md). Contributions are accepted
under Apache-2.0.
