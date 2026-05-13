# AI-Assisted Development Workflow — Talking Points

## 0. Introduction

There is a known and widespread fear — present at almost every level of the management hierarchy, from software engineers to near-top management — that AI will replace humans, especially in the software engineering industry. The idea I want to present today attempts to show the opposite. It is possible to use AI to significantly speed up the entire software development cycle — not just the coding, but planning, review, and delivery — without eliminating a single person.

## 1. The Second Problem

Inefficient management — poor planning, vague requirements, endless review loops — is an extremely common condition. It is not limited to the lowest development level; it exists across all levels of the hierarchy. This is the second problem this idea aims to solve. The same framework that accelerates delivery also enforces clarity and structure at every level — reducing the opportunity for inefficiency to compound as work flows through the organization.

## 2. The Core Idea

Use AI to enforce documentation standards at every level of the software development cycle. When planning produces a breakdown — at any level — each resulting piece gets wrapped into a properly defined description with measurable, achievable acceptance criteria. Each of those pieces in turn breaks down further into smaller parts under the same conditions, all the way down to the individual task assigned to a single contributor.

AI is involved twice at every level: first, to help define and document each piece according to the standards; and second, to help review and accept the deliverable against those same criteria. This dual AI involvement at every step significantly speeds up the entire process.

Here is why: when tasks are well-defined and acceptance criteria are clear, an individual developer — especially with AI-assisted planning and execution — can reliably take on a much larger scope of work. Larger individual scope means the project requires fewer breakdown levels and fewer total pieces. Fewer pieces means simpler planning. Simpler planning means better definitions. And the cycle accelerates. This creates what I call a Virtuous Circle — a self-reinforcing loop where each rotation amplifies the next, producing exponential rather than linear improvement in delivery speed.


## 3. How to Implement (High Level)

Let's take the lowest and most tangible level as an example: planning broken down into individual tasks. The implementation requires two things:

1. **Design universal standards** — clear documentation standards and acceptance rules that are not tied to any specific project but applicable across a wide range of them.
2. **Prepare two prompts** — once the standards are defined, create two AI prompts:
   - One for producing well-defined task descriptions with measurable, achievable acceptance criteria (the "define" step).
   - One for reviewing deliverables against those criteria and determining acceptance (the "review" step).

This can be achieved in two ways:

**Approach A — From many projects to common rules.** Study several real projects, analyze what makes task definitions good or bad across different domains, and extract universal standards from these observations. Then design the prompts against those standards.

**Approach B — From one project to common rules.** Start with a specific project, prepare the prompts for it directly, and use them in practice. Then apply to the next project, adapt what doesn't fit, and observe what changed. Iteratively refine through successive projects until the standards and prompts converge into something universal — not by upfront design, but through practical use.

## 4. Example — The Difference in Practice

**Example task:** Add password reset functionality (email-based, with expiring token).

**Without AI-assisted standards (8 tasks):**
1. Create password reset tokens DB table
2. Create token generation service
3. Create "request reset" API endpoint
4. Integrate email sending (reset link)
5. Create "confirm reset" API endpoint
6. Add token expiration validation
7. Add rate limiting for reset requests
8. Write tests

Tasks are kept small deliberately — because without precise definitions, giving a developer "build the password reset flow" results in ambiguity: Do I include rate limiting? What's the token expiration? What email template? Each question either blocks the developer or produces a guess that gets rejected in review.

**With AI-assisted standards (3 tasks):**
1. Build reset request flow — endpoint, token generation, DB storage, email dispatch
2. Build reset confirmation flow — endpoint, token validation, expiration logic, password update
3. Add rate limiting and abuse protection

Each task is larger but fully defined — scope boundaries, token lifetime, rate limits, error responses, and acceptance criteria are all documented before work begins. No guessing, no back-and-forth.

## 5. Conclusion

Once implemented, the standards and prompts can follow a familiar override hierarchy — the same pattern seen in systems like `.gitignore` or `CLAUDE.md`. There are global standards that apply universally, project-level overrides that tailor them to a specific codebase or domain, and local overrides for team- or task-specific adjustments. Each level inherits from the one above and can refine without breaking the whole.