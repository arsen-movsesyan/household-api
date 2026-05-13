# PR #643 Feedback Process Concerns

## Context

Ticket #481 — Timeline Draft/Publish Workflow. Assigned to me, with Laurie (lroderick26) as co-assignee and reviewer.

---

## 1. Ticket explicitly required upfront planning review

The ticket (written by Laurie) stated:
- "Put together the proposed workflow, database schema changes, and API contract and send those to Laurie and Skye for input and review"
- "Present your implementation plan covering the necessary endpoints and migration strategy"

I did this — posted a detailed proposal on the ticket before implementation.

---

## 2. Design questions came during PR review instead of during planning

Despite the proposal being posted on the ticket, the substantive design feedback arrived only after the code was written and the PR was open. Examples:
- The 409 lock removal (Laurie's comment on the ticket after the plan was posted)
- Validate on save vs. separate validate call (same comment)
- The `failed` state concern (raised on the PR, not during planning)
- The "what's live?" question about superseded timelines (raised on the PR)
- Publish by UUID vs. publish latest (raised on the PR)

Each of these required code changes after implementation was complete.

---

## 3. Iterative one-question-at-a-time pattern

Rather than collecting all concerns and delivering them at once, the feedback came in sequential rounds. Each round:
- A question is raised
- I implement a solution
- A new review happens
- A new follow-up question appears based on the solution

This happened at least 4-5 times on this single PR (lock removal → validate on save → failed state → superseded → "but what about failure case of superseded?").

---

## 4. Questions without proposed solutions

The feedback style is: "I think we need to think through X" or "How does the frontend do Y?" without proposing an answer. This puts the full burden of both identifying the problem AND solving it on the implementer, then subjects the solution to another round of review that may generate another question.

---

## 5. The ticket had a section explicitly for questions and planning

The ticket included "Open Questions" and "Questions and Clarifications" sections, and said "please read through this ticket and provide any questions/feedback directly here." The implication was that design discussion happens on the ticket. But the actual design discussion happened on the PR after implementation.

---

## 6. Impact: multiple rework cycles on a 2-3 day task

The original ticket estimated 1-2 days planning + 2-3 days development. The implementation itself was completed efficiently. However, addressing iterative PR feedback (lock removal, validate on save, superseded state, failed state discussion) each required going back into the code, modifying logic, updating tests, and re-running the full test suite. This multiplies the effort.

---

## 7. This is a recurring pattern

This happens constantly with all team members, not just on this PR. Previously raised with manager without significant results.

---

## 8. The informal authority dynamic

Laurie is not formally a manager or above in hierarchy, but informally positioned (by manager's support) as a gatekeeper/reviewer whose approval is required. This means the iterative feedback loop cannot be bypassed or pushed back on without escalation.

---

## Summary of the core inefficiency

The process asks for upfront planning review → planning review doesn't happen substantively → code is written → design-level feedback arrives during code review → multiple rework cycles occur → task takes 2-3x the estimated effort. The feedback itself is valid (the questions are real), but the timing and delivery pattern creates avoidable rework.