# Drill 07: Yesterday's policy

- **Drill ID:** `stale-data`
- **Duration:** 45 minutes
- **Audience:** Product, data, engineering, content operations, support

## Learning objectives

- Detect stale or incorrectly authoritative source data.
- Practise source withdrawal and answer correction.
- Assign ownership across content and AI operations.

## Setup

Atlas is a fictional employee policy assistant. It retrieves approved documents
from a content system and includes source links in every answer. A nightly job
updates the search index. Content owners can replace a document while keeping
the same public URL.

A new travel policy took effect this morning after an urgent legal change.

## Roles

Assign an incident lead, content owner, product owner, engineering or data lead,
support or communications lead, and observer.

## Timeline

### Inject 1 — 8 minutes

An employee reports that Atlas quoted yesterday's travel allowance. The linked
page now shows the correct policy, making the answer appear unsupported.

### Inject 2 — 15 minutes

The indexing job succeeded before the replacement was published. The index
stores extracted text but not the document version or effective date.

### Inject 3 — 22 minutes

About 600 employees asked travel questions today. Answers are not retained, but
query topics and source IDs are available. The content team cannot trigger an
individual document refresh.

### Inject 4 — 29 minutes

Engineering can rebuild the full index in three hours. During the rebuild, the
assistant may continue serving the old index or be disabled. A travel deadline
is in four hours.

## Decision points

- Who declares a source unsuitable for generated answers?
- Can the affected topic be blocked while other topics remain available?
- How do you identify and inform potentially affected users?
- What proves the replacement content is effective in retrieval and answers?
- Which freshness guarantees should the product communicate?

## Debrief

- Did a working source link create false confidence?
- Could content owners withdraw or urgently refresh material?
- Were effective dates and versions treated as product data?
- Did the response consider employees who already acted?
- Was recovery tested at the answer level, not only index completion?

## Expected follow-up

- Store source version, effective date, and indexing time with retrieved chunks.
- Add targeted refresh and withdrawal controls for content owners.
- Alert on source-to-index freshness and failed high-priority updates.
- Define correction communication for users exposed to superseded guidance.

## Advanced variant

The old policy was intentionally preserved for employees in one country, but
country metadata was lost during indexing. Ask the team to recover without
publishing one global answer or exposing employee location unnecessarily.
