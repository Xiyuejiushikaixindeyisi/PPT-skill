# Brand Tokens (theme-swappable)

This file is the human-readable twin of `assets/tokens.json`. **The JSON is the source of
truth for scripts; this file is for the model to reason about.**

## How theming works
Everything visual is a token. A new brand = a new `tokens.json` with the same keys and
different values. Motifs, layout math, and QA gate *logic* never change (thresholds are read
from the JSON). Default theme: **`dept-flat-blue`** — extracted from 9 real department decks
(237 slides). Alternates in `assets/`: `tokens-huawei-yunshan.json`, `tokens-emerald.json`.
部门风格的完整依据（明确规范 vs 个人习惯噪声、对提取草稿的修正）见 `dept-style-rules.md`。

## Palette (default: dept-flat-blue)
| Token | Hex | Role |
|---|---|---|
| `title` | #000000 | 标题与正文文字（部门标题就是黑色，不是深蓝） |
| `accent` | #2683C6 | 主视觉蓝：强调填充、当前阶段、连线、序号块 |
| `container` | #D7EAFE | 一级浅底容器 / 泳道体 / 甘特已完成 |
| `nested` | #DEEBF7 | 容器内子块、侧注、标签 |
| `chevron_mid` | #558ED5 | chevron 中段、架构中间层 |
| `neutral` | #F2F2F2 | 中性块、未开始甘特条、章节页子卡片 |
| `text` | #000000 | 正文 |
| `muted` | #808080 | 小标签、图注、图例 |
| `border_gray` | #BFBFBF | 卡片细描边 |
| `gray_line` | #D9D9D9 | 分隔线、表格线 |
| `border_blue` | #2683C6 | 一级容器描边（少用，多数容器无描边） |
| `red` | #C00000 | 风险、今日线、关键数字加粗、**红描边圈注框(7/9 文件惯例)** |
| `blue_text` | #0070C0 | 行内蓝色术语强调 |
| `amber` | #FFC000 | 里程碑、待决策高亮 |
| `pink` | #FFC8D3 | 第二分组色（与蓝并列时才用） |
| `white` | #FFFFFF | 背景、深色底上的文字 |

白色主导页面。蓝色是唯一的第一分组色；需要更多分组色按 pink → amber 顺序取，不引入新色。
扁平：无阴影、无渐变、直角矩形（部门实测：阴影 3.2%、渐变 3.3%、圆角仅 12%）。

## Font
- Family: **微软雅黑**（整套一个字族；latin+ea+cs 三槽同写，中西文一致）。
- Fallbacks: Microsoft YaHei, Noto Sans CJK SC, PingFang SC, SimHei.

## Type scale (pt) — hard floor **8pt**（tokens `min`，QA FONTSIZE 门禁自动读取）
| Token | pt | Use |
|---|---|---|
| `cover_title` | 40 | 封面主标题（加粗） |
| `section_title` | 28 | 节标题页 |
| `title` | 20 | 内容页页标题（加粗、黑、左对齐；实测 62% 用 20pt） |
| `container_title` | 14 | 一级容器 / 泳道 / 层标题 |
| `node_title` / `body` | 12 | 节点标题、正文 |
| `secondary` | 10 | 次级说明 |
| `caption` | 9 | 图注、页脚、来源 |
| `min` | 8 | 硬性下限——放不下就缩措辞/换行/加宽，绝不缩号 |

## Layout
16:9（13.333×7.5in），边距 0.51in。页标题带 `(5.5%, 1.7%) 89%×8%`（`d.title()` 自动使用）。
Logo 右下角 1.5in 宽、锁纵横比、0.24in 内边距，任何图形避开该区域。

## Density gates（tokens `density`，qa_check 自动读取）
形状数 ≥ 20/页（中位数 30，冲着 30+ 做）· 主图 ≥ 70% 页高 · 无 >1.2in 空白 ·
溢出 ≤3% · 字号 ≥ 8pt。
