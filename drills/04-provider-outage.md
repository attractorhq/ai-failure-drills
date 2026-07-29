# Drill 04: Slow provider, fast retries

- **Drill ID:** `provider-outage`
- **Duration:** 45 minutes
- **Audience:** Engineering, operations, product, support

## Learning objectives

- Recognise retry amplification and dependency failure.
- Choose a degraded product mode based on user need.
- Define service recovery beyond provider availability.

## Setup

Lighthouse is a fictional assistant that drafts maintenance summaries from
technician notes. Requests use one external model provider with a 20-second
timeout and two automatic retries. Users can also view the original notes.

The feature has a 99% monthly availability objective. It has no contractual
multi-provider requirement.

## Roles

Assign an incident lead, engineering and operations lead, product owner,
support lead, and observer.

## Timeline

### Inject 1 — 8 minutes

Model latency rises from 4 seconds to 18 seconds. Application error rate remains
below the alert threshold, but support receives reports of summaries appearing
twice.

### Inject 2 — 15 minutes

The provider status page reports degraded performance. Internal traffic to the
provider is now 2.6 times normal because timed-out requests continue while
retries start.

### Inject 3 — 22 minutes

Workers are exhausted and the queue delays original note uploads, which do not
require the model. A second provider is available in a prototype branch but has
not passed privacy review or evaluation.

### Inject 4 — 29 minutes

The provider reports recovery. Your queue contains 18,000 old generation jobs,
some for users who already retried manually.

## Decision points

- When do you stop retries or open the circuit?
- Which non-AI workflow must be protected first?
- Do you disable summaries, queue them, or attempt an unapproved provider?
- What should users see while the dependency is degraded?
- How will stale and duplicate jobs be handled during recovery?

## Debrief

- Did retries have a total time and attempt budget?
- Could the AI feature fail without blocking the base product?
- Was provider recovery confused with product recovery?
- Who could enable degraded mode without a code deployment?
- Were cost and duplicate side effects visible?

## Expected follow-up

- Add bounded retries, backoff, jitter, and circuit-breaking behaviour.
- Isolate generation capacity from the core note workflow.
- Document a user-centred degraded mode and queue expiration policy.
- Alert on dependency latency, retry amplification, queue age, and total cost.

## Advanced variant

The outage begins during a safety-critical maintenance window. Ask the team to
identify which users should receive priority, while ensuring that the generated
summary is not mistaken for the original technician record.
