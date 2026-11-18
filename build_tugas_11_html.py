import markdown

md_path = r"c:\A_main_code\all-my-projek\RPL\tugas-11-pengujian-black-box.md"
html_path = r"c:\A_main_code\all-my-projek\RPL\tugas-11-pengujian-black-box.html"

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

body_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite'])

full_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>TUGAS 11 RPL - PENGUJIAN PERANGKAT LUNAK (BLACK BOX TESTING) - KELOMPOK 7</title>
  <style>
    @page {{
      size: A4;
      margin: 3.5cm 2.5cm 2.5cm 3.5cm;
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
      table {{ page-break-inside: auto; }}
      tr {{ page-break-inside: avoid; page-break-after: auto; }}
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
      background: #db2777;
      color: white;
      border: none;
      padding: 6px 14px;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 600;
      transition: background 0.2s;
    }}
    .print-btn:hover {{ background: #be185d; }}
    h1 {{ font-size: 14pt; text-align: center; text-transform: uppercase; margin-bottom: 6px; }}
    h2 {{ font-size: 12pt; margin-top: 24px; border-bottom: 2px solid #f472b6; padding-bottom: 4px; }}
    h3 {{ font-size: 11.5pt; margin-top: 18px; }}
    h4 {{ font-size: 11pt; margin-top: 12px; font-style: italic; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      font-size: 9.5pt;
    }}
    th, td {{
      border: 1px solid #94a3b8;
      padding: 7px 9px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: #f472b6 !important;
      color: #000000 !important;
      font-weight: bold;
      text-align: center;
      vertical-align: middle;
    }}
    tr:nth-child(even) {{ background: #fdf2f8; }}
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
      background: #fce7f3;
      padding: 2px 4px;
      border-radius: 4px;
      color: #831843;
    }}
    blockquote {{
      border-left: 4px solid #f472b6;
      margin: 14px 0;
      padding: 8px 16px;
      background: #fdf2f8;
      color: #475569;
    }}
    hr {{
      border: none;
      border-top: 1px solid #cbd5e1;
      margin: 24px 0;
    }}
    .badge-valid {{
      display: inline-block;
      font-weight: bold;
      color: #065f46;
      background: #d1fae5;
      padding: 2px 8px;
      border-radius: 4px;
    }}
  </style>
</head>
<body>
  <div class="print-bar no-print">
    <span>Tugas 11 RPL (Pengujian Black Box) - SIPESAT Kelompok 7</span>
    <button class="print-btn" onclick="window.print()">Cetak / Simpan PDF</button>
  </div>
  {body_html}
</body>
</html>
"""

# Replace Valid with formatted badge or standard valid
full_html = full_html.replace("<td>Valid</td>", "<td><strong>Valid</strong></td>")
full_html = full_html.replace("<td>Sesuai harapan</td>", "<td>Sesuai harapan</td>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("HTML generated successfully at:", html_path)
