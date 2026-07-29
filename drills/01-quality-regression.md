# Drill 01: Confidently wrong after release

- **Drill ID:** `quality-regression`
- **Duration:** 60 minutes
- **Audience:** Product, engineering, customer support, operations

## Learning objectives

- Connect user harm with a model or prompt change when service health is green.
- Practise containment when there is no perfect rollback.
- Define evidence for recovery and user communication.

## Setup

Northstar is a fictional support assistant used by account managers. It
summarises policy documents and drafts answers; users send the answer after
review. Yesterday the team released a new model and shorter system prompt.
Offline evaluation improved from 82% to 86%, latency fell by 18%, and no alert
has fired.

The release owner is away. The previous model remains available, but the
retrieval index was also rebuilt and cannot be rolled back automatically.

## Roles

Assign an incident lead, product owner, engineering and operations lead,
support lead, and observer. Add design or communications when six or more
people participate.

## Timeline

### Inject 1 — 10 minutes

Three account managers report that the assistant confidently quoted a
non-existent cancellation rule. One answer has already been sent to a customer.
Standard uptime, latency, and error-rate dashboards are green.

### Inject 2 — 17 minutes

Engineering reproduces one report only when a long customer history is present.
The trace records the final answer and token count but not retrieved passages or
prompt version.

### Inject 3 — 25 minutes

Support finds 14 similar conversations from the last 18 hours. Disabling the
assistant would also remove search used by 200 account managers during a busy
renewal week.

### Inject 4 — 33 minutes

The previous model gives the correct answer for the first case but fails two
cases that the new model handles correctly. A sales leader asks whether the
feature is safe to re-enable before a customer demonstration in two hours.

## Decision points

- What establishes incident severity and ownership?
- Do you continue, degrade, disable, or partially roll back the feature?
- How do you find affected outputs when provenance is incomplete?
- Who needs a message now, and what can be said with confidence?
- Which evaluation result and production evidence are required for recovery?

## Debrief

- Which metric created false reassurance?
- Did the team distinguish generation, retrieval, and workflow failures?
- Could users verify or correct the wrong answer before sending it?
- What slice was absent from pre-release evaluation?
- Was the recovery criterion more precise than “looks good again”?

## Expected follow-up

- Add the reviewed failures and long-history slice to the evaluation set.
- Record prompt, model, retrieval, and source provenance in privacy-safe traces.
- Define a degraded mode that preserves search without generated answers.
- Assign release rollback ownership and a user-notification decision path.

## Advanced variant

The incorrect rule appears only in Finnish-language conversations for one
contract tier. Ask the team to revise its impact search, communication, and
release threshold without treating all users as equally affected.
