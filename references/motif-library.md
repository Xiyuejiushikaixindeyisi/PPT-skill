# Motif Library (A–L)

Twelve reusable diagram archetypes. Each page uses **1 primary motif + up to 2 supporting
motifs** to hit density. Every motif is specified as four parts so a model copies structure
instead of improvising:

1. **Trigger** — content signature that selects this motif
2. **Required parts** — checklist; missing any part = non-compliant
3. **Coordinate skeleton** — relative-coordinate pseudocode mapping to `pptx_kit` calls
4. **Good vs degraded** — the degraded form is the failure to avoid

Colors below use token names from `brand-tokens.md`. `d` = a `Deck` instance.

**Shape rule (all motifs):** every text-bearing shape — boxes, containers, lane heads, table
cells, tag chips, KPI pills — is a **square-cornered rectangle**. No rounded rectangles
anywhere. `d.box` / `d.pill` already emit plain rectangles; the legacy `rad` argument is
ignored, so don't pass it. Circles (`d.circle`) stay circles for index/icon glyphs, diamonds
(`d.diamond`) stay diamonds for decisions/milestones, arrows and chevrons keep their shapes.

## Table of contents
- A. Horizontal nested swimlane flow
- B. Stage chevron + sub-process
- C. Data-example detail panel
- D. Vertical pipeline + nested sub-blocks + side notes
- E. Gantt / time plan
- F. Layered product-architecture diagram
- G. Swimlane collaboration diagram
- H. Sequence / interaction diagram
- I. Deployment / topology zones
- J. State machine
- K. Quadrant / priority matrix
- L. As-Is → To-Be comparison

---

## A. Horizontal nested swimlane flow
**Trigger** — Agent/multi-skill collaboration with iteration; an end-to-end run with loops.
**Required parts** — left vertical scene label; a main chain of nodes with arrows; ≥1 tinted
Skill *container* nesting sub-steps; a loop/return arrow between containers; a right-side
convergence (judge/conclusion).
**Skeleton**
```
d.vlabel(s, ML, y, 0.4, H, "运行", "title","white")
# main chain
for i,node in enumerate(chain): d.box(...); d.harrow(... between ...)
# nested container
d.box(s, cx, cy, cw, ch, fill="container", line="border_blue")   # container
for sub in steps: d.box(..., fill="white")                        # sub-steps inside
d.harrow(..., color="chevron_mid", left=True)                     # return/loop
```
**Good vs degraded** — Good: containers visibly wrap sub-steps and a return arrow shows
iteration. Degraded: a single straight row of equal boxes with no nesting and no loop.

---

## B. Stage chevron + sub-process
**Trigger** — a lifecycle with ordered phases; "设计→生成→管理→应用" style.
**Required parts** — top row of interlocking chevrons (gradient title→accent→chevron_mid→
container); under each chevron, white sub-step boxes with arrows; optional branch merging in;
left vertical lane label.
**Skeleton**
```
cx = x0
for i,ph in enumerate(phases):
    d.chevron(s, cx, y, cw, 0.42, ph, fill=grad[i], tc=tc[i]); cx += cw - overlap
for each phase: place sub-boxes below, connect with d.harrow / d.varrow
```
**Good vs degraded** — Good: chevrons interlock and each has real sub-steps beneath.
Degraded: four flat rectangles with one word each and nothing below them.

---

## C. Data-example detail panel
**Trigger** — prove what a step does with real data: tables, SQL, input→output.
**Required parts** — stacked titled panels; a mini-table with dark header + zebra rows
(use `d.mini_table`); optional SQL/code snippet block; an input→output arrow.
Highest information density of all motifs.
**Skeleton**
```
d.text(s, x, y, w, .2, [[("获取受影响维表清单", d.sz("caption"), d.c("muted"), True)]])
d.mini_table(s, x, y+.23, w, ["列A","列B","列C"], rows, col_ws)
d.varrow(...); # 生成SQL
d.box(s, ..., fill="neutral", paras=[[("select ...", 7.2, d.c("text"), False)]])
```
**Good vs degraded** — Good: an actual small table/SQL a reader can inspect.
Degraded: a paragraph describing the data instead of showing it.

---

## D. Vertical pipeline + nested sub-blocks + side notes
**Trigger** — one function/skill's top-to-bottom processing pipeline with sub-classification.
**Required parts** — vertical main flow of step headers; each step nests parallel sub-blocks;
down-arrows between steps; optional side annotation pulling out details.
**Skeleton**
```
def step(y, num, head): d.box(s, ix, y, iw, .27, [[(num+" ", .., "accent",1),(head,..,"title",1)]],
                              fill="container", align=LEFT)
step(y1,"①","知识库筑基"); two sub-boxes fill="nested"; d.varrow(...)
step(y2,"②","语义精准消费"); one wide sub-box; d.varrow(...)
step(y3,"③","边界控制"); two sub-boxes
```
**Good vs degraded** — Good: headers + nested sub-blocks + arrows read as a pipeline.
Degraded: a bulleted list with no boxes or arrows.

---

## E. Gantt / time plan
**Trigger** — tasks with start/end and status; a roadmap or rollout schedule.
**Required parts** — top time axis (week/month/quarter ticks); vertical grid lines; left task
column (optionally grouped, group header in `title`); status-colored bars
(done=`container`, active=`accent`, not_started=`neutral`); diamond milestones (`milestone`);
dashed today line (`today_line`); a legend. Missing ticks/legend = degraded.
**Skeleton**
```
# axis
for i,q in enumerate(quarters): d.text(gx+task_w+i*gw, gy0, gw, .18, [[(q,7.2,"muted",1)]], align=CENTER)
# grid lines: thin RECTANGLE fills, color border_gray
# rows
for r,(name,start,len_,status) in enumerate(tasks):
    d.text(gx, ry, task_w, rh, [[(name, 7.5,"title",1)]])
    d.box(gx+task_w+start*gw, ry+.05, len_*gw, rh-.09, None, fill=status_fill)
d.diamond(gx+task_w+ms*gw, my, .15, "milestone")
d.dashline(today_x, y_top, y_bot, "today_line")
# legend at bottom: small swatches + labels
```
**Good vs degraded** — Good: bars align to a real dated axis with legend + milestone + today.
Degraded: colored bars with no time axis (just a colored list).

---

## F. Layered product-architecture diagram
**Trigger** — a platform/product structure: 应用层/能力层/引擎层/数据层/基础设施层.
**Required parts** — top-to-bottom full-width layer bands (alternating container/nested/neutral);
left vertical layer names (`d.layer_band`); inside each band, equal-width module boxes on a
grid; optional vertical governance bars on the right spanning multiple layers; up/down arrows
for call relationships between layers.
**Skeleton**
```
for (y,h,fill,label) in layers:
    d.layer_band(s, main_x, main_w, lane_x, lane_w, y, h, fill, label)
    # place equal-width module boxes inside band
    d.varrow(main_x+main_w/2, y+h, .16, .11)   # between layers
# governance: d.box(gx, span_y, gov_w, span_h, fill="neutral"); d.vlabel(...)
```
**Good vs degraded** — Good: full-width bands + gridded modules + cross-layer arrows +
vertical governance. Degraded: a few stacked boxes without bands or alignment.

---

## G. Swimlane collaboration diagram
**Trigger** — multi-role/system hand-offs, approval flows, rework loops.
**Required parts** — horizontal (or vertical) lanes, one per role/system, lane head in `title`;
nodes placed in lanes; cross-lane arrows for hand-offs; diamond for decisions; a back arrow
for rework/return.
**Skeleton**
```
for i,lane in enumerate(lanes):
    d.box(s, x, yy, head_w, lane_h, [[(lane,7.6,"white",1)]], fill="title")   # lane head
    d.box(s, x+head_w, yy, body_w, lane_h, None, fill=[container/neutral][i%2]) # lane body
# nodes staggered across lanes; connect with d.varrow across rows
d.varrow(..., color="chevron_mid", up=True)   # status return / rework
```
**Good vs degraded** — Good: nodes sit in distinct lanes and arrows cross lanes to show
hand-offs. Degraded: one row of boxes with no lanes.

---

## H. Sequence / interaction diagram
**Trigger** — timed call/return between systems or agents: "前端→网关→服务→DB" 接口时序,
LLM tool-call 往返, 审批消息往返.
**Required parts** — top row of participant heads (`fill="title"`, white text); a dashed
lifeline under each head (`d.dashline`, `border_gray`); numbered message arrows between
lifelines (`d.harrow`, request=`accent`, return=`chevron_mid` + `left=True`); a short label
above each arrow; narrow activation bars (`d.box`, `fill="container"`, w≈0.10) on the
lifeline while a participant is working; optional loop/alt frame as a thin-bordered
container box with a corner pill.
**Skeleton**
```
for i,pt in enumerate(parts): d.box(s, x0+i*gap, y0, pw, .34, [[(pt,11.5,"white",1)]], fill="title")
for i in range(n): d.dashline(s, cx(i), y0+.36, y_bot, "border_gray")
for k,(a,b,txt,ret) in enumerate(msgs):
    d.box(s, min(cx(a),cx(b)), my-.06, .10, .30, None, fill="container", line=None)  # activation
    d.harrow(s, ..., color=("chevron_mid" if ret else "accent"), left=ret)
    d.text(s, mid_x, my-.20, mw, .19, [[(f"{k+1}. {txt}",11,"text",0)]], align=CENTER)
# loop frame: d.box(fill=None-ish "nested", line="border_blue"); corner d.pill("循环", "nested","accent")
```
**Good vs degraded** — Good: lifelines + numbered ordered arrows + activation bars read as
time flowing downward. Degraded: boxes connected left-to-right with no lifelines or order.

---

## I. Deployment / topology zones
**Trigger** — where things run and how they connect: 网络分区(DMZ/内网), 云上/云下,
集群与节点, 数据链路拓扑.
**Required parts** — 2–4 zone containers (`fill` alternating `container`/`nested`/`neutral`,
`line="border_blue"` for the primary zone) each with a title bar or `d.vlabel`; node boxes
on a grid inside each zone (white, `border_gray`), optionally with a `d.circle` glyph;
cross-zone links (`d.harrow`/`d.varrow`, protocol/port pill on the link, e.g. "HTTPS 443");
a legend row mapping zone colors; replica counts as chips ("×XX 节点").
**Skeleton**
```
for (zx,zy,zw,zh,fill,name) in zones:
    d.box(s, zx, zy, zw, zh, None, fill=fill, line="border_blue")
    d.box(s, zx, zy, zw, .30, [[(name,11.5,"white",1)]], fill="title")
    # grid of node boxes inside; chips "×XX" bottom-right of zone
d.harrow(s, ...); d.pill(s, link_mid, "HTTPS 443", "nested", "accent")
# legend at bottom (swatch + label), same pattern as motif E
```
**Good vs degraded** — Good: zones visibly contain nodes and labeled links cross zone
borders. Degraded: floating boxes with anonymous lines and no zones.

---

## J. State machine
**Trigger** — one entity's status lifecycle with events/guards: 工单/订单/任务状态流转,
草稿→评审→发布→归档, 含驳回回环.
**Required parts** — an initial marker (`d.circle`, `fill="title"`); state boxes (white,
`border_blue`, state name + 1 short line of entry action); transition arrows labeled with
the triggering event (pill on the arrow, `nested` fill, `accent` text); ≥1 backward arrow
(`chevron_mid`, reject/rework); a terminal state (`fill="container"`); optional `d.diamond`
for a guard split. Lay states on a grid (2 rows max), not a circle.
**Skeleton**
```
d.circle(s, x0, cy, .22, "title", "", "white", 11)          # initial
for i,(name,act) in enumerate(states):
    d.box(s, sx(i), sy(i), stw, .52, [[(name,12,"title",1)],[(act,11,"muted",0)]], line="border_blue")
    d.harrow(s, ...); d.pill(s, ..., event, "nested", "accent")
d.harrow(s, ..., color="chevron_mid", left=True)             # 驳回/返工
d.box(s, xe, ye, stw, .52, [[("归档",12,"title",1)]], fill="container")
```
**Good vs degraded** — Good: every arrow carries its event and at least one loop shows
rework. Degraded: a plain forward chain identical to motif B with no events.

---

## K. Quadrant / priority matrix
**Trigger** — items scored on two axes: 价值×成本, 紧急×重要, 风险矩阵, 能力成熟度分布.
**Required parts** — a full-width plot square; center cross axes (two thin `d.box` rules,
`border_gray`) with axis-end labels (`muted`, e.g. "价值 高→"); four quadrant tints
(`nested`/`neutral` alternating) each with a corner title (`container_title`, `title`
color); item chips placed by score (`d.pill` or small box, `accent` border for highlighted
items); a side takeaway column (which quadrant to act on first, KPI chips).
**Skeleton**
```
d.box(s, qx, qy, qw/2, qh/2, None, fill="nested", line=None)      # ×4 tints
d.box(s, qx, qy+qh/2-.008, qw, .016, None, fill="border_gray")     # axes
d.box(s, qx+qw/2-.008, qy, .016, qh, None, fill="border_gray")
d.text(s, corner, [[("高价值·低成本",13,"title",1)]])               # ×4 titles
for (name,px,py,hot) in items:
    d.pill(s, qx+px*qw, qy+(1-py)*qh, w, .28, name, "white", "text")
# right column: 结论/优先级 chips (anti-blank auxiliary layer)
```
**Good vs degraded** — Good: items positioned meaningfully inside labeled quadrants plus a
takeaway. Degraded: a 2×2 table of bullet lists (that's a table, not a matrix).

---

## L. As-Is → To-Be comparison
**Trigger** — before/after, 现状痛点 vs 目标方案, 人工流程 vs AI 流程, 新旧架构对比.
**Required parts** — two side-by-side containers: left "As-Is" (`fill="neutral"`, gray
`d.vlabel` or header) and right "To-Be" (`fill="container"`, `border_blue`); mirrored inner
structure (same row count, so rows align and differences pop); a large center transform
arrow (`d.harrow`, `accent`) stacked with 2–3 改造要点 pills; a bottom quantified-gain strip
(mini_table or KPI chips: 时长 XX→XX, 人力 XX→XX). Mirror rows 1:1 — never freeform prose.
**Skeleton**
```
d.box(s, lx, y, colw, H, None, fill="neutral");  d.box(s, rx, y, colw, H, None, fill="container", line="border_blue")
d.box(s, lx, y, colw, .32, [[("As-Is 现状",12,"white",1)]], fill="muted")
d.box(s, rx, y, colw, .32, [[("To-Be 目标",12,"white",1)]], fill="title")
for i,(old,new) in enumerate(rows):   # mirrored rows
    d.box(s, lx+.14, ry(i), colw-.28, rh, [[(old,11,"text",0)]], fill="white")
    d.box(s, rx+.14, ry(i), colw-.28, rh, [[(new,11,"title",0)]], fill="white", line="border_blue")
d.harrow(s, mid_x, mid_y, aw, .30)                       # transform arrow
for k,pt in enumerate(points): d.pill(s, mid_x, mid_y+.4+k*.34, aw, .28, pt, "nested", "accent")
# bottom: mini_table 或 KPI chips "交付周期 XX天 → XX天"
```
**Good vs degraded** — Good: mirrored rows + labeled transform arrow + quantified gains.
Degraded: two unrelated bullet lists side by side.

---

## Filling leftover space (anti-blank)
After the primary motif, if a >1.2in blank remains, add supporting content in this priority:
1. expand the main figure (more annotations / sub-blocks / stretch rows to fill);
2. add an auxiliary layer: legend, status notes, KPI chips, risk/dependency side-notes;
3. add a mini-panel (motif C small table or input→output example);
4. only then allow a small blank (≤1.2in). Never fake fullness by enlarging fonts or gaps.
