import os

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"
ASSETS_DIR = os.path.join(RPL_DIR, "assets")

# 1. DRAW.IO XML GENERATOR FOR DEPLOYMENT DIAGRAM
drawio_xml = """<mxfile host="65bd71144e">
    <diagram id="deployment-diagram-sipesat" name="1. Deployment Diagram (SIPESAT)">
        <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1100" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="hdr_deploy" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;DEPLOYMENT DIAGRAM — SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Pemodelan UML 2.5 Arsitektur Fisik, Node Perangkat, Container Docker &amp;amp; Protokol Jaringan — Kelompok 7 (RPL_XD UNINDRA 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1600" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- ==================== TIER 1: CLIENT TIER ==================== -->
                <mxCell id="node_client" parent="1" style="shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=12;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;align=center;verticalAlign=top;spacingTop=16;" value="&amp;laquo;device&amp;raquo;&#xa;Client Tier: User Device&#xa;(PC / Laptop / Smartphone)" vertex="1">
                    <mxGeometry x="50" y="110" width="340" height="480" as="geometry" />
                </mxCell>

                <mxCell id="env_browser" parent="node_client" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=top;spacingTop=8;fontStyle=1;" value="&amp;laquo;executionEnvironment&amp;raquo;&#xa;Web Browser Engine&#xa;(Chrome, Edge, Firefox, Safari)" vertex="1">
                    <mxGeometry x="25" y="80" width="290" height="370" as="geometry" />
                </mxCell>

                <mxCell id="art_client_app" parent="env_browser" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=10;spacingTop=6;" value="&amp;laquo;artifact&amp;raquo;&#xa;&lt;b&gt;SIPESAT Web Application&lt;/b&gt;&#xa;&lt;hr/&gt;&#xa;• HTML5 / CSS3 / React Virtual DOM&#xa;• Tailwind CSS Compiled Assets&#xa;• Client-Side JWT Auth Storage&#xa;• File Upload Input (Limit 2MB)&#xa;• Interactive Tracking Stepper UI&#xa;• PDF Viewer &amp;amp; Download Component" vertex="1">
                    <mxGeometry x="15" y="70" width="260" height="150" as="geometry" />
                </mxCell>

                <mxCell id="art_actors" parent="env_browser" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=10;spacingTop=6;" value="&amp;laquo;actor / role&amp;raquo;&#xa;&lt;b&gt;Pengguna Sistem Terautentikasi&lt;/b&gt;&#xa;&lt;hr/&gt;&#xa;1. &lt;b&gt;Siswa&lt;/b&gt;: Form Permohonan &amp;amp; Lacak&#xa;2. &lt;b&gt;Petugas TU / Admin&lt;/b&gt;: Verifikasi, Disposisi, Terbitkan No. Surat, Cetak PDF" vertex="1">
                    <mxGeometry x="15" y="240" width="260" height="110" as="geometry" />
                </mxCell>


                <!-- ==================== TIER 2: APPLICATION & WEB SERVER TIER ==================== -->
                <mxCell id="node_app_server" parent="1" style="shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=12;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;align=center;verticalAlign=top;spacingTop=16;" value="&amp;laquo;device / executionServer&amp;raquo;&#xa;Application &amp;amp; Service Tier&#xa;(Node.js Server Host / Local / VPS)" vertex="1">
                    <mxGeometry x="500" y="110" width="560" height="740" as="geometry" />
                </mxCell>

                <!-- SUB-NODE: FRONTEND RUNTIME (NEXT.JS) -->
                <mxCell id="env_nextjs" parent="node_app_server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=top;spacingTop=8;fontStyle=1;" value="&amp;laquo;executionEnvironment&amp;raquo;&#xa;Next.js 14 Web Server (Port 3000)&#xa;[Node.js Runtime v18/v20]" vertex="1">
                    <mxGeometry x="25" y="80" width="510" height="230" as="geometry" />
                </mxCell>

                <mxCell id="art_next_build" parent="env_nextjs" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=10;spacingTop=6;" value="&amp;laquo;artifact&amp;raquo;&#xa;&lt;b&gt;fe/.next (Compiled Next.js App Router)&lt;/b&gt;&#xa;&lt;hr/&gt;&#xa;• Server Components &amp;amp; Client Components SSR&#xa;• API Client Proxy Helper (/lib/api.ts)&#xa;• Authentication State &amp;amp; Protected Route Guard&#xa;• Toast Notifications &amp;amp; Modals Handler" vertex="1">
                    <mxGeometry x="20" y="70" width="470" height="135" as="geometry" />
                </mxCell>

                <!-- SUB-NODE: BACKEND RUNTIME (EXPRESS REST API) -->
                <mxCell id="env_express" parent="node_app_server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=top;spacingTop=8;fontStyle=1;" value="&amp;laquo;executionEnvironment&amp;raquo;&#xa;Express REST API Server (Port 5000)&#xa;[TypeScript / Node.js Engine]" vertex="1">
                    <mxGeometry x="25" y="340" width="510" height="370" as="geometry" />
                </mxCell>

                <mxCell id="cmp_auth_guard" parent="env_express" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=8;spacingTop=4;fontSize=10;" value="&amp;laquo;component&amp;raquo;&#xa;&lt;b&gt;AuthMiddleware (JWT)&lt;/b&gt;&#xa;• Token Verification &amp;amp; Extraction&#xa;• RBAC Role Guard (Siswa vs TU)" vertex="1">
                    <mxGeometry x="20" y="65" width="225" height="85" as="geometry" />
                </mxCell>

                <mxCell id="cmp_pengajuan_ctrl" parent="env_express" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=8;spacingTop=4;fontSize=10;" value="&amp;laquo;component&amp;raquo;&#xa;&lt;b&gt;PengajuanController&lt;/b&gt;&#xa;• CRUD Permohonan Surat&#xa;• Validasi Kelayakan Berkas Siswa&#xa;• State Transition &amp;amp; Audit Log" vertex="1">
                    <mxGeometry x="265" y="65" width="225" height="85" as="geometry" />
                </mxCell>

                <mxCell id="cmp_surat_ctrl" parent="env_express" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=8;spacingTop=4;fontSize=10;" value="&amp;laquo;component&amp;raquo;&#xa;&lt;b&gt;SuratGeneratorController&lt;/b&gt;&#xa;• Auto-Numbering Engine (Format Resmi)&#xa;• QR Code Digital Signature Generator&#xa;• PDFKit Binary Document Streamer" vertex="1">
                    <mxGeometry x="20" y="165" width="225" height="90" as="geometry" />
                </mxCell>

                <mxCell id="cmp_multer" parent="env_express" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=8;spacingTop=4;fontSize=10;" value="&amp;laquo;component&amp;raquo;&#xa;&lt;b&gt;Multer FileHandler&lt;/b&gt;&#xa;• Whitelist MIME Type (PDF, JPG, PNG)&#xa;• Max File Size Filter (2 MB)&#xa;• UUID File Renaming &amp;amp; Path Binding" vertex="1">
                    <mxGeometry x="265" y="165" width="225" height="90" as="geometry" />
                </mxCell>

                <mxCell id="cmp_prisma" parent="env_express" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=8;spacingTop=4;fontSize=10;" value="&amp;laquo;component&amp;raquo;&#xa;&lt;b&gt;Prisma Client ORM Engine&lt;/b&gt;&#xa;• Connection Pooling &amp;amp; Transaction Manager&#xa;• Type-Safe SQL Query Builder&#xa;• Foreign Key Constraint Integrity" vertex="1">
                    <mxGeometry x="20" y="270" width="470" height="80" as="geometry" />
                </mxCell>


                <!-- ==================== TIER 3: DATA & STORAGE TIER (DOCKER) ==================== -->
                <mxCell id="node_db_server" parent="1" style="shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=12;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;align=center;verticalAlign=top;spacingTop=16;" value="&amp;laquo;device / virtualizationHost&amp;raquo;&#xa;Data &amp;amp; Storage Tier&#xa;(Docker Container &amp;amp; File System)" vertex="1">
                    <mxGeometry x="1170" y="110" width="480" height="740" as="geometry" />
                </mxCell>

                <mxCell id="env_docker" parent="node_db_server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=top;spacingTop=8;fontStyle=1;" value="&amp;laquo;executionEnvironment&amp;raquo;&#xa;Docker Engine 24+ Runtime&#xa;[Bridge Network: sipesat-network]" vertex="1">
                    <mxGeometry x="25" y="80" width="430" height="400" as="geometry" />
                </mxCell>

                <mxCell id="cnt_postgres" parent="env_docker" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=center;verticalAlign=top;spacingTop=8;fontStyle=1;" value="&amp;laquo;container&amp;raquo;&#xa;sipesat-postgres-1&#xa;[PostgreSQL 16 Alpine - Port 5432]" vertex="1">
                    <mxGeometry x="20" y="70" width="390" height="305" as="geometry" />
                </mxCell>

                <mxCell id="art_db_tables" parent="cnt_postgres" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#000000;strokeWidth=1;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=10;spacingTop=6;" value="&amp;laquo;database schema&amp;raquo;&#xa;&lt;b&gt;Database: sipesat_db (3NF Relational)&lt;/b&gt;&#xa;&lt;hr/&gt;&#xa;• &lt;b&gt;tb_user&lt;/b&gt; (id_user, username, password_hash, role)&#xa;• &lt;b&gt;tb_siswa&lt;/b&gt; (id_siswa, nisn, nama_lengkap, kelas, jurusan)&#xa;• &lt;b&gt;tb_petugas&lt;/b&gt; (id_petugas, nip, nama, bagian)&#xa;• &lt;b&gt;tb_jenis_surat&lt;/b&gt; (id_jenis, kode, nama, syarat_berkas)&#xa;• &lt;b&gt;tb_pengajuan_surat&lt;/b&gt; (id_pengajuan, nomor_surat, status)&#xa;• &lt;b&gt;tb_berkas_persyaratan&lt;/b&gt; (id_berkas, path_file, ukuran)&#xa;• &lt;b&gt;tb_riwayat_status&lt;/b&gt; (id_log, id_pengajuan, status, tgl)" vertex="1">
                    <mxGeometry x="15" y="65" width="360" height="225" as="geometry" />
                </mxCell>

                <!-- PERSISTENT STORAGE ARTIFACTS -->
                <mxCell id="vol_db" parent="node_db_server" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=10;spacingTop=6;" value="&amp;laquo;file system volume&amp;raquo;&#xa;&lt;b&gt;Persistent Database Storage&lt;/b&gt;&#xa;&lt;hr/&gt;&#xa;• Named Volume: &lt;b&gt;sipesat_postgres_data&lt;/b&gt;&#xa;• Mount Path: /var/lib/postgresql/data&#xa;• Backup Snapshot &amp;amp; WAL Logs Engine" vertex="1">
                    <mxGeometry x="25" y="500" width="430" height="100" as="geometry" />
                </mxCell>

                <mxCell id="vol_uploads" parent="node_db_server" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;align=left;verticalAlign=top;spacingLeft=10;spacingTop=6;" value="&amp;laquo;file system volume&amp;raquo;&#xa;&lt;b&gt;Local Uploads Storage&lt;/b&gt;&#xa;&lt;hr/&gt;&#xa;• Path: &lt;b&gt;be/uploads/&lt;/b&gt;&#xa;• Berkas Syarat Siswa (PDF, JPG, PNG &amp;le; 2MB)&#xa;• Hasil Generate Dokumen PDF Surat Resmi" vertex="1">
                    <mxGeometry x="25" y="620" width="430" height="100" as="geometry" />
                </mxCell>


                <!-- ==================== COMMUNICATION LINKS & PROTOCOLS ==================== -->
                <!-- LINK 1: BROWSER TO NEXT.JS (HTTP/HTTPS) -->
                <mxCell id="link_browser_next" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;endArrow=open;endFill=1;" edge="1" source="node_client" target="env_nextjs">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="440" y="240" />
                            <mxPoint x="440" y="240" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="lbl_link1" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=#ffffff;fontColor=#000000;fontSize=10;fontStyle=1;" value="&amp;laquo;protocol&amp;raquo;&lt;br/&gt;HTTP / HTTPS (Port 3000)&lt;br/&gt;HTML / CSS / JS Chunks" vertex="1">
                    <mxGeometry x="385" y="195" width="130" height="40" as="geometry" />
                </mxCell>

                <!-- LINK 2: BROWSER DIRECT / NEXT API TO EXPRESS (REST API JSON) -->
                <mxCell id="link_browser_express" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;endArrow=open;endFill=1;" edge="1" source="node_client" target="env_express">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="440" y="480" />
                            <mxPoint x="440" y="480" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="lbl_link2" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=#ffffff;fontColor=#000000;fontSize=10;fontStyle=1;" value="&amp;laquo;protocol&amp;raquo;&lt;br/&gt;REST API JSON (Port 5000)&lt;br/&gt;Bearer JWT / Multipart Form" vertex="1">
                    <mxGeometry x="385" y="445" width="130" height="40" as="geometry" />
                </mxCell>

                <!-- LINK 3: NEXT.JS SERVER TO EXPRESS API -->
                <mxCell id="link_next_express" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;endArrow=open;endFill=1;dashed=1;" edge="1" source="env_nextjs" target="env_express">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="750" y="325" />
                            <mxPoint x="750" y="325" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="lbl_link3" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=#ffffff;fontColor=#000000;fontSize=9;fontStyle=2;" value="Internal Fetch / SSR Proxy (HTTP JSON)" vertex="1">
                    <mxGeometry x="660" y="318" width="180" height="20" as="geometry" />
                </mxCell>

                <!-- LINK 4: EXPRESS API TO POSTGRESQL DOCKER -->
                <mxCell id="link_express_db" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;endArrow=open;endFill=1;" edge="1" source="cmp_prisma" target="cnt_postgres">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1110" y="650" />
                            <mxPoint x="1110" y="350" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="lbl_link4" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=#ffffff;fontColor=#000000;fontSize=10;fontStyle=1;" value="&amp;laquo;protocol&amp;raquo;&lt;br/&gt;TCP/IP Connection Pool&lt;br/&gt;Port 5432 / PostgreSQL Driver" vertex="1">
                    <mxGeometry x="1055" y="445" width="145" height="40" as="geometry" />
                </mxCell>

                <!-- LINK 5: EXPRESS MULTER TO UPLOADS STORAGE -->
                <mxCell id="link_express_uploads" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;endArrow=open;endFill=1;dashed=1;" edge="1" source="cmp_multer" target="vol_uploads">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1090" y="550" />
                            <mxPoint x="1090" y="670" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="lbl_link5" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=#ffffff;fontColor=#000000;fontSize=9;fontStyle=2;" value="File System I/O Write" vertex="1">
                    <mxGeometry x="1065" y="605" width="105" height="20" as="geometry" />
                </mxCell>

                <!-- LINK 6: POSTGRES CONTAINER TO DATA VOLUME -->
                <mxCell id="link_pg_volume" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;endArrow=open;endFill=1;dashed=1;" edge="1" source="cnt_postgres" target="vol_db">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1400" y="490" />
                            <mxPoint x="1400" y="490" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="lbl_link6" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=#ffffff;fontColor=#000000;fontSize=9;fontStyle=2;" value="Docker Volume Bind Mount" vertex="1">
                    <mxGeometry x="1335" y="475" width="130" height="20" as="geometry" />
                </mxCell>

            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""

# Write Draw.io file
drawio_path = os.path.join(RPL_DIR, "tugas-7-deployment-diagram.drawio")
with open(drawio_path, "w", encoding="utf-8") as f:
    f.write(drawio_xml)
print(f"Generated: {drawio_path}")
