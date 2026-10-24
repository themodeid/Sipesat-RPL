import os
import xml.etree.ElementTree as ET

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

def generate_tugas_2_drawio():
    # Read the clean Use Case tab from tugas-3-usecase.drawio
    tugas3_path = os.path.join(RPL_DIR, "tugas-3-usecase.drawio")
    with open(tugas3_path, "r", encoding="utf-8") as f:
        tugas3_content = f.read()
    
    # Extract the diagram content of tugas-3
    tugas3_tree = ET.fromstring(tugas3_content)
    usecase_diagram = tugas3_tree.find(".//diagram")
    usecase_inner = ET.tostring(usecase_diagram, encoding="utf-8").decode("utf-8")
    # Change diagram name for SRS
    usecase_inner = usecase_inner.replace('name="Use Case Diagram (SIPESAT)"', 'name="Lampiran B - Use Case Diagram SRS (SIPESAT)"')

    # Construct Tab 1: System Context & Product Perspective Diagram
    tab1_xml = """    <diagram id="srs-context-sipesat" name="Bab 2.1 - Diagram Konteks &amp; Arsitektur Produk">
        <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="hdr_banner" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:16px;'&gt;DIAGRAM KONTEKS &amp;amp; PERSPEKTIF ARSITEKTUR PRODUK (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Dokumen Spesifikasi Kebutuhan Perangkat Lunak (SRS) Standar IEEE Std 830-1998 / Karl Wiegers — Kelompok 7 (RPL_XD)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1280" x="60" y="20" as="geometry" />
                </mxCell>

                <!-- LAYER 1: EXTERNAL ACTORS -->
                <mxCell id="box_siswa" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b style='font-size:13px;'&gt;Aktor: Siswa (Aktor Pemohon)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;Perangkat: Smartphone / Web Browser&lt;br&gt;Protokol: HTTPS (Port 443)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="75" width="360" x="150" y="115" as="geometry" />
                </mxCell>

                <mxCell id="box_tu" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b style='font-size:13px;'&gt;Aktor: Petugas TU &amp;amp; Kepala Sekolah&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;Perangkat: Desktop PC / Web Browser&lt;br&gt;Protokol: HTTPS (Port 443)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="75" width="360" x="890" y="115" as="geometry" />
                </mxCell>

                <!-- LAYER 2: CORE SYSTEM APPLICATION BOUNDARY -->
                <mxCell id="box_app_boundary" parent="1" style="swimlane;startSize=32;fontStyle=1;align=center;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Boundary: Aplikasi Web SIPESAT (Next.js 15 App Router)" vertex="1">
                    <mxGeometry height="340" width="1100" x="150" y="240" as="geometry" />
                </mxCell>

                <!-- Sub-Modules Inside App Boundary -->
                <mxCell id="mod_presentation" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b&gt;Presentation Layer (UI/UX)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;• Tailwind CSS &amp;amp; Pure Neutral Zinc&lt;br&gt;• React Server &amp;amp; Client Components&lt;br&gt;• Real-time Status Stepper Tracker&lt;/span&gt;" vertex="1">
                    <mxGeometry height="95" width="480" x="180" y="295" as="geometry" />
                </mxCell>

                <mxCell id="mod_security" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b&gt;Security &amp;amp; Session Management&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;• JSON Web Token (JWT) HttpOnly Cookie&lt;br&gt;• Role-Based Access Control (RBAC Guard)&lt;br&gt;• Password Hash Verification (Argon2 / Bcrypt)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="95" width="480" x="730" y="295" as="geometry" />
                </mxCell>

                <mxCell id="mod_business" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b&gt;Business Logic &amp;amp; Validation Engine&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;• Runtime Schema Validation (Zod Boundary Guard)&lt;br&gt;• Service Layer Persuratan &amp;amp; Disposisi TU&lt;br&gt;• State Transition Machine Validator&lt;/span&gt;" vertex="1">
                    <mxGeometry height="95" width="480" x="180" y="445" as="geometry" />
                </mxCell>

                <mxCell id="mod_document" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b&gt;Document &amp;amp; QR Engine&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;• PDFKit Official Letterhead Compiler&lt;br&gt;• Dynamic QR Code TTE Hash Generator&lt;br&gt;• Public Document Verification Resolver&lt;/span&gt;" vertex="1">
                    <mxGeometry height="95" width="480" x="730" y="445" as="geometry" />
                </mxCell>

                <!-- LAYER 3: DATA PERSISTENCE & STORAGE -->
                <mxCell id="box_db" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b style='font-size:13px;'&gt;Basis Data: PostgreSQL 16&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;• Master Data Siswa, Akun, &amp;amp; Jenis Surat&lt;br&gt;• tb_pengajuan_surat &amp;amp; Riwayat Status&lt;br&gt;• Immutable Audit Log &amp;amp; Disposisi TU&lt;/span&gt;" vertex="1">
                    <mxGeometry height="110" width="440" x="200" y="640" as="geometry" />
                </mxCell>

                <mxCell id="box_storage" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;align=center;verticalAlign=middle;" value="&lt;b style='font-size:13px;'&gt;Media Penyimpanan: Object Storage&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;• Berkas Syarat Unggahan Siswa (PDF ≤ 2MB)&lt;br&gt;• Arsip File Surat Resmi Ber-QR Code&lt;br&gt;• Template Naskah Kop Sekolah&lt;/span&gt;" vertex="1">
                    <mxGeometry height="110" width="440" x="750" y="640" as="geometry" />
                </mxCell>

                <!-- CONNECTORS -->
                <!-- Siswa -> Presentation -->
                <mxCell id="edge_s_pres" edge="1" parent="1" source="box_siswa" style="html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=11;exitX=0.5;exitY=1;entryX=0.35;entryY=0;endArrow=block;endFill=1;" target="mod_presentation" value="1. Form Input &amp;amp; Upload Syarat">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- TU -> Security -->
                <mxCell id="edge_tu_sec" edge="1" parent="1" source="box_tu" style="html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=11;exitX=0.5;exitY=1;entryX=0.65;entryY=0;endArrow=block;endFill=1;" target="mod_security" value="1. Login &amp;amp; Otorisasi Pengesahan">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Presentation -> Business -->
                <mxCell id="edge_pres_bus" edge="1" parent="1" source="mod_presentation" style="html=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=block;endFill=1;" target="mod_business" value="2. Server Actions Payload">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Security -> Business -->
                <mxCell id="edge_sec_bus" edge="1" parent="1" source="mod_security" style="html=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11;exitX=0.25;exitY=1;entryX=0.75;entryY=0;endArrow=block;endFill=1;" target="mod_business" value="2. RBAC Session Context">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Business -> Document -->
                <mxCell id="edge_bus_doc" edge="1" parent="1" source="mod_business" style="html=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11;exitX=1;exitY=0.5;entryX=0;entryY=0.5;endArrow=block;endFill=1;" target="mod_document" value="3. Trigger Render Surat Sah">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Business -> DB -->
                <mxCell id="edge_bus_db" edge="1" parent="1" source="mod_business" style="html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=11;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=block;endFill=1;" target="box_db" value="4. Prisma ORM / Transaksi ACID">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Document -> Storage -->
                <mxCell id="edge_doc_str" edge="1" parent="1" source="mod_document" style="html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=11;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=block;endFill=1;" target="box_storage" value="4. Simpan PDF &amp;amp; Baca Lampiran">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

            </root>
        </mxGraphModel>
    </diagram>"""

    # Assemble complete 2-Tab file
    full_xml = f"""<mxfile host="65bd71144e">
{tab1_xml}
{usecase_inner}
</mxfile>"""

    out_file = os.path.join(RPL_DIR, "tugas-2-srs-wiegers.drawio")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(full_xml)
    print(f"[OK] Generated {out_file} (2 Tabs: Arsitektur Konteks Bab 2.1 & Use Case SRS Lampiran B)")

if __name__ == "__main__":
    generate_tugas_2_drawio()
