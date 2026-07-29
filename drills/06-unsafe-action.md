# Drill 06: Approved by automation

- **Drill ID:** `unsafe-action`
- **Duration:** 60 minutes
- **Audience:** Product, design, risk, engineering, operations

## Learning objectives

- Test whether human approval is informed and meaningful.
- Practise stopping unsafe automated actions.
- Improve override, reversal, and user communication.

## Setup

Compass is a fictional procurement assistant. It reads supplier requests,
recommends a risk category, and prepares an approval for an employee. Requests
below a threshold need one click to accept; higher-risk requests go to a
specialist team.

To reduce delay, the interface highlights the recommended action and collapses
source details. Employees accept 96% of recommendations.

## Roles

Assign an incident lead, product owner, designer, engineering lead, risk or
compliance owner, operations representative, and observer.

## Timeline

### Inject 1 — 10 minutes

An employee notices that the assistant approved a supplier whose application
contains a prohibited ownership structure. The employee clicked approve after
seeing a “low risk” recommendation.

### Inject 2 — 17 minutes

The model extracted the ownership detail correctly, but a prompt example taught
it to treat the phrase as an exception. The interface did not show the
extracted detail unless expanded.

### Inject 3 — 25 minutes

Thirty-seven similar suppliers were approved in the last month. Approval
records contain the employee click and final recommendation, but not the
evidence shown at the time.

### Inject 4 — 33 minutes

Disabling automated recommendations would create a ten-day review backlog.
Operations proposes keeping recommendations visible with a warning while the
team investigates.

## Decision points

- Who can pause approvals, recommendations, or only the affected category?
- Was the employee's click meaningful review?
- How will previous approvals be identified and reassessed?
- What evidence must the interface show before an approval?
- Which workflow and evaluation changes are required for recovery?

## Debrief

- Did the organisation transfer responsibility to users without giving them
  enough information?
- Could an action be reversed after approval?
- Was automation bias measured in product research?
- Did the team distinguish correct extraction from unsafe policy reasoning?
- Were backlog and business pressure allowed to redefine acceptable risk?

## Expected follow-up

- Display decision-relevant evidence and uncertainty before the approval action.
- Require specialist review for enforceable high-consequence rules.
- Preserve the policy, evidence, recommendation, and interface version.
- Add reversal, retrospective review, and automation-bias usability tests.

## Advanced variant

The employee noticed the problem but believed overriding the recommendation
would reduce their performance score. Ask the team to address organisational
incentives, escalation safety, and interface design together.
