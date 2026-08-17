# -*- coding: utf-8 -*-
"""
example_slide.py — a complete motif-F (layered architecture) slide built with pptx_kit.
Serves as a few-shot anchor: it shows how theme tokens + motif skeleton combine, and it
passes qa_check.py. Run:  python example_slide.py  ->  example.pptx

From inside the skill folder:
    python assets/example_slide.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from pptx_kit import Deck
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(__file__)
TOKENS = os.path.join(HERE, "tokens.json")

d = Deck(TOKENS)
s = d.add_slide()
SW, SH, M = d.SW, d.SH, d.M
d.title(s, "AI FOR 研发工作台：用「智能引擎」驱动数据交付新范式")
d.box(s, SW-2.55, 0.36, 2.55, 0.30,
      [[("产品架构 ", d.sz("caption"), d.c("muted"), False),
        ("V1.0", d.sz("caption"), d.c("accent"), True),
        ("  ·  数据研发平台", d.sz("caption"), d.c("muted"), False)]],
      fill="neutral", line=None)

lane_x = M; lane_w = 0.40; main_x = lane_x+lane_w+0.10
gov_w = 0.52; gov_gap = 0.08
gov2_x = (SW-M)-gov_w; gov1_x = gov2_x-gov_gap-gov_w
main_r = gov1_x-0.14; main_w = main_r-main_x

L1y,L1h = 0.90,0.56
L2y,L2h = L1y+L1h+0.13, 2.42
L3y,L3h = L2y+L2h+0.13, 1.66
L4y,L4h = L3y+L3h+0.13, 0.60
LEGy,LEGh = L4y+L4h+0.10, 0.30

def band(y,h,fill,label): d.layer_band(s, main_x, main_w, lane_x, lane_w, y, h, fill, label)

# L1 输入层
band(L1y,L1h,"nested","输入层")
in_items=[("自然语言需求","业务人员直述"),("结构化文档","需求规格/模板"),("系统推荐问题","场景化引导")]
iw=(main_w-0.40-2*0.14)/3
for i,(a,b) in enumerate(in_items):
    x=main_x+0.20+i*(iw+0.14)
    d.box(s,x,L1y+0.09,iw,L1h-0.18,[[(a,12,d.c("title"),True),("  "+b,11,d.c("muted"),False)]],
          fill="white",line="border_gray")
d.varrow(s,main_x+main_w/2-0.08,L1y+L1h+0.01,0.16,0.11)

# L2 工作流层
band(L2y,L2h,"container","工作流层")
d.harrow(s,main_x+1.2,L2y+0.075,main_w-2.4,0.10,color="chevron_mid",left=True)
d.text(s,main_x+main_w/2-1.2,L2y+0.045,2.4,0.16,[[("验证不通过 · 回流修正",11,d.c("title"),True)]],align=PP_ALIGN.CENTER)
agents=[("A","需求分析","需求 Agent",["理解意图","拆解子任务","关联元数据"]),
        ("B","方案设计","方案 Agent",["生成逻辑模型","映射字段","引用知识库规范"]),
        ("C","开发","开发 Agent",["生成 SQL/ETL 脚本","代码审查","性能优化建议"]),
        ("D","测试验证","测试 Agent",["生成测试数据","执行测试用例","结果比对"])]
na=4; aw=0.26; ip=0.18
acw=(main_w-2*ip-(na-1)*aw)/na; ach=L2h-0.44; ay=L2y+0.30
for i,(lt,tt,tag,abil) in enumerate(agents):
    ax=main_x+ip+i*(acw+aw)
    d.box(s,ax,ay,acw,ach,None,fill="white",line="border_blue",shadow=True)
    d.circle(s,ax+0.12,ay+0.10,0.36,"accent",lt,"white",13)
    d.text(s,ax+0.54,ay+0.08,acw-0.60,0.24,[[(tt,12.5,d.c("title"),True)]],anchor=MSO_ANCHOR.MIDDLE)
    d.text(s,ax+0.54,ay+0.33,acw-0.60,0.20,[[(tag,11,d.c("accent"),True)]])
    d.box(s,ax+0.10,ay+0.58,acw-0.20,ach-0.68,[[("· "+a,11,d.c("text"),False)] for a in abil],
          fill="nested",line=None,align=PP_ALIGN.LEFT,ml=0.09,ls=1.12,sa=2)
    if i<na-1: d.harrow(s,ax+acw+0.02,ay+ach/2-0.10,aw-0.04,0.20)
d.varrow(s,main_x+main_w/2-0.08,L2y+L2h+0.01,0.16,0.11)

# L3 配置层
band(L3y,L3h,"nested","配置层")
cfg=[("积","Skill 池管理","「搭积木式」研发","标准化方案封装为 Skill,原子 Skill 跨租户复用",["原子Skill","组合编排"]),
     ("知","知识库","元数据+规范文档 双轮驱动","让 Agent 懂业务、懂规范",["元数据","血缘"]),
     ("具","工具调用配置","按主题域收敛调用范围","作用域隔离,精准打击",["主题域","作用域"])]
mw=(main_w-2*ip-2*0.20)/3; mh=L3h-0.34; my=L3y+0.17
for i,(g,t,st,ds,tags) in enumerate(cfg):
    mx=main_x+ip+i*(mw+0.20)
    d.box(s,mx,my,mw,mh,None,fill="white",line="border_gray",shadow=True)
    d.circle(s,mx+0.11,my+0.10,0.34,"title",g,"white",11)
    d.text(s,mx+0.52,my+0.08,mw-0.60,0.22,[[(t,12,d.c("title"),True)]],anchor=MSO_ANCHOR.MIDDLE)
    d.text(s,mx+0.52,my+0.32,mw-0.60,0.20,[[(st,11,d.c("accent"),True)]])
    d.text(s,mx+0.13,my+0.58,mw-0.26,0.46,[[(ds,11,d.c("text"),False)]],ls=1.1)
    tgx=mx+0.13; tgy=my+mh-0.34
    for tg in tags:
        tw=0.26+0.17*len(tg)
        d.box(s,tgx,tgy,tw,0.26,[[(tg,11,d.c("accent"),True)]],fill="nested",line=None)
        tgx+=tw+0.09
    # 右侧量化胶囊(防空白兜底:辅助层)
    for k,stat in enumerate(["沉淀 XX+","复用 XX%"]):
        d.box(s,mx+mw-1.22,my+0.50+k*0.36,1.08,0.28,[[(stat,11,d.c("title"),True)]],
              fill="nested",line=None)
d.varrow(s,main_x+main_w/2-0.08,L3y+L3h+0.01,0.16,0.11)

# governance vertical bars
gv_y=L2y; gv_h=L3y+L3h-L2y
for gx,(g,t) in zip((gov1_x,gov2_x),[("户","租户用户管理"),("监","研发状态监控")]):
    d.box(s,gx,gv_y,gov_w,gv_h,None,fill="neutral",line="border_gray")
    d.circle(s,gx+(gov_w-0.34)/2,gv_y+0.10,0.34,"title",g,"white",11)
    d.vlabel(s,gx+0.055,gv_y+0.54,gov_w-0.11,gv_h-0.66,t,"neutral","title",11.5,line=None)
d.text(s,gov1_x-0.28,gv_y-0.24,2*gov_w+gov_gap+0.56,0.20,[[("平台支撑·保障",11,d.c("muted"),True)]],align=PP_ALIGN.CENTER)

# L4 输出层
band(L4y,L4h,"neutral","输出层")
outs=["RS/TS 文档","数据模型","SQL 脚本","ETL 任务","测试报告"]
ow=(main_w-2*ip-4*0.12)/5
for i,o in enumerate(outs):
    ox=main_x+ip+i*(ow+0.12)
    d.box(s,ox,L4y+0.11,ow,L4h-0.22,[[(o,11.5,d.c("title"),True)]],fill="white",line="border_gray")

# legend + KPI
d.text(s,main_x,LEGy,0.55,LEGh,[[("图例",11,d.c("muted"),True)]],anchor=MSO_ANCHOR.MIDDLE)
lx=main_x+0.55
for fl,tt in [("container","工作流层"),("nested","输入/配置层"),("neutral","输出/平台")]:
    d.box(s,lx,LEGy+0.075,0.22,0.15,None,fill=fl,line="border_gray")
    d.text(s,lx+0.27,LEGy,1.00,LEGh,[[(tt,11,d.c("muted"),False)]],anchor=MSO_ANCHOR.MIDDLE); lx+=1.42
d.text(s,lx,LEGy,1.85,LEGh,[[("↕ 调用 · ↩ 回流",11,d.c("muted"),False)]],anchor=MSO_ANCHOR.MIDDLE)
kx=lx+1.9
for a,b in [("4 Agent","协同"),("3 能力","支撑"),("5 制品","交付")]:
    d.box(s,kx,LEGy,1.38,LEGh,[[(a+" ",11.5,d.c("accent"),True),(b,11,d.c("text"),False)]],fill="neutral",line=None)
    kx+=1.48

d.logo(s)
out=os.path.join(HERE,"example.pptx") if os.path.basename(os.getcwd())!="assets" else "example.pptx"
d.save("example.pptx")
print("saved example.pptx")
