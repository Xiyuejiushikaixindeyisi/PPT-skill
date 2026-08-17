# -*- coding: utf-8 -*-
"""
render_preview.py — turn a .pptx into per-slide JPGs for human/model review.

    python render_preview.py deck.pptx --outdir preview --dpi 135

Chain: soffice --convert-to pdf  ->  pdftoppm -jpeg. Both must be on PATH.
Falided rasterization is non-fatal; it just prints guidance.
"""
import sys, os, argparse, subprocess, glob

def which(cmd):
    return subprocess.call(["bash","-lc",f"command -v {cmd} >/dev/null 2>&1"]) == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--outdir", default="preview")
    ap.add_argument("--dpi", type=int, default=135)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    soffice = "soffice" if which("soffice") else ("libreoffice" if which("libreoffice") else None)
    if not soffice:
        print("No soffice/libreoffice on PATH. Install LibreOffice to render previews.")
        sys.exit(2)
    if not which("pdftoppm"):
        print("No pdftoppm on PATH. Install poppler-utils to render previews.")
        sys.exit(2)

    subprocess.run([soffice,"--headless","--convert-to","pdf","--outdir",args.outdir,args.pptx],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = os.path.join(args.outdir, os.path.splitext(os.path.basename(args.pptx))[0]+".pdf")
    if not os.path.exists(pdf):
        print("PDF conversion failed."); sys.exit(2)
    subprocess.run(["pdftoppm","-jpeg","-r",str(args.dpi),pdf,os.path.join(args.outdir,"slide")],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    jpgs = sorted(glob.glob(os.path.join(args.outdir,"slide-*.jpg")))
    print(f"Rendered {len(jpgs)} slide(s) to {args.outdir}/")
    for j in jpgs: print("  ", j)

if __name__ == "__main__":
    main()
