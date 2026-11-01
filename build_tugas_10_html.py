import markdown

md_path = r"c:\A_main_code\all-my-projek\RPL\tugas-10-konstruksi-implementasi.md"
html_path = r"c:\A_main_code\all-my-projek\RPL\tugas-10-konstruksi-implementasi.html"

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

body_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite'])

full_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>TUGAS 10 RPL - KONSTRUKSI & IMPLEMENTASI PL - KELOMPOK 7</title>
  <style>
    @page {{
      size: A4;
      margin: 4cm 3cm 3cm 4cm;
    }}
    body {{
      font-family: 'Times New Roman', Times, serif;
      font-size: 11pt;
      line-height: 1.5;
      color: #111;
      margin: 0 auto;
      padding: 3cm 2cm;
      max-width: 210mm;
      background: #fff;
    }}
    @media print {{
      body {{ padding: 0; max-width: 100%; }}
      .no-print {{ display: none !important; }}
      h1, h2 {{ page-break-after: avoid; }}
      pre, table {{ page-break-inside: avoid; }}
    }}
    .print-bar {{
      position: fixed;
      top: 12px;
      right: 16px;
      z-index: 1000;
      background: #1e293b;
      color: #fff;
      padding: 8px 16px;
      border-radius: 6px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      display: flex;
      gap: 10px;
      align-items: center;
      font-family: system-ui, -apple-system, sans-serif;
      font-size: 13px;
    }}
    .print-btn {{
      background: #2563eb;
      color: white;
      border: none;
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 500;
    }}
    .print-btn:hover {{ background: #1d4ed8; }}
    h1 {{ font-size: 14pt; text-align: center; text-transform: uppercase; margin-bottom: 8px; }}
    h2 {{ font-size: 12pt; margin-top: 24px; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; }}
    h3 {{ font-size: 11.5pt; margin-top: 18px; }}
    h4 {{ font-size: 11pt; margin-top: 12px; font-style: italic; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      font-size: 10pt;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 8px 10px;
      text-align: left;
    }}
    th {{
      background: #1e293b;
      color: #fff;
      font-weight: bold;
    }}
    tr:nth-child(even) {{ background: #f8fafc; }}
    pre {{
      background: #0f172a;
      color: #f8fafc;
      padding: 12px 14px;
      border-radius: 6px;
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 9.5pt;
      overflow-x: auto;
      line-height: 1.4;
      border: 1px solid #334155;
    }}
    code {{
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 10pt;
      background: #f1f5f9;
      padding: 2px 4px;
      border-radius: 4px;
      color: #0f172a;
    }}
    pre code {{
      background: none;
      padding: 0;
      color: inherit;
    }}
    blockquote {{
      border-left: 4px solid #2563eb;
      margin: 12px 0;
      padding: 8px 16px;
      background: #eff6ff;
      color: #1e3a8a;
    }}
  </style>
</head>
<body>
  <div class="print-bar no-print">
    <span>Tugas 10 RPL - Kelompok 7 UNINDRA</span>
    <button class="print-btn" onclick="window.print()">🖨️ Cetak / Simpan PDF</button>
  </div>
  {body_html}
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("SUCCESS: HTML created at", html_path)
