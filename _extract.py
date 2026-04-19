import sys, os, io
from pypdf import PdfReader

paths = [
    "הצעת מחיר - כלמוביל Energy.pdf",
    "כלמוביל Energy/מפרט אופטימייזרים.pdf",
    "כלמוביל Energy/מפרט ממיר סאנגרו רגיל.pdf",
    "כלמוביל Energy/מפרט ממיר סולאר אדג.pdf",
    "כלמוביל Energy/פאנל 600 תדיראן.pdf",
    "מחקר כללי על חברות סולאר ועוד דברים.pdf",
]

out_path = "_extracted.txt"
with io.open(out_path, "w", encoding="utf-8") as f:
    for p in paths:
        f.write("="*80 + "\n")
        f.write("FILE: " + p + "\n")
        f.write("="*80 + "\n")
        try:
            r = PdfReader(p)
            for i, page in enumerate(r.pages):
                text = page.extract_text() or ""
                f.write(f"--- PAGE {i+1} ---\n")
                f.write(text + "\n")
        except Exception as e:
            f.write("ERROR: " + str(e) + "\n")
        f.write("\n")
print("Done. Wrote", out_path)
