---
name: ai-ppt-engineering
description: Generate high-density, engineering-style PowerPoint slides in the department's flat-blue style (微软雅黑, #2683C6 accent, square-cornered flat shapes) with complex flow diagrams (Gantt charts, layered architecture, swimlanes, chevron lifecycles, data-example panels, sequence diagrams, deployment topologies, state machines, quadrant matrices, as-is/to-be comparisons) and standard page layouts (封面 cover, 目录 TOC, 节标题 section header, 内容页 content, 末尾页 end page). Use whenever the user wants a .pptx / slides / deck / presentation / 汇报材料 in the department or company style, with process, architecture, roadmap, Gantt, swimlane, or workflow diagrams, OR wants slides that look full and dense rather than sparse bullet lists — even without naming a specific diagram type. Also use when a generated deck is too empty, needs re-theming/re-branding, or the user wants a reusable prompt/spec for other LLMs. Works across models, degrading gracefully from full script execution to a paste-anywhere text spec.
---

# AI-PPT Engineering (department flat-blue, high-density flow-diagram slides)

Build department-style, **engineering-dense** slides: flat, square-cornered, 微软雅黑,
white background, #2683C6 accent — whose content pages carry a complex diagram (Gantt,
layered architecture, swimlane, chevron lifecycle, nested pipeline, data-example panel,
sequence diagram, deployment topology, state machine, quadrant matrix, as-is→to-be) on a
**swappable theme**. Density is enforced by measurable gates, not vibes. Default theme
`dept-flat-blue` was extracted from 9 real department decks (237 slides) and hand-verified.

## Pick your execution tier FIRST
Detect the environment, then follow the matching tier. This is what makes the skill portable
across models.

- **T1 — full (sandboxed code execution available, e.g. Claude Code):** run the Python
  toolkit + QA loop directly. This is the default when you can run bash/python.
- **T2 — script-out (model can write code the user runs locally, e.g. GPT/Gemini chat):**
  emit ONE self-contained Python file (inline the parts of `pptx_kit.py` / `dept_pages.py`
  you use) plus the `qa_check.py` content, and tell the user how to run them.
- **T3 — text-only (no code path):** produce the standalone spec by reading
  `STANDALONE_PROMPT.md` and filling it with the chosen theme + motifs. That file is a
  paste-anywhere prompt that reproduces the style verbally.

## Six-step workflow (all tiers)
1. **Understand content** — restate the user's content and page count; identify the info
   type of each page. Keep placeholders like `XX` / `XX%` verbatim unless real numbers were
   given.
2. **Frame the deck** — map content onto the standard page sequence
   封面 → 目录 → [节标题 → 内容页×N] → 末尾页 (skip 目录/节标题 for ≤6-page decks), using
   `references/layout-library.md`. Scaffold these pages with `scripts/dept_pages.py`
   (cover / toc / section / content / end) instead of hand-placing coordinates.
3. **Route motifs** — for each content page, use `references/content-mapping.md` to choose
   1 primary + up to 2 supporting motifs. Briefly confirm with the user.
4. **Plan layout (density budget)** — using `references/density-rules.md`, reserve the title
   band, give the main figure ≥70% page height, lay a grid, and pre-list the anti-blank
   filler you'll use if a region is short.
5. **Build** — per tier above. Colors/fonts/sizes come only from the theme tokens; page
   frames from `dept_pages.py`; diagram structure from `references/motif-library.md`. Never
   hardcode brand values in slide code.
6. **QA loop** — run `scripts/qa_check.py` (overflow / geometry / density / structure /
   fontsize / shape). Fix every HARD flag, re-run, and only deliver when it prints
   `RESULT: PASS`. If you can't rasterize (no LibreOffice), still run the non-render gates
   and reason about density from the coordinate budget.

## Reference map (read on demand)
- `references/brand-tokens.md` — palette, font, type scale, layout, density thresholds
  (human-readable twin of `assets/tokens.json`). Read in steps 4–5 and when re-theming.
- `references/dept-style-rules.md` — the department style evidence base: authoritative
  rules vs personal-habit noise, corrections made to the auto-extracted draft, table/chart
  conventions. Read when styling decisions feel ambiguous or the user questions the style.
- `references/layout-library.md` — the five canonical page layouts with measured
  %-coordinates (cover / TOC / section / content title band / end page). Read in step 2.
- `references/motif-library.md` — motifs A–L, each with trigger / required parts /
  coordinate skeleton / good-vs-degraded. Read in steps 3 and 5.
- `references/density-rules.md` — hard indicators, coordinate budget, anti-blank priority.
  Read in steps 4 and 6.
- `references/content-mapping.md` — content→motif decision tree. Read in step 3.
- `assets/tokens.json` — machine-readable theme, default `dept-flat-blue` (source of truth
  for scripts). Alternates: `tokens-huawei-yunshan.json`, `tokens-emerald.json`.
- `assets/example_slide.py` — a complete motif-F architecture slide; few-shot anchor.
- `scripts/dept_pages.py` — page scaffolds for the five standard layouts.
- `STANDALONE_PROMPT.md` — the T3 paste-anywhere spec (also the model-agnostic deliverable).

## Theming (swappable)
The default theme is `dept-flat-blue`. To re-brand: copy `assets/tokens.json`, change
`theme`, palette, `font`, and `logo.file` (drop the new logo into `assets/`), then pass
`--tokens <new>.json` to the scripts (T1/T2) or paste the new values into the standalone
prompt (T3). Motifs, layout math, and QA gate logic are theme-independent — never edit them
to re-brand (thresholds themselves live in each theme's `density` block).

## T1 quickstart (commands)
```bash
# build (your slide script imports pptx_kit + dept_pages and a tokens file)
python your_build.py                       # writes deck.pptx
# render for review (optional; needs LibreOffice + poppler)
python scripts/render_preview.py deck.pptx --outdir preview
# verify — iterate until PASS
python scripts/qa_check.py deck.pptx --tokens assets/tokens.json --render-dir preview
```

## Hard rules (all tiers, dept-flat-blue defaults)
- 16:9, pure-white background, one font family (微软雅黑 across latin/ea/cs).
- Page title: 20pt bold **black**, left-aligned in the title band `(5.5%,1.7%) 89%×8%`.
  Result-style titles ("XX 通过 XX 实现 XX", 20+ chars is the norm), not noun phrases.
- Content-page frame furniture (from the real master, drawn by `dept_pages.frame()`):
  full-width gray rule under the title (y 9.8%, #BFBFBF 0.75pt), small blue corner icon
  top-left, "page N" 8pt gray bottom-left, logo bottom-right. Cover/section/end pages skip
  the rule and page number. Optionally a group-label chip under the title (9/9-deck habit).
- **Flat + square-cornered containers**: no shadows, no gradients; all cards/containers are
  plain rectangles. Sole exception: small tag chips ≤1.1×0.5in may be rounded — use
  `d.chip()` (QA SHAPE gate enforces exactly this split).
- Blue #2683C6 is the only first-group color; extra groups take pink → amber in that order.
  Navy #04194C is the second brand color (section-page panel, index dots). Red #C00000 is
  for risk / today-line / key numbers — and the **red-outline callout box** (the department's
  strongest emphasis habit: 7/9 decks) for circling the key region of a page. Inline
  emphasis: blue #0070C0 terms, red bold, amber #F4A100 bold, secondary gray #333333.
- Logo bottom-right, aspect-locked, never overlapped. Shapes stay flat and ungrouped
  (grpSp=0 in all 237 sampled slides) so humans can adjust them afterwards.
- **Font floor 8pt** (tokens `min`; QA FONTSIZE gate hard-fails smaller). Body stays 12pt;
  9–10pt only for captions and secondary notes. Fit text by shortening/wrapping/widening —
  never by shrinking below the floor.
- Every content page: main diagram ≥70% height, no blank >1.2in, ≥20 shapes (aim 30+,
  the department median), text fits.
- Tables: no zebra by default; header row light-blue #D7EAFE or bold-on-white; 0.5pt
  #D9D9D9 grid. Charts: bar/line, series accent→#558ED5→#808080, data labels always on.
- Keep `XX` placeholders unless the user provides real data.
- Deliver only after `qa_check.py` passes (or, in T2/T3, after the user can run it / the
  spec encodes the same self-check list).
