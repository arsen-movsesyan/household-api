# AI-Assisted Development Workflow — Session Context and Summary

This file summarizes the full discussion context behind the two deliverables produced in this session. It is intended to be passed to a future AI session for continuity.

---

## What Was Produced

Two files in `app/playground/`:

1. **`ai_assisted_dev_workflow_proposal_final.md`** — The full proposal document. Contains: preface, overview (two parts), Part 1 (Capacity-Calibrated Slicing), Part 2 (Standards-Driven Development) with bad and good ticket examples, the Cascade Boost Cyclone concept, and a closing section on what remains beyond the document. Also contains a scratchpad of older draft material in HTML comments.

2. **`presentation_talking_points.md`** — A concise 15-20 minute presentation structure. Five sections: Introduction (fear vs reality), The Second Problem (inefficient management), The Core Idea, How to Implement, Example, and Conclusion.

The original brainstorming scratchpad remains at **`ai_assisted_dev_workflow_proposal.md`** — it has more detailed breakdowns of capacity formulas, agile hierarchy, breakdown techniques, and the proposed universal core standard (5 fields).

---

## The Core Idea (Definitive Statement)

Use AI to enforce documentation standards at every level of the software development cycle. After humans perform the breakdown at any level, AI helps document each piece with clear descriptions, measurable scope, and achievable acceptance criteria. Then, when the work is delivered, AI helps review it against those same criteria.

**Two distinct AI roles (not to be conflated):**
- AI for defining/documenting (wrapping each piece with standards)
- AI for helping review/accept (verifying deliverables against criteria)

**The Virtuous Circle:** Well-defined tasks → developers handle larger scope → fewer breakdown levels needed → simpler planning → even better definitions → cycle accelerates. Exponential, not linear.

---

## Key Concepts and Terminology

| Term | Meaning |
|------|---------|
| **Cascade Boost Cyclone** | The name for the self-reinforcing cycle in the proposal document (used in formal writing) |
| **Virtuous Circle** | The same concept, simpler name (used in the presentation) |
| **Capacity-Calibrated Slicing** | Part 1 — technique for sizing breakdown pieces against measured capacity (T = team throughput, I = individual throughput, D = duration) |
| **Standards-Driven Development** | Part 2 — using AI to document and review every piece per defined standards |
| **Dual AI involvement** | AI assists at two points: define the task, then help review the result |
| **Vertical axis** | Decomposition / breakdown (planning) |
| **Horizontal axis** | Execution of each individual piece (development) |

---

## Key Decisions Made During Discussion

1. **No problem statement** — deliberately skipped; the problem is too complex to define concisely.
2. **Two-part structure** — Part 1 (measure/size) and Part 2 (define/review). Part 1 was deliberately left incomplete because its inputs (T, I) depend on outputs of the cycle.
3. **AI does not own decisions** — humans break down, humans approve. AI helps document and helps review.
4. **Universal standards + level-specific extensions** — 5 universal fields (Intent, Scope, Completion Criteria, Dependencies, Risks/Assumptions) proposed in the scratchpad. Each hierarchy level adds its own requirements.
5. **Standards hierarchy** — global → project-level → local overrides (like .gitignore or CLAUDE.md).
6. **Two implementation approaches** — A: research many projects first, extract rules. B: start with one project, iterate to universal.
7. **Examples are non-software** — bad ticket (football field), good ticket (mermaid attendance scanner) — deliberately chosen to be domain-agnostic and memorable.
8. **The presentation** is aimed at a technically-minded former manager, ~15-20 minutes, conversational.

---

## Unresolved / Left for Future

- How to measure Individual Throughput (I) and Team Throughput (T) in practice, how AI-assisted development changes these values and their variance, and how to calibrate them over time
- Actual prompt design (the "define" prompt and the "review" prompt)
- Calibration/retrospective process after each cycle
- The broader argument: humans as the most valuable resource, AI companies' failure to position technology as helper not replacement
- Extension of the method to higher hierarchy levels (epic, milestone, project scope)
- Whether to use Approach A or B for implementation

---

## Author's Preferences (for future AI sessions)

- When Arsen provides rough text, rewrite it with better language but keep the idea absolutely unchanged.
- Arsen thinks technically and expresses ideas in raw form — expects linguistic polish, not interpretation.
- The document tone should be direct, personal (first person), and not overly formal.
- Non-software examples are preferred for illustrating concepts (keeps them domain-agnostic).
- "Virtuous Circle" is the working name for presentations; "Cascade Boost Cyclone" for the formal document.