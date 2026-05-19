# Concrete Example — Scratchpad

## Project Candidates

Five projects were considered, each sized for a team of 4–5 developers over 6–9 months:

1. **Multi-tenant e-commerce marketplace** — Seller onboarding, product catalog, order lifecycle, payment splitting, review/rating system, admin dashboard API. Clear domain boundaries, lots of state machines (order status, payout status), integrations (payment provider, email, shipping).

2. **Event ticketing platform** — Event creation, venue/seat management, real-time availability, checkout with payment, QR code entry validation, waitlist/notification system. Mix of CRUD, real-time constraints, and a clear user-facing flow from discovery to gate entry.

3. **Logistics & delivery tracking system** — Order intake, route planning, driver assignment, real-time GPS tracking API, delivery state machine (picked up → in transit → delivered → confirmed), customer notification, dispute resolution. Heavy on state transitions and external integrations.

4. **Internal developer platform** — Service registry, environment provisioning, build/deploy pipeline orchestration, rollback mechanism, secrets management, audit logging, Slack/webhook notifications. Meta-relevant to the AI workflow theme — a tool for developers, built by developers.

5. **Property management SaaS** — Landlord/tenant onboarding, lease lifecycle, maintenance request workflow (reported → assigned → scheduled → completed), payment collection, document generation (contracts, invoices), inspection scheduling. Very process-heavy, many parallel workflows, clear role-based access.

---

## Selected Project: Event Ticketing Platform

Chosen for clarity and broad accessibility — everyone understands buying a ticket to an event. The domain has enough complexity (real-time availability, payments, concurrency, multiple user roles) to demonstrate meaningful breakdown without requiring specialized knowledge.

---

## Epic Breakdown (Classic Agile, No AI Assistance)

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

## Epic 7: QR Code & Entry Validation — Definition Without AI-Assisted Standards

This is what a typical agile team produces as an epic definition:

**Epic:** QR Code & Entry Validation

**Description:** Generate QR codes for tickets and build a validation endpoint for scanning at the gate. Prevent double-entry.

**Acceptance:** Each ticket has a QR code. Scanning validates and marks as used. Can't use the same ticket twice.

**Estimated duration:** 1 sprint.

---

## Epic 7: QR Code & Entry Validation — Definition With AI-Assisted Standards

After human breakdown, AI documents the epic per universal standards:

**Intent:** Provide a secure, fast, and reliable entry mechanism at event venues — generating a unique, cryptographically verifiable QR code per ticket at purchase time and validating it at the gate — so that only confirmed ticket holders gain entry and no ticket can be used more than once.

**Scope:**
- In: QR code generation triggered on order confirmation (CONFIRMED status), QR payload containing a signed token (ticket ID, event ID, attendee reference, cryptographic signature), validation endpoint (accepts scanned payload, verifies signature, checks ticket status, marks as USED), double-entry prevention (USED status is terminal), offline-capable validation (signature verification requires no database call — network-optional basic check), entry log (timestamp, gate ID, validator device ID per scan).
- Out: QR code visual design/branding (plain standard QR with embedded data), mobile wallet integration (Apple Wallet, Google Pay passes), re-issuance of lost QR codes (support flow, not system feature), entry for non-ticket holders (guest lists, press passes — separate system).

**Completion Criteria:**
- [ ] Upon order reaching CONFIRMED status, a unique QR code is generated for each ticket in the order. QR payload is a signed JWT containing: ticket UUID, event UUID, ticket type, attendee reference, issued-at timestamp.
- [ ] Signing uses an asymmetric key pair (RS256). Private key held server-side only. Public key distributed to validation devices.
- [ ] Validation endpoint accepts QR payload, verifies JWT signature, checks ticket status in database (VALID → USED transition), returns accept/reject response in under 100ms for online mode.
- [ ] Offline validation mode: validator device verifies JWT signature locally using public key. Accepts if signature valid and event ID matches. Logs entry locally, syncs to server when connectivity resumes. Offline mode cannot check for double-entry across gates — accepted tradeoff.
- [ ] Double-entry prevention: once a ticket is marked USED (online mode), any subsequent scan of the same QR returns REJECTED with "already used" reason, gate ID, and timestamp of first use.
- [ ] Entry log records every scan attempt (success and failure): ticket ID, timestamp, gate/device ID, online/offline mode, result.
- [ ] QR code is delivered to attendee via: embedded in confirmation email, retrievable via order detail endpoint. No separate "ticket download" flow.

**Dependencies:**
- Requires: Order confirmation flow (Epic 6, Task 2) — QR generation triggers on CONFIRMED status. Order data model provides ticket ID and attendee reference.
- Unblocks: Entry reporting in Epic 9 (check-in rates, peak entry times derived from entry log).

**Risks / Assumptions:**
- Assumption: RS256 key rotation is not needed within a single event lifecycle. One key pair per event is generated at event creation and used for all tickets in that event.
- Assumption: Offline mode is a degraded-but-acceptable experience. The tradeoff (cannot prevent cross-gate double-entry while offline) is accepted because connectivity loss at venues is temporary and rare.
- Risk: If QR payload grows (additional fields requested later), QR code density increases and older/cheaper scanners may fail to read. Payload must stay minimal — only IDs and signature, no human-readable data in the QR itself.
- Risk: JWT signed tokens are valid forever unless explicitly revoked. If a refund occurs after QR is generated, the system must check ticket status in the database (online mode) — the signature alone is not sufficient to determine current validity. This means offline mode will accept refunded tickets until sync occurs.

---

## Epic 6: Checkout & Payment — Definition Without AI-Assisted Standards

This is what a typical agile team produces as an epic definition:

**Epic:** Checkout & Payment

**Description:** Implement the checkout flow. Users should be able to add tickets to a cart, pay via Stripe, and receive confirmation. Handle refunds and edge cases like double-purchasing.

**Acceptance:** Users can buy tickets and receive confirmation. Refunds work. No double-selling.

**Estimated duration:** 3 sprints.

---

## Epic 6: Checkout & Payment — Definition With AI-Assisted Standards

After human breakdown, AI documents the epic per universal standards:

**Intent:** Enable attendees to purchase tickets through a reliable, conflict-free checkout process — from seat selection through payment to confirmed order — so that the platform can generate revenue and attendees receive guaranteed entry.

**Scope:**
- In: Cart with temporary seat holds, Stripe payment integration (PaymentIntent, 3D Secure, webhooks), order lifecycle state machine (reserved → pending_payment → confirmed → refund_requested → refunded → cancelled), confirmation email, refund flow with organizer approval, concurrent purchase protection at database level.
- Out: Alternative payment providers (Stripe only), installment/financing options, automatic refunds without organizer approval, receipt PDF generation, physical ticket mailing, cart persistence across devices (single-session only).

**Completion Criteria:**
- [ ] Attendee can select tickets, hold corresponding seats for a configurable duration, and proceed to payment within that window.
- [ ] Payment processes through Stripe with idempotency, 3D Secure support, and webhook-based confirmation (no client-side-only confirmation).
- [ ] Confirmed order triggers email with event details and order reference. QR code generation is handled by a separate epic.
- [ ] Order state machine enforces legal transitions only — no invalid state changes are possible via API.
- [ ] Organizer can approve or deny refund requests. Approved refunds trigger Stripe refund and release seats to inventory.
- [ ] Under concurrent load (50+ simultaneous purchases for last available seat), exactly one order succeeds and zero oversells occur.
- [ ] Seat holds expire automatically and release inventory without manual intervention.

**Dependencies:**
- Requires: Venue & seating model (Epic 3) for seat hold mechanics, ticket types & pricing (Epic 4) for price calculation and availability.
- Unblocks: QR code generation (Epic 7) triggers on CONFIRMED order status, waitlist (Epic 8) triggers on seat release from refund, reporting (Epic 9) reads order and refund data.

**Risks / Assumptions:**
- Assumption: Stripe webhooks are the single source of truth for payment status. The system never marks an order confirmed based on client-side signals alone.
- Assumption: PostgreSQL row-level locking is sufficient for expected concurrency (up to 10,000 simultaneous users per high-demand event).
- Risk: Stripe webhook delivery delays during incidents could leave orders in pending_payment state beyond the expected window. A fallback reconciliation mechanism is needed.
- Risk: General admission events (no individual seats) require a different concurrency pattern — atomic counter decrement vs. row-level seat locking. Both patterns must be implemented.

---

## Task Breakdown — Without AI-Assisted Standards

Sprint planning produces these tickets for Epic 6. Each has a title and a brief description:

**Sprint 10:**
1. Implement shopping cart — *"User can add tickets to cart and view cart contents"*
2. Add seat hold/reservation on cart add — *"When user adds tickets, hold those seats temporarily"*
3. Cart expiration logic — *"Cart should expire after some time"*
4. Stripe integration — *"Integrate Stripe for payments"*

**Sprint 11:**
5. Order model and state transitions — *"Create order entity with statuses"*
6. Process payment and create order — *"After successful payment, create a confirmed order"*
7. Send confirmation email — *"User receives email after purchase"*
8. Handle payment failures — *"If payment fails, show error and release seats"*

**Sprint 12:**
9. Refund flow — *"Organizer can approve refunds"*
10. Concurrent purchase protection — *"Two users shouldn't be able to buy the same seat"*
11. Order history endpoint — *"User can view past orders"*
12. Edge cases and bug fixes — *"Handle remaining edge cases from QA"*

**What happens in practice:**

- Ticket 1: Developer builds the cart. Does it persist across sessions? Is there a max quantity? Can you mix ticket types from different events? Nobody said.
- Ticket 2: "Hold those seats temporarily" — for how long? What happens if the user closes the browser? Is the hold per-seat or per-cart? Developer guesses 10 minutes, reviewer wanted 15, product wanted 5.
- Ticket 4: "Integrate Stripe" — just the charge? What about webhooks for async confirmation? What about 3D Secure? What about idempotency keys for retries? Developer delivers the basic charge. Review says it's incomplete. Back-and-forth begins.
- Ticket 5: "Create order entity with statuses" — which statuses? What transitions are legal? Can an order go from confirmed back to pending? Developer invents a state machine. It doesn't match what ticket 9 (refunds) will need. Rework in Sprint 12.
- Ticket 10: Shows up in Sprint 12 as a one-liner. This is actually a concurrency problem requiring either database-level locking or optimistic versioning. It gets "spiked" and pushed to next sprint.
- Ticket 12: Exists because tickets 1–11 were vague. It's a buffer ticket for all the rework.

Three sprints planned. Actual delivery: 3.5–4 sprints. One sprint of time lost to ambiguity, rework, and review cycles.

---

## Task Breakdown — With AI-Assisted Standards

After human breakdown, AI documents each task per standards. Result: 4 tasks instead of 12, each fully defined.

---

### Task 1: Cart and Seat Reservation

**Intent:** Allow attendees to select tickets, hold the corresponding seats, and maintain that selection for a limited time while they complete purchase — so that the checkout flow has a stable, conflict-free window.

**Scope:**
- In: Cart creation, add/remove items, seat hold on add, automatic release on expiration or removal, cart persistence (cookie-based session, no login required), maximum 8 tickets per cart per event.
- Out: Payment processing, order creation, cross-event carts (one event per cart).

**Completion Criteria:**
- [ ] Adding a ticket type + quantity to the cart creates a hold on the corresponding seats (general admission: decrements available count; assigned seating: marks specific seats as held).
- [ ] Hold duration is configurable per event (default: 10 minutes). Expired holds release automatically via scheduled job running every 60 seconds.
- [ ] Cart persists across page reloads within the same session. Closing the browser and returning after hold expiration shows an empty cart.
- [ ] Attempting to add seats that are already held by another session returns 409 with a clear message.
- [ ] Removing an item from cart immediately releases the hold (no wait for expiration).
- [ ] Cart rejects additions beyond 8 tickets per event with 400 response.

**Dependencies:**
- Requires: Venue & seating model (Epic 3), ticket types with availability (Epic 4).
- Unblocks: Task 2 (payment and order creation reads from cart).

**Risks / Assumptions:**
- Assumption: 60-second scheduled cleanup is acceptable granularity — a seat could remain "phantom held" for up to 60 seconds after browser close.
- Risk: High-demand on-sale events may produce bursts of concurrent hold attempts on the same seats. The hold mechanism must use database-level atomic operations (SELECT FOR UPDATE or equivalent), not application-level checks.

---

### Task 2: Payment Processing and Order Confirmation

**Intent:** Convert a valid cart into a paid, confirmed order — handling the full Stripe payment lifecycle including asynchronous confirmation and failure recovery — so that the user receives a guaranteed ticket and the organizer receives revenue.

**Scope:**
- In: Stripe PaymentIntent creation, 3D Secure handling (redirect flow), webhook processing for async payment confirmation, idempotency keys on all Stripe calls, order creation on successful payment, confirmation email trigger.
- Out: Refunds (Task 3), order history (Task 4), receipt PDF generation.

**Completion Criteria:**
- [ ] Submitting checkout creates a Stripe PaymentIntent with idempotency key derived from cart ID. Repeated submissions do not create duplicate charges.
- [ ] If 3D Secure is required, API returns client_secret for frontend redirect. Order remains in "pending_payment" until webhook confirms.
- [ ] Webhook endpoint receives `payment_intent.succeeded` → creates order with status CONFIRMED, converts held seats to sold, sends confirmation email.
- [ ] Webhook receives `payment_intent.payment_failed` → releases seat holds, marks cart as failed with user-facing reason.
- [ ] Order record contains: attendee reference, event, ticket type, quantity, unit price, total, payment intent ID, timestamps.
- [ ] Confirmation email contains: event name, date, venue, ticket details, order ID. QR code generation is NOT included (separate epic).
- [ ] If webhook is not received within 15 minutes of PaymentIntent creation, a scheduled job flags the order for manual review (does not auto-cancel — payment may have succeeded).

**Dependencies:**
- Requires: Task 1 (cart with held seats).
- Unblocks: Task 3 (refund operates on confirmed orders), Epic 7 (QR generation triggers on CONFIRMED status).

**Risks / Assumptions:**
- Assumption: Stripe webhooks are the source of truth for payment status. The API never confirms an order based solely on client-side callback.
- Risk: Webhook delivery delay during Stripe incidents could leave orders in "pending_payment" longer than 15 minutes. The manual review fallback handles this, but operations team needs alerting.

---

### Task 3: Refund Flow

**Intent:** Allow organizers to process full refunds on confirmed orders — with explicit approval workflow — so that attendees can recover funds and released seats return to available inventory.

**Scope:**
- In: Attendee requests refund (creates refund request), organizer reviews and approves/denies, approved refund triggers Stripe refund, seat release on successful refund, refund confirmation email.
- Out: Automatic/self-service refunds without organizer approval, partial ticket refunds (refund is per-order, not per-seat within an order), chargeback handling.

**Completion Criteria:**
- [ ] Attendee can request refund on a CONFIRMED order. Order transitions to REFUND_REQUESTED. Request includes reason (free text).
- [ ] Organizer sees pending refund requests for their events. Can approve or deny with a note.
- [ ] Approval triggers Stripe refund via API. On success: order status → REFUNDED, seats released back to available inventory, refund confirmation email sent to attendee.
- [ ] Denial sends email to attendee with organizer's note. Order remains CONFIRMED.
- [ ] Refund cannot be requested on orders older than 30 days (configurable per event). Returns 400 with explanation.
- [ ] Partial amount refunds are not supported in this task — the full order amount is refunded or nothing.

**Dependencies:**
- Requires: Task 2 (confirmed orders with Stripe PaymentIntent IDs).
- Unblocks: Reporting (Epic 9 needs refund data for revenue calculations).

**Risks / Assumptions:**
- Assumption: Stripe refund processing is near-instant for card payments. For bank transfers, delays are communicated via email but not tracked in our system.
- Risk: Releasing seats on refund for a nearly sold-out event may trigger waitlist notifications (Epic 8). This interaction is out of scope for this task but must not break — refund should not fail if waitlist system is not yet built.

---

### Task 4: Concurrent Purchase Protection and Order History

**Intent:** Guarantee that no seat is sold twice under any race condition, and provide attendees a view of their purchase history — so that the platform's inventory integrity is absolute and users can reference past transactions.

**Scope:**
- In: Database-level locking on seat purchase (not just hold), conflict detection at payment confirmation time, order history list endpoint with pagination, order detail endpoint.
- Out: Analytics, export, admin-level order search.

**Completion Criteria:**
- [ ] At payment confirmation (webhook handler), seat status change from HELD to SOLD uses an atomic UPDATE with WHERE status = 'held' AND holder_session = current_session. If affected rows = 0, payment is refunded automatically and user is notified.
- [ ] Load test: 50 concurrent checkout attempts for the last remaining seat. Exactly one succeeds, 49 receive a clear "seat no longer available" error, zero oversells.
- [ ] Order history endpoint returns all orders for the authenticated attendee, sorted by date descending, paginated (20 per page).
- [ ] Order detail endpoint returns full order information including current status, ticket details, and refund status if applicable.
- [ ] Orders in PENDING_PAYMENT status older than 15 minutes do not appear in order history (they are not confirmed purchases).

**Dependencies:**
- Requires: Task 2 (order records exist), Task 1 (seat hold model).
- Unblocks: None — this is a hardening and completeness task.

**Risks / Assumptions:**
- Assumption: PostgreSQL row-level locking (SELECT FOR UPDATE) provides sufficient concurrency control for expected load (up to 10,000 simultaneous users per event).
- Risk: If the venue model allows general admission (no individual seats), the "50 concurrent" scenario becomes a counter decrement race. Same atomic pattern applies but on a quantity field rather than individual seat rows.

---

## The Difference (Summary)

| | Classic (12 tickets) | Standards-driven (4 tasks) |
|---|---|---|
| Tasks | 12, small, vague | 4, larger, fully defined |
| Rework | ~1 sprint lost to misinterpretation | Near zero — criteria are checkable before submission |
| Review cycles | 2–3 rounds per ticket average | 1 round — pass/fail against criteria |
| Edge cases | Discovered during QA (Sprint 12) | Defined upfront (concurrency, expiration, webhooks) |
| Developer questions during sprint | Frequent, blocking | Rare — scope answers them in advance |
| Actual delivery | 3.5–4 sprints | 2.5–3 sprints |

The same scope. The same team. Fewer pieces, better defined, delivered faster.

---

## Sprint 6 Estimation Notes

### Basis of estimation

All estimates are per-developer per-task — how long one developer takes to complete one task. Sums represent total effort, not calendar time.

### Per-task estimates (without AI-assisted coding)

- **Task 5: Link venue to event** — 1–1.5 days. Standard FK + endpoint + validation. The overlap check adds a half day over a plain FK assignment. Well-understood pattern.
- **Task 6: Seat availability tracking** — 3–4 days. Two separate implementations (status column vs. atomic counters), state transition validation, service interface that dispatches by mode. The dual-mode requirement roughly doubles the work compared to a single-mode status tracker.
- **Task 7: General admission mode** — 1–3 days (high variance). If Task 6 was well-defined and already handles both modes, Task 7 is nearly empty. If Task 6 was built for assigned seating only (which happens with vague definitions), Task 7 becomes a retrofit/rework task that can take 3+ days. In the standards-driven version, this task arguably doesn't need to exist separately — it's absorbed into Task 6.
- **Task 8: Availability API endpoint** — 1–2 days. Read-only endpoint querying existing data. Straightforward unless performance requirements are unclear (then add a day for query optimization or denormalization).

**Sprint total:** 6–10.5 days of actual developer work across 4 tasks.

### Team distribution and dependency chain

These tasks are mostly sequential:

```
Task 5 (1–1.5 days) → Task 6 (3–4 days) → Task 7 (1–3 days)
                                           → Task 8 (1–2 days)
```

Task 6 can't start until Task 5 is done (needs the venue-event link to know which mode to use). Tasks 7 and 8 can't start until Task 6 is done (they both depend on the availability data model). Tasks 7 and 8 can run in parallel with each other.

Having 5 developers doesn't help much here — the critical path is still Task 5 → Task 6 → Task 7, which is 5–8.5 days of sequential work. At most you save 1–2 days by parallelizing Task 7 and Task 8.

This is a realistic sprint problem: 5 developers, but only 1–2 can be productive on this epic at any given time because of internal dependencies. The other 3 are either idle on this epic, assigned to a different epic running in parallel, or doing tasks from Sprint 5 that are still in progress.

### Variance source

The estimation variance (6 vs 10.5 days) is almost entirely in Task 7 — which exists as a separate task only because Task 6 was defined without considering both modes. With proper standards, Sprint 6 is closer to 6–7 days. Without, it's 9–11.

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

## Estimation Summary

### Three scenarios compared

**Baseline: No standards, no AI coding**
- Sprint 6 total: ~8-10 days
- Includes: rework from misunderstood scope (~1-2 days), multiple review rounds (~1 day), blocked time waiting for clarification (~0.5-1 day)
- Developer writes wrong code, gets rejected, rewrites. Review is opinion-based — "I thought you meant something else."

**With AI-assisted standards only, no AI coding (~40% reduction)**
- Sprint 6 total: ~5-6 days
- Coding effort per task stays roughly the same — developer still writes code at human speed
- Savings come from eliminating: rework (wrong direction never taken), extra review rounds (1 round instead of 2-3), blocked time (scope answers questions in advance)
- The developer doesn't write the *wrong* code — that's the 40%

**With AI-assisted standards + AI coding (~80% reduction)**
- Sprint 6 total: ~1.5-2 days
- Implementation per task: 1-2 hours (definition contains the approach, AI generates code, developer reviews)
- Review: ~15 minutes per task (criteria are pass/fail checkboxes, AI does first pass, human confirms)
- Total per task including coordination overhead: ~4 hours worst case
- Savings compound: standards eliminate *wasted* work, AI coding accelerates *correct* work

### Why the two improvements compound

Standards make AI coding more effective — AI performs dramatically better on well-defined tasks with explicit scope and approach guidance. AI coding makes standards more valuable — the faster you execute, the more definition quality becomes the bottleneck rather than coding speed. They target different waste: standards eliminate wrong direction, AI coding accelerates right direction.

### Team composition impact

**All seniors + standards + AI coding:**
- Task 5: 30-45 min implementation + 10 min review
- Task 6: 1-1.5 hours implementation + 15 min review
- Task 7: 15-30 min + 10 min review
- Task 8: 30-45 min + 10 min review
- Sprint total: ~1 day (~90-93% reduction)
- Seniors don't need AI context to understand — they need it to confirm approach and skip decision-making. They recognize correct AI output instantly.

**All juniors + standards + AI coding:**
- Implementation per task: 2-4 hours (need to understand AI context, verify more carefully)
- Review: 30-60 minutes (less confidence in verdict)
- Sprint total: ~1.5-2 days
- Risk: juniors may accept AI output that superficially passes criteria but has subtle issues

**Gap narrowing effect:**
- Without standards: seniors 3-4 days, juniors 7-10+ days (gap: 2-3x)
- With standards + AI coding: seniors 1 day, juniors 1.5-2 days (gap: ~1.5x)
- The framework compensates for experience by making decisions explicit in the definition rather than requiring them to live in the developer's head.

### Realistic team scenario

A team of 2 seniors, 2 juniors, and 1 coordinator — applying AI-assisted standards + AI-assisted coding — can achieve approximately 80% time reduction on well-defined backend tasks. The seniors drive the complex tasks and review; the juniors handle the simpler tasks and learn from the explicit definitions. The coordinator ensures dependencies are respected and reviews are timely. The 80% figure accounts for the mix of speeds across skill levels and the coordination overhead of a distributed remote team.
