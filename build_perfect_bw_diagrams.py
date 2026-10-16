import os
import re
import xml.etree.ElementTree as ET

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

# =========================================================================
# 1. PERFECT ARCHITECTURAL REDESIGN FOR TUGAS 3 USE CASE DIAGRAM
# =========================================================================
def generate_tugas_3_xml():
    xml = """<mxfile host="65bd71144e">
    <diagram id="usecase-siswa-admin" name="3. Use Case Diagram (Siswa &amp; Petugas)">
        <mxGraphModel dx="1800" dy="1400" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1850" pageHeight="1300" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="header_banner" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;USE CASE DIAGRAM — SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Format Standar Bahan Ajar RPL UNINDRA (Pertemuan 04): 2 Role Eksklusif (Siswa &amp;amp; Petugas TU/Admin)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="60" width="1740" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- LEGEND BOX -->
                <mxCell id="legend_box" parent="1" style="rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=1.5;" value="&lt;b&gt;KETERANGAN SIMBOL (SLIDE 10 UNINDRA)&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;'&gt;&lt;table cellpadding='2' style='font-size:11px;width:100%;color:#000000;'&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;—— Asosiasi&lt;/b&gt;&lt;/td&gt;&lt;td&gt;Menghubungkan Aktor dengan Use Case&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;- - &amp;gt; &amp;lt;&amp;lt;include&amp;gt;&amp;gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;Use case yang wajib dijalankan&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;- - &amp;gt; &amp;lt;&amp;lt;extend&amp;gt;&amp;gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;Use case perluasan/kondisional&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;Role Siswa&lt;/b&gt;&lt;/td&gt;&lt;td&gt;Aktor Pemohon Surat Mandiri&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;Role Petugas&lt;/b&gt;&lt;/td&gt;&lt;td&gt;Aktor Pengelola, Verifikator &amp;amp; Approval&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" vertex="1">
                    <mxGeometry height="135" width="310" x="1480" y="95" as="geometry" />
                </mxCell>

                <!-- SYSTEM BOUNDARY -->
                <mxCell id="sys_boundary" parent="1" style="swimlane;startSize=34;fontStyle=1;align=center;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Boundary: Sistem Informasi Pengajuan Surat Siswa (SIPESAT)" vertex="1">
                    <mxGeometry height="1130" width="1220" x="230" y="95" as="geometry" />
                </mxCell>

                <!-- TOP SHARED USE CASES (LOGIN, LOGOUT, PROFIL) -->
                <mxCell id="uc_logout" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-04: Logout Sesi Sistem" vertex="1">
                    <mxGeometry height="55" width="200" x="170" y="50" as="geometry" />
                </mxCell>

                <mxCell id="uc_login" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-01: Login ke Sistem&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="220" x="490" y="50" as="geometry" />
                </mxCell>

                <mxCell id="uc_validate" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-01B: Validasi Kredensial &amp;amp; Token JWT&lt;/i&gt;" vertex="1">
                    <mxGeometry height="50" width="220" x="490" y="135" as="geometry" />
                </mxCell>

                <mxCell id="uc_profile" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-03: Kelola Profil &amp;amp; Ganti Password" vertex="1">
                    <mxGeometry height="55" width="220" x="830" y="50" as="geometry" />
                </mxCell>

                <mxCell id="inc_login_val" edge="1" parent="sys_boundary" source="uc_login" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_validate" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 1: SISWA MAIN USE CASES ==================== -->
                <mxCell id="uc_register" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-02: Registrasi Akun Siswa Mandiri" vertex="1">
                    <mxGeometry height="55" width="230" x="40" y="240" as="geometry" />
                </mxCell>

                <mxCell id="uc_catalog" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-05: Lihat Katalog &amp;amp; Syarat Jenis Surat" vertex="1">
                    <mxGeometry height="55" width="230" x="40" y="360" as="geometry" />
                </mxCell>

                <mxCell id="uc_apply" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-06: Mengajukan Permohonan Surat&lt;/b&gt;" vertex="1">
                    <mxGeometry height="60" width="230" x="40" y="490" as="geometry" />
                </mxCell>

                <mxCell id="uc_track" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-08: Melacak Status Surat (Real-time)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="60" width="230" x="40" y="640" as="geometry" />
                </mxCell>

                <mxCell id="uc_history" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-09: Melihat Riwayat Pengajuan Surat" vertex="1">
                    <mxGeometry height="55" width="230" x="40" y="780" as="geometry" />
                </mxCell>

                <mxCell id="uc_download" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-10: Unduh / Cetak Surat PDF &amp;amp; QR Code&lt;/b&gt;" vertex="1">
                    <mxGeometry height="60" width="230" x="40" y="910" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 2: SISWA INCLUDE & EXTEND ==================== -->
                <mxCell id="uc_upload" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-07: Unggah Berkas Syarat&#10;(PDF/Img &amp;le; 2MB)&lt;/i&gt;" vertex="1">
                    <mxGeometry height="60" width="220" x="330" y="490" as="geometry" />
                </mxCell>

                <mxCell id="inc_apply_up" edge="1" parent="sys_boundary" source="uc_apply" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_upload" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_revision" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-08A: Melihat Catatan Revisi /&#10;Penolakan Berkas&lt;/i&gt;" vertex="1">
                    <mxGeometry height="60" width="220" x="330" y="640" as="geometry" />
                </mxCell>

                <mxCell id="ext_rev_track" edge="1" parent="sys_boundary" source="uc_revision" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_track" value="&amp;lt;&amp;lt;extend&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 3: PETUGAS INCLUDE ==================== -->
                <mxCell id="uc_qr" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-14A: Terbitkan No. Surat &amp;amp;&#10;QR Code Resmi&lt;/i&gt;" vertex="1">
                    <mxGeometry height="60" width="220" x="670" y="570" as="geometry" />
                </mxCell>

                <mxCell id="inc_app_qr" edge="1" parent="sys_boundary" source="uc_approve" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_qr" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_note" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-15A: Input Alasan &amp;amp;&#10;Catatan Penolakan&lt;/i&gt;" vertex="1">
                    <mxGeometry height="60" width="220" x="670" y="700" as="geometry" />
                </mxCell>

                <mxCell id="inc_rej_note" edge="1" parent="sys_boundary" source="uc_reject" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_note" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 4: PETUGAS MAIN USE CASES ==================== -->
                <mxCell id="uc_dashboard" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-11: Akses Dashboard &amp;amp; Statistik Surat" vertex="1">
                    <mxGeometry height="55" width="230" x="950" y="240" as="geometry" />
                </mxCell>

                <mxCell id="uc_inbox" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-12: Memeriksa Antrean Pengajuan Masuk" vertex="1">
                    <mxGeometry height="55" width="230" x="950" y="350" as="geometry" />
                </mxCell>

                <mxCell id="uc_verify" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-13: Verifikasi Berkas &amp;amp; Dokumen Siswa&lt;/b&gt;" vertex="1">
                    <mxGeometry height="60" width="230" x="950" y="460" as="geometry" />
                </mxCell>

                <mxCell id="uc_approve" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-14: Menyetujui (Approve) Permohonan&lt;/b&gt;" vertex="1">
                    <mxGeometry height="60" width="230" x="950" y="570" as="geometry" />
                </mxCell>

                <mxCell id="uc_reject" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-15: Menolak / Minta Revisi Pengajuan&lt;/b&gt;" vertex="1">
                    <mxGeometry height="60" width="230" x="950" y="700" as="geometry" />
                </mxCell>

                <mxCell id="uc_master" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-16: Kelola Master Jenis Surat &amp;amp; Syarat" vertex="1">
                    <mxGeometry height="55" width="230" x="950" y="810" as="geometry" />
                </mxCell>

                <mxCell id="uc_users" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;" value="UC-17: Kelola Data Siswa &amp;amp; Akun Pengguna" vertex="1">
                    <mxGeometry height="55" width="230" x="950" y="910" as="geometry" />
                </mxCell>

                <mxCell id="uc_report" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-18: Ekspor Rekapitulasi Laporan (Excel/PDF)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="60" width="230" x="950" y="1010" as="geometry" />
                </mxCell>

                <!-- ==================== ACTORS ==================== -->
                <mxCell id="act_siswa" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.5;fontColor=#000000;fontStyle=1;fontSize=14;" value="&lt;b&gt;Siswa&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;color:#000000;'&gt;(Aktor Pemohon)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="160" width="90" x="70" y="550" as="geometry" />
                </mxCell>

                <mxCell id="act_petugas" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.5;fontColor=#000000;fontStyle=1;fontSize=14;" value="&lt;b&gt;Petugas&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;color:#000000;'&gt;(Verifikator &amp;amp; TU)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="160" width="90" x="1590" y="550" as="geometry" />
                </mxCell>

                <!-- ==================== CLEAN NON-CROSSING ASSOCIATIONS ==================== -->
                <!-- 1. SISWA CLEAN FAN TO COLUMN 1 (Straight lines, zero collisions) -->
                <mxCell id="edge_s_reg" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_register">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_s_cat" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_catalog">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_s_apply" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_apply">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_s_track" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_track">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_s_hist" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_history">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_s_down" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_download">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 2. SISWA TO TOP SHARED (Clean perimeter routing along exterior margin, zero shape intersection) -->
                <mxCell id="edge_s_logout" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_logout">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="115" y="540" />
                            <mxPoint x="115" y="172" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <mxCell id="edge_s_login" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0.25;entryY=0;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_login">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="90" y="540" />
                            <mxPoint x="90" y="70" />
                            <mxPoint x="775" y="70" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- 3. PETUGAS CLEAN FAN TO COLUMN 4 (Straight lines, zero collisions) -->
                <mxCell id="edge_p_dash" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_dashboard">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_p_inbox" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_inbox">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_p_ver" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_verify">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_p_app" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_approve">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_p_rej" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_reject">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_p_mast" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_master">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_p_usr" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_users">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="edge_p_rep" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_report">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 4. PETUGAS TO TOP SHARED (Clean perimeter routing along exterior margin, zero shape intersection) -->
                <mxCell id="edge_p_prof" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_profile">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1635" y="540" />
                            <mxPoint x="1635" y="172" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <mxCell id="edge_p_login" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0.75;entryY=0;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_login">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1660" y="540" />
                            <mxPoint x="1660" y="70" />
                            <mxPoint x="885" y="70" />
                        </Array>
                    </mxGeometry>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
    """
    return xml

def update_all_drawio():
    # 1. Update tugas-3-usecase.drawio with redesigned Tab 1 and clean Tab 2
    master_path = os.path.join(RPL_DIR, "use-case-siswa-admin.drawio")
    with open(master_path, "r", encoding="utf-8") as f:
        master_content = f.read()

    rbac_match = re.search(r'(<diagram id="rbac-matrix".*?</diagram>)', master_content, re.DOTALL)
    rbac_xml = rbac_match.group(1) if rbac_match else ""

    # Convert RBAC to B&W
    rbac_tree = ET.fromstring(rbac_xml)
    for cell in rbac_tree.iter("mxCell"):
        style = cell.get("style", "")
        cid = cell.get("id", "").lower()
        val = cell.get("value", "")
        if style:
            parts = style.split(";")
            new_p = []
            for p in parts:
                if not p.strip(): continue
                k = p.split("=")[0].strip()
                if k == "strokeColor": new_p.append("strokeColor=#000000")
                elif k == "fontColor": new_p.append("fontColor=#000000")
                elif k == "fillColor":
                    if "header" in cid or "th_" in cid:
                        new_p.append("fillColor=#f1f5f9")
                    elif re.search(r'row_[02468]', cid) or re.search(r'c[02468]_', cid):
                        new_p.append("fillColor=#f8fafc")
                    elif p.split("=")[1].strip() == "none":
                        new_p.append("fillColor=none")
                    else:
                        new_p.append("fillColor=#ffffff")
                else:
                    new_p.append(p)
            if not any(x.startswith("fontColor=") for x in new_p):
                new_p.append("fontColor=#000000")
            cell.set("style", ";".join(new_p))
        if val:
            cleaned = re.sub(r'color:\s*#[0-9a-fA-F]{3,6}', 'color:#000000', val)
            cleaned = re.sub(r'background(?:-color)?:\s*#[0-9a-fA-F]{3,6}', 'background-color:#ffffff', cleaned)
            cleaned = cleaned.replace("📋 ", "")
            cell.set("value", cleaned)

    clean_rbac_xml = ET.tostring(rbac_tree, encoding="utf-8").decode("utf-8")

    tugas_3_full = generate_tugas_3_xml().strip() + "\n" + clean_rbac_xml.strip() + "\n</mxfile>\n"
    t3_path = os.path.join(RPL_DIR, "tugas-3-usecase.drawio")
    with open(t3_path, "w", encoding="utf-8") as f:
        f.write(tugas_3_full)
    print(f"[OK] Re-engineered Tugas 3 Draw.io with zero collisions: {t3_path}")

    # 2. Convert Tugas 4 and Tugas 5 to ensure labelBackgroundColor=#ffffff on all edges and clean B&W
    for fn in ["tugas-4-activity-sequence.drawio", "tugas-5-state-machine.drawio"]:
        fp = os.path.join(RPL_DIR, fn)
        with open(fp, "r", encoding="utf-8") as f:
            c = f.read()
        tree = ET.fromstring(c)
        for cell in tree.iter("mxCell"):
            style = cell.get("style", "")
            cid = cell.get("id", "").lower()
            val = cell.get("value", "")
            is_edge = cell.get("edge") == "1"
            
            is_initial = "ellipse" in style and "doubleellipse" not in style.lower() and (cid.endswith("_init") or cid.endswith("_start") or cid in ["act_r1_sym", "sm_init", "auth_init", "s_start", "d1", "f1", "a1"])
            is_final = "doubleellipse" in style.lower() or cid.endswith("_final") or cid.endswith("_end") or cid in ["act_r5_sym", "sm_final", "auth_final", "s_end", "d13", "f14", "a14"]
            is_th = "header" in cid or "th" in cid
            is_alt = bool(re.search(r'row_[02468]', cid) or re.search(r'c[02468]_', cid))
            
            if style:
                parts = style.split(";")
                new_p = []
                for p in parts:
                    if not p.strip(): continue
                    kv = p.split("=", 1)
                    k = kv[0].strip()
                    v = kv[1].strip() if len(kv) > 1 else ""
                    
                    if k == "strokeColor":
                        new_p.append("strokeColor=none" if v == "none" else "strokeColor=#000000")
                    elif k == "fontColor":
                        new_p.append("fontColor=#000000")
                    elif k == "fillColor":
                        if v == "none": new_p.append("fillColor=none")
                        elif is_initial or is_final: new_p.append("fillColor=#000000")
                        elif is_th: new_p.append("fillColor=#f1f5f9")
                        elif is_alt: new_p.append("fillColor=#f8fafc")
                        else: new_p.append("fillColor=#ffffff")
                    elif k == "labelBackgroundColor":
                        new_p.append("labelBackgroundColor=#ffffff")
                    else:
                        new_p.append(p)
                if not any(x.startswith("fontColor=") for x in new_p):
                    new_p.append("fontColor=#000000")
                if is_edge and not any(x.startswith("labelBackgroundColor=") for x in new_p):
                    new_p.append("labelBackgroundColor=#ffffff")
                cell.set("style", ";".join(new_p))
                
            if val:
                cleaned = re.sub(r'color:\s*#[0-9a-fA-F]{3,6}', 'color:#000000', val)
                cleaned = re.sub(r'background(?:-color)?:\s*#[0-9a-fA-F]{3,6}', 'background-color:#ffffff', cleaned)
                cell.set("value", cleaned)
                
        out_content = ET.tostring(tree, encoding="utf-8").decode("utf-8")
        if not out_content.startswith("<mxfile"):
            out_content = f'<mxfile host="65bd71144e">\n{out_content}\n</mxfile>'
        with open(fp, "w", encoding="utf-8") as f:
            f.write(out_content)
        print(f"[OK] Cleaned & verified edges for {fn}")

if __name__ == "__main__":
    update_all_drawio()
