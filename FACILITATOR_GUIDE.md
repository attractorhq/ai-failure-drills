# Facilitator guide

You do not need to be the system's technical expert. Your job is to protect the
learning environment, keep time, reveal information gradually, and turn the
conversation into owned follow-up.

## Before the session

1. Choose one drill from the [matrix](README.md#choose-a-drill).
2. Invite five to eight people who represent the affected workflow, not only
   the implementation team.
3. Replace fictional names and thresholds only when local detail will improve
   the decisions. Do not use real credentials or personal data.
4. Share the [participant brief](materials/participant-brief.md), but keep the
   inject timeline private.
5. Print or copy the [role cards](materials/role-cards.md), the
   [decision log](materials/decision-log.md), and the
   [debrief scorecard](materials/debrief-scorecard.md).
6. Decide where actions will be recorded after the session.

## Suggested 60-minute format

| Time | Activity |
| --- | --- |
| 0–5 min | Explain the purpose, boundaries, and fictional starting state |
| 5–10 min | Assign roles and let participants read the initial situation |
| 10–35 min | Reveal one inject at a time and record decisions |
| 35–50 min | Run the debrief without replaying every conversation |
| 50–60 min | Agree actions, owners, and review dates |

For a 45-minute session, use the first three injects and reserve ten minutes for
the debrief.

## Ground rules

- The scenario is a learning exercise, not a performance review.
- Participants act with the information available at that moment.
- Saying “we would check the dashboard” is incomplete: name the signal,
  threshold, owner, and resulting decision.
- The facilitator may answer an unspecified factual question with
  “that information is not currently available.”
- Capture disagreements. They often reveal missing policy or ownership.
- Do not let architectural debate consume the incident response.

## Revealing injects

Read the initial situation and first inject exactly enough to create a decision.
Ask the incident lead what happens next, then let other roles respond. Reveal
the next inject when the team has:

- made or explicitly deferred a decision;
- named an owner;
- stated what evidence it needs; and
- considered user impact.

Do not rescue the team by supplying a preferred answer. Use the decision points
in the drill to probe gaps.

## Debrief

Move from the fictional incident to the real system:

1. What did we notice quickly, and what stayed invisible?
2. Which decision lacked an owner, threshold, or source of truth?
3. Could we stop or degrade the feature without causing a second incident?
4. What would affected users need from us?
5. Which assumption should become a test, alert, control, or runbook step?

Score the current capability, not the quality of the conversation. Finish with
no more than five concrete actions.

## After the session

Send the decision log and actions within one working day. Put actions in the
team's normal delivery system, assign owners and review dates, and schedule a
short follow-up. Repeat the drill after important system or ownership changes.
