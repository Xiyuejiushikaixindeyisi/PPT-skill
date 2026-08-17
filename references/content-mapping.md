# Content → Motif Routing

Use this decision tree to pick the **primary** motif for each page, then add supporting
motifs to reach density. Confirm the choice with the user before building.

## Decision tree (first match wins)
1. Content has **tasks with start/end dates or a schedule/roadmap** → **E Gantt**.
2. Content describes a **platform / product made of layers** (application/capability/engine/
   data/infra) → **F Layered architecture**.
3. Content is a **multi-role / multi-system hand-off or approval/rework flow** → **G Swimlane**.
4. Content is an **Agent / multi-skill run with iteration/loops** → **A Nested swimlane flow**.
5. Content is a **lifecycle with ordered phases** (design→build→manage→apply) → **B Chevron**.
6. Content is **one function's step-by-step pipeline with sub-classification** → **D Vertical pipeline**.
7. Content is a **timed call/return between systems** (接口时序, tool-call 往返, 消息交互)
   → **H Sequence diagram**.
8. Content is about **where things run / network or cluster zones** (部署、拓扑、云上云下)
   → **I Deployment topology**.
9. Content is **one entity's status lifecycle with events and rework** (工单/订单状态流转)
   → **J State machine**. (Phases of *work* → B; states of *an entity* → J.)
10. Content **scores items on two axes** (价值×成本, 紧急×重要, 风险矩阵)
    → **K Quadrant matrix**.
11. Content is a **before/after or current-vs-target comparison** (As-Is/To-Be, 人工 vs AI)
    → **L As-Is → To-Be**.
12. Content needs to **prove behavior with real data/tables/SQL** → **C Data-example panel**.

(C moved last on purpose: it is the universal supporting motif — prefer a structural
primary from 1–11, then add C for evidence.)

If two match, the earlier number wins as primary; the other becomes a supporting motif.

## Supporting-motif pairings (for density)
- E Gantt (primary) + C mini-table of KPIs, or + B chevron of scope expansion.
- F Architecture (primary) + legend/KPI chips + C tag chips inside modules.
- A/G flow (primary) + C example table + KPI chips ("N 人并行 / 0 冲突").
- Comparison-heavy page → **L As-Is/To-Be** as primary + C table of quantified gains.
- H sequence (primary) + C payload example (一条真实报文/SQL) + KPI chips (P99 XX ms).
- I topology (primary) + legend + "×XX 节点" chips + C port/protocol mini-table.
- J state machine (primary) + C state×permission mini-table, or + G swimlane of who fires
  each event.
- K quadrant (primary) + right takeaway column + E mini-gantt of the "do-first" quadrant.

## Per-page planning checklist
For each page, before building, write down:
- primary motif + supporting motif(s)
- the vertical budget (title band / main figure ≥70% / logo box)
- the anti-blank filler you'll use if a column comes up short
- which text is a placeholder (keep `XX` / `XX%` verbatim unless the user gave numbers)

## Multi-page decks
Vary motifs across pages so the deck doesn't look repetitive, but keep tokens identical.
A common 3-page rhythm: (1) problem/solution as D+A or D+G, (2) results/roadmap as C-table +
E-gantt, (3) architecture as F.
