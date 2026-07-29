# Drill 08: Green dashboard, unhappy users

- **Drill ID:** `monitoring-blind-spot`
- **Duration:** 60 minutes
- **Audience:** Operations, support, product, engineering, leadership

## Learning objectives

- Connect technical signals with user-visible AI quality.
- Establish incident ownership when no component is down.
- Practise communication during uncertain, distributed impact.

## Setup

Signal is a fictional assistant that converts incoming service requests into a
summary, category, and routing recommendation. The service meets its latency
and availability objectives. A weekly sampled review measures summary quality.

Product owns the interface, a platform team owns generation, and operations
owns routing rules. No team owns the combined outcome.

## Roles

Assign an incident lead, product owner, platform engineering lead, operations
lead, customer support lead, leadership or communications representative, and
observer.

## Timeline

### Inject 1 — 10 minutes

Support reports a rise in customers asking why urgent requests have not been
answered. All services are green and ticket volume is normal.

### Inject 2 — 17 minutes

Operations finds that requests written in short, informal language are often
classified as “general.” Routing rules correctly process the supplied category.
No quality alert exists by language or writing style.

### Inject 3 — 25 minutes

The pattern began gradually six days ago after a prompt update. Each team's
dashboard remains within its own target. The weekly human review happened to
sample no affected requests.

### Inject 4 — 33 minutes

There may be 1,200 delayed requests. Reprocessing everything could flood the
urgent queue with duplicates. Leadership asks for an impact number and a public
status update within 30 minutes.

## Decision points

- Who becomes incident lead when every component meets its target?
- How do you find affected users without creating further routing harm?
- Which containment protects new and already delayed requests?
- What can be communicated before the impact count is reliable?
- Which end-to-end objective and alert should own this failure?

## Debrief

- Did team boundaries hide the user outcome?
- Which user cohort was absent from evaluation and sampling?
- Could support reports create a structured operational signal?
- Did the team assign one owner for recovery verification?
- Was the status message honest about uncertainty and next update time?

## Expected follow-up

- Add end-to-end routing quality objectives and cohort-level evaluation.
- Connect support signals, overrides, and delayed outcomes to monitoring.
- Version prompts in traces and add guarded rollback.
- Define safe reprocessing, deduplication, and customer-update procedures.

## Advanced variant

The affected writing style correlates with users of an accessibility feature.
Ask the team to investigate and communicate impact without making unsupported
claims about protected characteristics.
