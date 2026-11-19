import pypdfium2 as pdfium
import os

rpl_dir = r"c:\A_main_code\all-my-projek\RPL"
output_path = os.path.join(rpl_dir, "BUNDEL_LENGKAP_10_DELIVERABLES_PROJEK_RPL_SIPESAT.pdf")
master_laporan = os.path.join(rpl_dir, "LAPORAN_LENGKAP_PROJEK_RPL_SIPESAT_KELOMPOK_7.pdf")

# Files in sequence matching the 10 deliverables
ordered_files = [
    ("1. SRS (Software Requirements Specification - Versi Revisi 2 Role)", os.path.join(rpl_dir, "tugas-2-srs-wiegers.pdf")),
    ("2. USECASE DIAGRAM & Matriks RBAC (Versi Revisi)", os.path.join(rpl_dir, "tugas-3-usecase.pdf")),
    ("3. CLASS DIAGRAM & Analisis Database (Versi Revisi)", os.path.join(rpl_dir, "tugas-6-class-object.pdf")),
    ("4 & 5. ACTIVITY & SEQUENCE DIAGRAM Pola BCE (Versi Revisi)", os.path.join(rpl_dir, "tugas-4-activity-sequence.pdf")),
    ("6. DEPLOYMENT DIAGRAM 3-Tier (Versi Revisi)", os.path.join(rpl_dir, "tugas-7-deployment-diagram.pdf")),
    ("7. HASIL FIGMA & UI/UX Style Guide", os.path.join(rpl_dir, "tugas-7-figma-uiux.pdf")),
    ("8. FILE PENGUJIAN SOFTWARE Black Box Testing 35 Test Cases (Versi Revisi)", os.path.join(rpl_dir, "tugas-11-pengujian-black-box.pdf")),
    ("9. HASIL SISTEMNYA Konstruksi & Implementasi (Versi Revisi)", os.path.join(rpl_dir, "tugas-10-konstruksi-implementasi.pdf")),
]

merged_pdf = pdfium.PdfDocument.new()

# Step 1: Prepend Cover Page & Matriks Table from LAPORAN_LENGKAP (pages 0 and 1)
if os.path.exists(master_laporan):
    master_doc = pdfium.PdfDocument(master_laporan)
    # Import page 0 (Cover) and page 1 (Matriks Deliverables)
    merged_pdf.import_pages(master_doc, [0, 1])
    print("[OK] Prepend Cover Resmi UNINDRA & Matriks 10 Deliverables (2 pages)")

# Step 2: Append all revised documents in strict order
total_pages = len(merged_pdf)
for label, fpath in ordered_files:
    if os.path.exists(fpath):
        src_pdf = pdfium.PdfDocument(fpath)
        page_count = len(src_pdf)
        merged_pdf.import_pages(src_pdf)
        total_pages += page_count
        print(f"[OK] Added {label} ({page_count} pages)")
    else:
        print(f"[WARN] File not found: {fpath}")

merged_pdf.save(output_path)
print(f"\n[SUCCESS 100%] Generated Master Bundel PDF: {output_path}")
print(f"Total Pages: {len(merged_pdf)}")
print(f"File Size: {os.path.getsize(output_path) / 1024:.2f} KB")
