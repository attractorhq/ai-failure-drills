# Drill 03: The other customer's contract

- **Drill ID:** `cross-tenant-exposure`
- **Duration:** 60 minutes
- **Audience:** Security, privacy, engineering, product, support

## Learning objectives

- Contain potential cross-tenant exposure without waiting for perfect facts.
- Distinguish access-control evidence from model-output evidence.
- Practise notification and recovery decisions.

## Setup

Harbour is a fictional contract assistant used by business customers. It
summarises clauses from documents uploaded to a tenant-specific workspace.
Retrieval filters by tenant identifier, and generated answers are retained for
30 days so users can reopen prior work.

The service has 80 tenants. Enterprise contracts require prompt notice of
confirmed unauthorised disclosure.

## Roles

Assign an incident lead, security and privacy lead, engineering lead, product
owner, customer support lead, and observer. Add legal or communications when
available.

## Timeline

### Inject 1 — 10 minutes

A customer opens a support ticket with a screenshot showing another company's
name and a specific payment term in an answer. They ask whether anyone else can
see their contracts.

### Inject 2 — 17 minutes

Engineering finds a cache key that includes document ID but not tenant ID. The
cache was enabled three days ago. Document identifiers are normally unique, but
a migration imported legacy documents with overlapping IDs.

### Inject 3 — 25 minutes

Request logs can identify cache hits but do not record which source text was
returned. The screenshot may show public boilerplate, yet the payment term
matches a real customer contract.

### Inject 4 — 33 minutes

Disabling the cache removes the suspected path but doubles latency and causes
timeouts for large contracts. Two enterprise customers ask for written
assurance that their data was not exposed.

## Decision points

- When do you declare and escalate a potential data breach?
- What is the safest immediate containment?
- How do you define the possibly affected population with incomplete logs?
- What do you tell the reporting customer and other tenants, and when?
- Which technical and evidence criteria permit restoration?

## Debrief

- Did the team centre affected customers rather than debate terminology?
- Could tenant isolation be tested below the model layer?
- Were retention and logs sufficient for investigation but appropriately
  minimised?
- Who had authority to disable or degrade the feature?
- Did recovery include independent verification?

## Expected follow-up

- Include tenant identity in every cache and retrieval boundary.
- Add deterministic cross-tenant isolation tests and migration collision cases.
- Document evidence-preservation, notification, and customer-support paths.
- Create a degraded mode with bounded input size while the cache is disabled.

## Advanced variant

An internal analyst used an administrator support tool that bypasses tenant
filters shortly before the report. Ask the team to investigate both plausible
paths without prematurely blaming the analyst or losing audit evidence.
