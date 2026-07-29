# Drill 05: The agent that would not stop

- **Drill ID:** `runaway-agent`
- **Duration:** 60 minutes
- **Audience:** Product, engineering, operations, finance, security

## Learning objectives

- Contain an agent loop across model, tool, and business boundaries.
- Balance financial, operational, and user impact.
- Define enforceable action and cost budgets.

## Setup

Relay is a fictional sales-operations agent. On request, it researches a
prospect, enriches the account record, drafts follow-up tasks, and schedules the
next review. The agent may call three internal tools. A run normally takes
under two minutes and costs less than one euro.

The team recently allowed the agent to retry failed tool calls and reflect on
incomplete tasks. A per-user daily budget exists only as a dashboard.

## Roles

Assign an incident lead, engineering lead, product owner, security lead,
finance or commercial owner, and observer.

## Timeline

### Inject 1 — 10 minutes

Finance reports that model spend is six times the normal daily amount by 09:30.
Application dashboards show more active runs but no errors.

### Inject 2 — 17 minutes

One run has executed for 74 minutes. A tool returns “record already exists,”
which the agent interprets as incomplete work and retries with slightly
different account names.

### Inject 3 — 25 minutes

The agent created 430 duplicate follow-up tasks across 62 account records.
Killing the worker stops current runs, but queued jobs restart automatically.
The tool has no bulk undo operation.

### Inject 4 — 33 minutes

A sales director asks the team to keep the agent available for unaffected
users. Security notices that several near-duplicate account names belong to
organisations outside the original user's territory.

## Decision points

- How do you stop model calls, tool actions, and automatic restarts?
- Is this one incident or separate cost, integrity, and access incidents?
- What can be safely reversed, and who approves the repair?
- Can any subset of users or actions remain enabled?
- Which budgets and permissions must be enforced before recovery?

## Debrief

- Was there a kill switch outside the agent's own reasoning loop?
- Did the team monitor successful but unwanted actions?
- Were permissions limited by user, territory, tool, and action?
- Could spend alerts trigger containment rather than only notification?
- Did the recovery plan protect evidence and prevent duplicate repair?

## Expected follow-up

- Enforce limits on iterations, elapsed time, tokens, cost, and tool calls.
- Require idempotency keys and reversible or reviewable consequential actions.
- Separate the scheduler, worker, model, and tool kill switches.
- Alert on action cardinality, unusual target scope, and cost velocity.

## Advanced variant

The loop stays within its financial budget by using a cheaper model, but it
creates thousands of low-value internal tasks. Ask the team to define harm and
containment without relying on cost as the primary signal.
