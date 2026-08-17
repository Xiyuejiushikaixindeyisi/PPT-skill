# ai-ppt-engineering

A portable skill for generating **high-density, engineering-style PPTX decks** whose main body
is a complex diagram — Gantt charts, layered product-architecture diagrams, swimlanes, chevron
lifecycles, nested pipelines, data-example panels — on a **swappable brand theme**, with
density enforced by measurable QA gates (not vibes).

## What's inside
```
ai-ppt-engineering/
├── SKILL.md                 # entry: tier routing + 6-step workflow + hard rules
├── STANDALONE_PROMPT.md     # paste-anywhere spec for any LLM (T3 / model-agnostic)
├── README.md
├── references/
│   ├── brand-tokens.md      # palette / font / type scale / layout / density (human twin of tokens.json)
│   ├── dept-style-rules.md  # department style evidence: rules vs noise, draft corrections
│   ├── layout-library.md    # five canonical page layouts (cover/TOC/section/content/end)
│   ├── motif-library.md     # motifs A–L: trigger / required parts / skeleton / good-vs-degraded
│   ├── density-rules.md     # hard indicators + coordinate budget + anti-blank priority
│   └── content-mapping.md   # content → motif decision tree
├── scripts/
│   ├── pptx_kit.py          # theme-driven python-pptx toolkit (box/gantt/swimlane/layer_band…)
│   ├── dept_pages.py        # page scaffolds: cover / toc / section / content / end
│   ├── qa_check.py          # overflow + geometry + density + structure + fontsize(≥11pt) + shape(no rounded) gates
│   └── render_preview.py    # pptx → pdf → jpg for review
└── assets/
    ├── tokens.json          # DEFAULT theme (source of truth for scripts)
    ├── tokens-emerald.json  # example alternate theme (copy me to re-brand)
    ├── example_slide.py     # complete motif-F slide; few-shot anchor; passes qa_check
    └── logo-default.png     # default brand logo (bottom-right)
```

## Three usage tiers (portable across models)
- **T1 full** (sandboxed code, e.g. Claude Code): run the toolkit + QA loop directly.
- **T2 script-out** (model writes code the user runs, e.g. GPT/Gemini): emit one self-contained
  Python file + `qa_check.py`, tell the user how to run them.
- **T3 text-only**: hand the user `STANDALONE_PROMPT.md` filled with the chosen theme + motifs.

## Quickstart (T1)
```bash
pip install python-pptx Pillow numpy
python assets/example_slide.py                                   # -> example.pptx
python scripts/render_preview.py example.pptx --outdir preview   # needs LibreOffice + poppler
python scripts/qa_check.py example.pptx --tokens assets/tokens.json --render-dir preview
```
Iterate your own `build.py` (import `pptx_kit.Deck`) until `qa_check.py` prints `RESULT: PASS`.

## Re-branding (swappable theme)
1. Copy `assets/tokens.json` → `assets/tokens-<brand>.json`.
2. Change `theme`, `palette`, `font`, and `layout.logo.file`; drop the new logo into `assets/`.
3. Point scripts at it: `--tokens assets/tokens-<brand>.json` (T1/T2), or paste the values into
   `STANDALONE_PROMPT.md` §2 (T3).
Motifs, layout math, and QA gates never change when re-branding.

## Dependencies
- Required: `python-pptx`, `Pillow`, `numpy`.
- Optional (for render + density gate): LibreOffice (`soffice`) and poppler (`pdftoppm`).
  Without them, the overflow / geometry / structure gates still run.
