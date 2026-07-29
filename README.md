# AI Failure Drills

Facilitator-ready tabletop exercises for rehearsing how AI products fail in
production.

The hardest time to decide who can stop an AI feature is during an incident.
These drills help product, engineering, design, security, operations, legal, and
communications people practise decisions before users are affected.

Each drill runs in 45–60 minutes, works offline, and requires no API keys or
participant coding. Choose a scenario, print or share the materials, assign
roles, and reveal the injects one at a time.

## Quick start

```bash
git clone https://github.com/attractorhq/ai-failure-drills.git
cd ai-failure-drills
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Then read the [facilitator guide](FACILITATOR_GUIDE.md), select a drill, and
open [the printable facilitator pack](print/facilitator-pack.html) in a
browser. For printing, select A4, enable background graphics, and disable
browser headers and footers. Everything runs with the Python standard library
and static files.

## Choose a drill

| Drill | Primary risk | Useful participants | Duration |
| --- | --- | --- | --- |
| [Confidently wrong after release](drills/01-quality-regression.md) | Quality regression | Product, engineering, support | 60 min |
| [Instructions in the knowledge base](drills/02-prompt-injection.md) | Prompt injection | Engineering, security, product | 60 min |
| [The other customer's contract](drills/03-cross-tenant-exposure.md) | Data exposure | Security, engineering, privacy | 60 min |
| [Slow provider, fast retries](drills/04-provider-outage.md) | Availability | Engineering, operations, support | 45 min |
| [The agent that would not stop](drills/05-runaway-agent.md) | Actions and cost | Product, engineering, finance | 60 min |
| [Approved by automation](drills/06-unsafe-action.md) | Human control | Product, design, risk, operations | 60 min |
| [Yesterday's policy](drills/07-stale-data.md) | Data integrity | Product, data, operations | 45 min |
| [Green dashboard, unhappy users](drills/08-monitoring-blind-spot.md) | Detection and ownership | Operations, support, leadership | 60 min |

If this is your first exercise, start with
[Confidently wrong after release](drills/01-quality-regression.md). It exposes
product, evaluation, communication, and rollback decisions without requiring
specialist security knowledge.

## Included materials

- [Participant brief](materials/participant-brief.md)
- [Role cards](materials/role-cards.md)
- [Decision and observation log](materials/decision-log.md)
- [Debrief scorecard](materials/debrief-scorecard.md)
- [Facilitator guide](FACILITATOR_GUIDE.md)
- [A4 printable pack](print/facilitator-pack.html)

## What a good drill produces

A drill is not a test of individual performance. It should leave the team with:

- a clearer incident owner and escalation path;
- explicit stop, degrade, and recovery criteria;
- monitoring or evaluation gaps to fix;
- named actions with owners and review dates; and
- at least one new test, runbook step, or product safeguard.

## Contributing

Run the [validator](scripts/validate.py) and tests before opening a pull request.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the scenario contract and review
expectations.

Attractor maintains these drills for the community. They are licensed under
[Apache-2.0](LICENSE).
