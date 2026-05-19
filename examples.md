# AI-Assisted Development Workflow — Examples

This document provides a concrete set of examples demonstrating the framework in practice. It starts with the documentation standards, then applies them to a realistic project — showing the difference between a traditional agile definition and one produced with AI-assisted standards.

---

## Standards

What follows is a sample universal standard — one possible set of fields that every work item at any hierarchy level (epic, task, subtask) would carry. This is not the only way to structure it; the specific fields, their names, and their definitions can be reworked, expanded, or simplified depending on the organization, the domain, or the project. The point is that a standard exists, is explicit, and is applied consistently.

Each field in the standard should be designed to serve two audiences. The first is the human — planners, developers, managers — who need to read, understand, drive, orchestrate, and correct the process. The second is the AI, which uses the field definitions operationally: to produce structured documentation, enforce completeness, verify deliverables, and flag inconsistencies. Both parts are written in human-readable language, but they serve different purposes. The human-facing aspect is for understanding and steering. The AI-facing aspect is for the framework to function mechanically — it is what makes the define-execute-verify cycle work without requiring subjective judgment at the review step.

The five fields:

**1. Intent**
What is being done and why. A single statement that connects purpose to action. This prevents completing the letter of the work while missing its spirit. Without intent, a developer can build something that technically works but doesn't serve the actual goal.

**2. Scope**
What is in and what is out. Explicit boundaries of the work. This is the most commonly skipped field in practice and the single biggest source of misalignment and rework. If the boundary is not stated, two people will draw it differently.

**3. Completion Criteria**
How a reviewer verifies the work is done. A list of concrete, yes/no checkable conditions. This is the load-bearing mechanism of the entire framework — it makes review mathematical rather than opinion-based. Both the developer and the reviewer operate against the same checklist. AI-assisted review becomes possible precisely because these criteria are measurable and unambiguous.

**4. Dependencies**
What must be satisfied before this work starts, and what does this work unblock. This serves as a gate — without satisfying incoming dependencies, there is no reason to begin the work. Dependencies can be enforced the same way as completion criteria: as checkpoints verified before a task is assigned. The "unblocks" direction makes the critical path visible and prevents invisible bottlenecks.

**5. Risks / Assumptions**
What could make this work wrong or harder than expected, and what unverified assumptions does it rest on. This field serves an orchestration function: based on the results of the current work item, future work items downstream may need to be redesigned. When an assumption is proven false or a risk materializes, this field tells you which other pieces in the plan are affected and need correction — before they are started, not after they are delivered.

---

## Example Project: Event Ticketing Platform

An event ticketing platform — covering event creation, venue/seat management, real-time availability, checkout with payment, QR code entry validation, and waitlist/notification systems. The domain involves a mix of CRUD operations, real-time constraints, payment integration, concurrency challenges, and multiple user roles (organizers, attendees, platform admins). It follows a clear user-facing flow from event discovery to gate entry.

This project is chosen for clarity and broad accessibility — everyone understands buying a ticket to an event. The domain has enough complexity to demonstrate meaningful breakdown without requiring specialized knowledge. It is sized for a team of 5 developers working over approximately 8 months in 2-week sprint cycles.

---

## Epic Breakdown. Classic Agile

Team: 5 developers, 2-week sprints, ~16 sprints total (8 months).

**Epic 1: Foundation & Infrastructure (Sprints 1–2)**
Project scaffolding, CI/CD pipeline, database setup, authentication (organizer + attendee roles), base API structure, deployment to staging environment. By end: a running app that does nothing useful but is deployable and has login.

**Epic 2: Event Creation & Management (Sprints 3–4)**
Organizer can create, edit, publish, and archive events. Event has metadata (name, description, date/time, location, category, images). Draft/published/cancelled state machine. List and detail endpoints for public consumption.

**Epic 3: Venue & Seating (Sprints 5–6)**
Venue model (capacity, sections, rows, seats). Two modes: general admission (capacity-only) and assigned seating (seat map). Seat map upload/configuration. Link venue to event. Seat availability tracking (the data model, not yet real-time).

**Epic 4: Ticket Types & Pricing (Sprints 7–8)**
Ticket categories per event (VIP, general, early bird). Price tiers with date-based activation (early bird expires on date X). Quantity limits per tier. Promo codes / discount logic. Ticket availability calculated from venue capacity minus sold.

**Epic 5: Search & Discovery (Sprint 9)**
Public event listing with filters (date, category, location, price range). Full-text search. Sorting (date, popularity, price). Pagination. Featured/promoted events flag.

**Epic 6: Checkout & Payment (Sprints 10–12)**
Cart model (hold seats temporarily during checkout). Payment provider integration (Stripe or equivalent). Order lifecycle: reserved → paid → confirmed → refunded/cancelled. Email confirmation with order details. Refund flow with organizer approval. Concurrent purchase protection (two people buying last seat).

**Epic 7: QR Code & Entry Validation (Sprint 13)**
Generate unique QR code per ticket upon purchase. Validator endpoint (scan → verify → mark as used). Prevent double-entry. Offline-capable validation (signed token in QR, no network required for basic check). Entry log with timestamps.

**Epic 8: Waitlist & Notifications (Sprint 14)**
Join waitlist when event/tier is sold out. Notification when spot opens (seat released, capacity increased). Time-limited claim window — expires back to waitlist if not purchased. Email + push notification integration.

**Epic 9: Reporting & Admin (Sprints 15–16)**
Organizer dashboard: sales by tier, revenue, check-in rate, refund rate. Platform admin: all events, all organizers, flag/suspend, revenue share reporting. Export (CSV). Basic analytics (peak purchase times, conversion funnel).

---

## Epic 3: Venue & Seating — Definition Without AI-Assisted Standards

This is what a typical agile team produces as an epic definition:

**Epic:** Venue & Seating

**Description:** Build the venue and seating model. Support general admission and assigned seating. Organizers should be able to configure their venue layout and link it to events.

**Acceptance:** Venues can be created with sections and seats. Events can be linked to a venue. Availability is tracked.

**Estimated duration:** 2 sprints.

---

## Epic 3: Venue & Seating — Definition With AI-Assisted Standards

After human breakdown, AI documents the epic per universal standards:

**Intent**
Build the venue and seating system that models physical event spaces — their capacity, layout, sections, and individual seats — so that the platform knows what can be sold, how much of it remains, and whether a given seat is available at any moment. This is the inventory foundation the entire checkout flow (Epic 6) will operate against.
*AI context:* This epic produces the data model that all downstream availability checks depend on. When generating completion criteria or reviewing deliverables for this epic, validate that both venue modes (general admission and assigned seating) are treated as first-class paths — not one as default and the other as edge case. Every criterion must hold for both modes independently.

**Scope**
- In: Venue entity (name, address, total capacity), section model (named zones within a venue), row and seat model (for assigned seating), two venue modes (general admission: capacity-only, no individual seats; assigned seating: every seat is a discrete, bookable entity), seat map configuration by organizer, venue-to-event linking (one venue per event, one event can reuse a venue), real-time availability data model (seat status: available / held / sold).
- Out: Visual seat map rendering (frontend concern), dynamic pricing per seat location (Epic 4 handles pricing), multi-venue events (festival across stages — future scope), seat map import from third-party providers (manual configuration only in this epic).

*AI context:* When assisting the developer with implementation, treat the two venue modes as separate code paths that share a common interface — do not attempt to unify them into a single generic model. The venue entity, section, and row/seat hierarchy should be modeled as relational tables with foreign keys. Seat status (AVAILABLE, HELD, SOLD) belongs on the seat record for assigned seating, and as an aggregate counter on the section/venue for general admission. The availability endpoint should query pre-computed values, not calculate on the fly. Anything listed as "out" is not to be scaffolded, stubbed, or prepared for — build only what is "in."

**Completion Criteria**
- [ ] Organizer can create a venue with general admission mode — specifying total capacity and optionally named sections with sub-capacities that sum to total.
- [ ] Organizer can create a venue with assigned seating mode — defining sections, rows within sections, and individual seats within rows. Each seat has a unique identifier within the venue.
- [ ] Venue mode is immutable after first ticket is sold against it (prevents structural changes that would invalidate existing orders).
- [ ] Organizer can link a venue to an event. One event has exactly one venue. A venue can be reused across multiple non-overlapping events.
- [ ] Seat status model supports three states: AVAILABLE, HELD, SOLD. Status transitions are enforced (AVAILABLE → HELD → SOLD, HELD → AVAILABLE on expiration, SOLD → AVAILABLE on refund). No other transitions are legal.
- [ ] For general admission venues: availability is a single integer counter (capacity minus held minus sold). For assigned seating: availability is per-seat status.
- [ ] API endpoint returns venue layout with current availability (section-level summary for large venues, seat-level detail for individual section queries).
- [ ] Venue with 10,000+ seats performs availability queries in under 200ms.

*AI context:* You are reviewing the deliverable for this epic. Evaluate each criterion independently as pass or fail. A criterion passes only when you can confirm it through code, tests, or measurable evidence — not through developer assertion. For criteria mentioning both venue modes, verify each mode separately; passing in one mode does not satisfy the other. The performance criterion (200ms for 10,000+ seats) requires a benchmark or load test result as evidence. Produce a per-criterion verdict and an overall accept/reject decision. If any criterion fails, specify exactly what is missing or incorrect.

**Dependencies**
- Requires: Event creation (Epic 2) — events must exist to be linked to venues.
- Unblocks: Ticket types & pricing (Epic 4) — ticket tiers map to venue sections. Checkout (Epic 6) — cart hold and purchase operate on seat status model defined here.

*AI context:* Before this epic can begin, check that Epic 2's completion criteria are satisfied — specifically that events exist as entities with stable identifiers that can be referenced by a foreign key. If Epic 2 is not complete, report this epic as blocked and specify which Epic 2 criteria are unmet. Do not allow work to proceed on a blocked epic.

**Risks / Assumptions**
- Assumption: Organizers configure seating manually through the API. No seat map image upload with auto-detection of seats in this epic.
- Assumption: Venue layout does not change between event announcement and event date. If an organizer needs to add/remove sections after tickets are on sale, that is a manual support operation outside the system.
- Risk: The 10,000+ seat performance requirement may require denormalized availability counters (per-section aggregates maintained via triggers or application logic) rather than counting seat rows on every query.
- Risk: The two-mode design (general admission vs. assigned) means all downstream epics must handle both patterns. This is a structural decision that propagates — if the abstraction is wrong here, it creates rework in Epic 4, 6, 7, and 8.

*AI context:* After this epic is completed, compare the listed assumptions against the actual delivered implementation. If any assumption was violated or any risk materialized, identify which downstream epics (Epic 4, 6, 7, 8) depend on that assumption and raise a warning that their definitions may need revision. Do this before downstream work begins — not after. If the two-mode design risk materialized (e.g., the abstraction doesn't cleanly serve both modes), flag this as a structural issue requiring human decision before proceeding.

---

## Sprint 6 Tasks — Classic Definition

**Task 5: Link venue to event**
Associate a venue with an event. An event should have a venue assigned to it.
Story points: 2

**Task 6: Seat availability tracking**
Track which seats are available, held, or sold. Update status when seats are reserved or purchased.
Story points: 3

**Task 7: General admission mode**
Support venues that don't have individual seats. Use capacity-based tracking instead of per-seat tracking.
Story points: 3

**Task 8: Availability API endpoint**
Return venue layout with current availability information. Frontend needs this to display the seat map / availability to the user.
Story points: 3

---

## Sprint 6 Tasks — With AI-Assisted Standards

### Task 5: Link venue to event

**Intent**
Establish the relationship between a venue and an event so that when tickets are created for an event, the system knows which venue's inventory (seats or capacity) they are sold against.

*AI context:* This task creates the data relationship that all ticket and availability logic depends on. Help the developer understand that this is a one-to-one relationship from the event's perspective (one event has exactly one venue) but one-to-many from the venue's perspective (a venue can host multiple events at different times). The linking mechanism must prevent assigning the same venue to two events whose dates overlap.

**Scope**
- In: Add venue_uuid foreign key column to the events table. API endpoint for organizer to assign a venue to their event. Validation: an event can have exactly one venue; a venue can be linked to multiple events only if their date ranges do not overlap. Unlinking a venue is allowed only if no tickets have been sold for that event.
- Out: Creating venues (task 1–4 already done). Modifying venue data through this endpoint. Automatic venue suggestions or matching.

*AI context:* The FK column goes on the events table, not a join table — this is one-to-one from event side. Guide the developer to implement overlap validation by querying existing events linked to the same venue and comparing date ranges. The "no unlink after ticket sale" rule is a business constraint enforced at the service layer, not a database constraint.

**Completion Criteria**
- [ ] Migration adds nullable `venue_uuid` FK column to the events table referencing `cms.venues`.
- [ ] PATCH endpoint allows organizer to assign a venue to an event they own. Returns 200 on success.
- [ ] Assigning a venue to an event that already has a venue replaces the previous assignment (only if no tickets sold).
- [ ] Attempting to link a venue that is already linked to another event with overlapping dates returns 409 with explanation.
- [ ] Attempting to unlink or change venue on an event that has sold tickets returns 400 with explanation.
- [ ] An event without a venue assigned returns `venue: null` in the event detail response.

*AI context:* Verify the migration adds the FK column as nullable. Test the overlap detection: create two events with overlapping dates, assign the same venue to both — second assignment must fail with 409. Test the ticket-sale lock: create an event with venue, simulate a sold ticket, attempt to change venue — must fail with 400. Verify that events with no venue still return successfully from the detail endpoint.

**Dependencies**
- Requires: Venues table exists (task 1). Events entity exists with date fields (Epic 2).
- Unblocks: Task 6, 7, 8 (availability tracking operates on the venue linked to an event). Epic 4 (ticket types are created per event, and their availability derives from the linked venue's capacity).

*AI context:* Check that both `cms.venues` and `cms.events` tables exist with uuid PKs and that events have date columns for overlap comparison. If either is missing or events have no date fields, this task is blocked.

**Risks / Assumptions**
- Assumption: An event has a single start and end date (not multi-day with gaps). Overlap check is a simple range comparison.
- Risk: If events can span multiple non-consecutive days (e.g., a festival on Saturday and Sunday but not Friday), the overlap logic becomes more complex than a single range check. This is not handled here.

*AI context:* After completion, verify whether the overlap logic matches the actual event date model. If events have multiple date entries or recurring schedules, raise a warning — the simple range check implemented here would be insufficient and this task's overlap validation would need revision before Epic 4 or 6 can rely on it.

---

### Task 6: Seat availability tracking

**Intent**
Implement the mechanism that tracks whether each seat (or capacity unit) is available, held, or sold — so that the platform has a single source of truth for what can still be purchased at any moment.

*AI context:* This task requires two distinct implementations — one for assigned seating (status on individual seat records) and one for general admission (atomic counters on section records). These are not variations of the same logic; they are two separate code paths. Help the developer treat them as independent implementations that share a common service interface but differ internally.

**Scope**
- In: For assigned seating — add status column (enum: AVAILABLE, HELD, SOLD) to the seats table with enforced legal transitions (AVAILABLE → HELD → SOLD, HELD → AVAILABLE on release, SOLD → AVAILABLE on refund). For general admission — add available_count, held_count, sold_count columns to the sections table, updated atomically. Service method that performs a state transition given a seat identifier (assigned) or section identifier + quantity (general admission). Validation rejects illegal transitions.
- Out: The trigger logic that calls these transitions (Epic 6 — checkout builds on top of this). Hold expiration timers. API endpoints exposing availability to users (task 8).

*AI context:* For assigned seating, the status column goes on the existing `cms.venue_seats` table from task 4. For general admission, the counters go on `cms.venue_sections`. Guide the developer to implement counter updates as atomic SQL (knex `.increment()`/`.decrement()` or raw UPDATE with arithmetic) — never read-then-write. The service method should accept a mode parameter or resolve it from the venue, then dispatch to the correct implementation. Do not unify the two modes into a single abstraction — keep them as separate internal paths behind one interface.

**Completion Criteria**
- [ ] Migration adds `status` column (enum: AVAILABLE, HELD, SOLD, default AVAILABLE) to `cms.venue_seats`.
- [ ] Migration adds `available_count`, `held_count`, `sold_count` columns to `cms.venue_sections` (for general admission venues, initialized so that available_count = section capacity, held and sold = 0).
- [ ] Service method for assigned seating: accepts seat UUID and target status, validates the transition is legal, updates the record. Returns error on illegal transition.
- [ ] Service method for general admission: accepts section UUID, quantity, and transition direction (e.g., hold 3, sell 2, release 1), updates counters atomically. Returns error if insufficient availability.
- [ ] Illegal transitions are rejected: AVAILABLE → SOLD directly (must go through HELD), SOLD → HELD, or any transition that would make a counter negative.
- [ ] Sum invariant for general admission: available_count + held_count + sold_count = section capacity at all times.

*AI context:* Verify the migration runs and columns exist with correct types and defaults. Test illegal transitions for both modes and confirm rejection. For general admission, verify atomic updates by checking for SQL-level arithmetic operations in the code — flag any pattern that reads the count, modifies in JS, then writes back. Verify sum invariant holds after a sequence of mixed transitions (hold, sell, release).

**Dependencies**
- Requires: Task 4 (seats table exists for status column), Task 3 (sections table exists for counters), Task 5 (venue linked to event — so the system knows which venue mode to use when processing a transition for an event).
- Unblocks: Task 8 (availability endpoint reads from this data). Epic 6 (checkout calls these service methods to hold and sell).

*AI context:* Verify that `cms.venue_seats` and `cms.venue_sections` tables exist. Verify that venue-to-event linking (task 5) is complete — the service method needs to resolve which venue mode applies for a given event. If any prerequisite is missing, this task is blocked.

**Risks / Assumptions**
- Assumption: The service methods created here will be called by Epic 6's checkout logic. This task builds the transition mechanism only, not the business flow that triggers it.
- Risk: Under high concurrency (50+ simultaneous hold attempts on the same section), atomic increment alone may be insufficient — row-level locking (SELECT FOR UPDATE) on the section record may be needed to prevent overselling in general admission mode.
- Risk: The sum invariant is application-enforced. If any code path bypasses the service method and updates counters directly, the invariant breaks silently.

*AI context:* After completion, check whether the concurrency risk is addressed. If the implementation uses simple increment without locking, raise a warning for Epic 6 — under high-demand on-sale events, the current approach may oversell. Also verify that no other code path in the codebase writes to the status column or counter columns directly, bypassing the service method.

---

## Conclusion

Standards-driven documentation — wrapping every task and epic with clear intent, scope, completion criteria, dependencies, and risks — produces measurable time savings even without changing how code is written. Applied alone, without AI-assisted coding, it eliminates rework, reduces review cycles, and removes ambiguity-driven delays, resulting in approximately 40% time reduction. Combined with AI-assisted coding, where the well-defined scope and approach guidance allow AI to generate correct implementations on the first pass, the total reduction reaches approximately 80%.

At this level of acceleration, a new bottleneck emerges. When individual tasks take 1-2 hours instead of 1-2 days, the tasks themselves become too small — the inter-task coordination, review handoffs, context switching, and dependency waiting between tasks becomes the dominant overhead. The process of managing many small tasks costs more time than executing them.

This leads to a necessary revision of the breakdown itself. If tasks can be completed dramatically faster, they should be correspondingly larger. With AI-assisted coding, task scope can grow up to 80% bigger than traditional sizing — what was previously four tasks becomes one well-defined task with broader scope that a developer completes in a single focused session. Without AI-assisted coding but with standards-driven documentation, task scope can still grow up to 40% bigger — because the elimination of rework and review cycles means a developer can reliably handle more in one pass. In both cases, larger well-defined chunks reduce the total number of pieces, reduce coordination overhead, and simplify the planning hierarchy — which is precisely the Virtuous Circle in action.
