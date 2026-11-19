import pypdfium2 as pdfium
import os

rpl_dir = r"c:\A_main_code\all-my-projek\RPL"
output_path = os.path.join(rpl_dir, "BUNDEL_LENGKAP_10_DELIVERABLES_PROJEK_RPL_SIPESAT.pdf")

# Files in sequence matching the 10 deliverables
ordered_files = [
    ("1. SRS (Software Requirements Specification)", os.path.join(rpl_dir, "tugas-2-srs-wiegers.pdf")),
    ("2. USECASE DIAGRAM & Matriks RBAC", os.path.join(rpl_dir, "tugas-3-usecase.pdf")),
    ("3. CLASS DIAGRAM & Analisis Database", os.path.join(rpl_dir, "tugas-6-class-object.pdf")),
    ("4 & 5. ACTIVITY & SEQUENCE DIAGRAM (Pola BCE)", os.path.join(rpl_dir, "tugas-4-activity-sequence.pdf")),
    ("6. DEPLOYMENT DIAGRAM", os.path.join(rpl_dir, "tugas-7-deployment-diagram.pdf")),
    ("7. HASIL FIGMA & UI/UX Style Guide", os.path.join(rpl_dir, "tugas-7-figma-uiux.pdf")),
    ("8. FILE PENGUJIAN SOFTWARE (Black Box Testing)", os.path.join(rpl_dir, "tugas-11-pengujian-black-box.pdf")),
    ("9. HASIL SISTEMNYA (Konstruksi & Implementasi)", os.path.join(rpl_dir, "tugas-10-konstruksi-implementasi.pdf")),
]

# We will create a new PDF combining all pages
merged_pdf = pdfium.PdfDocument.new()

total_pages = 0
for label, fpath in ordered_files:
    if os.path.exists(fpath):
        src_pdf = pdfium.PdfDocument(fpath)
        page_count = len(src_pdf)
        # Import all pages from src_pdf into merged_pdf
        merged_pdf.import_pages(src_pdf)
        total_pages += page_count
        print(f"[OK] Added {label} ({page_count} pages)")
    else:
        print(f"[WARN] File not found: {fpath}")

merged_pdf.save(output_path)
print(f"\n[SUCCESS 100%] Generated Master Bundel PDF: {output_path}")
print(f"Total Pages: {len(merged_pdf)}")
print(f"File Size: {os.path.getsize(output_path) / 1024:.2f} KB")
