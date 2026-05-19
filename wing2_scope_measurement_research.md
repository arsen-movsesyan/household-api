# Wing 2: AI-Assisted Scope Measurement — Research Starting Point

## Context

This document is part of a larger framework with two complementary parts ("wings"):

**Wing 1: Standards-Driven Development** — already developed. AI wraps every work item (epic, task) with structured documentation per defined standards (Intent, Scope, Completion Criteria, Dependencies, Risks/Assumptions). AI then helps review deliverables against those same criteria. This produces reliable delivery data — actual time per task, actual throughput per developer and per team.

**Wing 2: AI-Assisted Scope Measurement** — this document. The research question: how to use AI to accurately measure the total scope of work to be done, so that breakdown into right-sized pieces becomes calculation rather than guessing.

---

## The Problem

The breakdown formulas already exist and are well understood:

- Milestone scope: M ≈ T(t) × D
- Number of milestones: N ≈ S / (T(t) × D)
- Task scope: Tk ≈ I(t) × (1–3 days)
- Number of tasks: N ≈ M / (I(t) × (1–3 days))

Where:
- S = total project scope (in work units)
- T(t) = team throughput per time period
- I(t) = individual throughput per time period
- D = target duration per milestone

Wing 1 solves the throughput side — by producing reliable delivery data, it makes T and I trustworthy inputs rather than guesses. But the formulas also assume you know **S** — the total scope of work. Measuring S accurately is the actual unsolved problem. If S is wrong, the entire plan is wrong regardless of how well you know T and I.

---

## What "Measuring S" Means

Scope measurement is not estimation in story points or hours. It is determining the actual volume and complexity of work that a project contains — including:

- Visible features and requirements (what stakeholders ask for)
- Hidden complexity (integration points, edge cases, error handling, data migration)
- Implicit dependencies (things that must exist but nobody listed as a task)
- Assumption-driven work (work that only appears when an assumption is proven false)
- Infrastructure and cross-cutting concerns (auth, logging, deployment, testing)

Traditional estimation misses scope because humans are optimistic — they estimate what they can see and forget what they can't. The research question is whether AI can identify the invisible parts of scope that humans routinely miss.

---

## How AI Might Help Measure Scope

Potential approaches (not yet validated — this is the research direction):

1. **Comparative analysis** — AI has exposure to millions of projects. Given a project description, it could identify: "projects like this typically include X, Y, Z that you haven't mentioned — are these in scope or explicitly out?" This surfaces hidden work.

2. **Dependency and integration surface analysis** — Given a list of features, AI could map the integration points between them and estimate the "connective tissue" work that doesn't appear in any single feature's description but must exist for the system to function.

3. **Assumption extraction and risk-sizing** — AI could identify implicit assumptions in a scope document and estimate the additional work each assumption carries if it turns out to be false. This produces a risk-weighted scope rather than a best-case scope.

4. **Historical pattern matching** — If fed delivery data from past projects (from Wing 1), AI could compare new scope to completed similar scope and produce data-driven size estimates rather than opinion-based ones.

5. **Decomposition depth probing** — AI could recursively ask "what does this actually involve?" for each item in the scope until it reaches atomic tasks, then count upward. This produces a bottom-up scope measurement to compare against the top-down estimate.

---

## How the Two Wings Feed Each Other

Wing 1 → Wing 2: Delivery data from standards-driven development (actual task durations, actual throughput) provides the historical base that makes scope measurement calibratable. Without real data, any measurement is a guess.

Wing 2 → Wing 1: Accurate scope measurement produces right-sized work items for Wing 1 to document with standards. If scope is measured correctly, the breakdown matches reality — tasks are neither too big (ambiguous) nor too small (overhead-dominated).

Together: With reliable S (from Wing 2) and reliable T/I (from Wing 1), the sizing formulas become actual calculations. The breakdown is no longer a subjective judgment — it is arithmetic with measured inputs. This is the full realization of the Virtuous Circle.

---

## The Name Problem

"Capacity-Calibrated Slicing" was the original name for this concept, but it describes the *output* (slicing calibrated to capacity) rather than the *hard problem* (measuring scope). The name should reflect what the research is actually about — accurate scope measurement using AI — not the mechanical step that follows once measurement is done. A better name is TBD.

---

## What Remains to Research

- How to represent scope in measurable units that are comparable across projects
- What inputs AI needs to produce a scope measurement (requirements docs, architecture diagrams, comparable past projects, team constraints)
- How to validate a scope measurement (what does "this measurement was accurate" look like retroactively)
- Whether AI can identify the specific categories of hidden scope (integration, infrastructure, edge cases) reliably or only some of them
- How scope measurement accuracy improves over time as more delivery data (from Wing 1) becomes available
- The relationship between scope measurement and the "40-80% bigger tasks" conclusion — if AI measures scope accurately, does the optimal task size follow directly from the formula, or are there additional factors?

---

## Connection to "What's Not Covered" in the Presentation

The presentation document (`presentation_talking_points.md`) lists "Individual's and team's throughput measuring" as a separate research topic. That topic is the T and I side — the inputs that Wing 1 produces. This document is the S side — the other input the formulas need. Together, they complete the picture: measure S, measure T/I, apply formulas, get right-sized breakdown, document with standards, deliver, measure actual results, feed back into next cycle.