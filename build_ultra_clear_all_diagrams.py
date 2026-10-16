import os

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

# =========================================================================
# 1. TUGAS 3: ULTRA-CLEAR USE CASE DIAGRAM (1 TAB TUNGGAL)
# =========================================================================
def generate_tugas_3_xml():
    xml = """<mxfile host="65bd71144e">
    <diagram id="usecase-sipesat" name="Use Case Diagram (SIPESAT)">
        <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1780" pageHeight="1150" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="header_banner" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;USE CASE DIAGRAM — SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Pemodelan UML 2.5 Rekayasa Perangkat Lunak — Kelompok 7 (Kelas RPL_XD 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1680" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- SYSTEM BOUNDARY -->
                <mxCell id="sys_boundary" parent="1" style="swimlane;startSize=32;fontStyle=1;align=center;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Boundary: Sistem Informasi Pengajuan Surat Siswa (SIPESAT)" vertex="1">
                    <mxGeometry height="1000" width="1240" x="260" y="95" as="geometry" />
                </mxCell>

                <!-- ==================== SHARED AUTH & ACCOUNT (TOP ROW) ==================== -->
                <mxCell id="uc_logout" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-04: Logout Sesi" vertex="1">
                    <mxGeometry height="48" width="180" x="180" y="45" as="geometry" />
                </mxCell>

                <mxCell id="uc_login" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-01: Login ke Sistem&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="220" x="510" y="45" as="geometry" />
                </mxCell>

                <mxCell id="uc_validate" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-01B: Validasi Kredensial &amp;amp; Hak Akses&lt;/i&gt;" vertex="1">
                    <mxGeometry height="48" width="220" x="510" y="125" as="geometry" />
                </mxCell>

                <mxCell id="inc_login_val" edge="1" parent="sys_boundary" source="uc_login" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_validate" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_profile" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-03: Kelola Profil &amp;amp; Sandi" vertex="1">
                    <mxGeometry height="48" width="190" x="870" y="45" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 1: SISWA MAIN USE CASES (LEFT) ==================== -->
                <mxCell id="uc_register" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-02: Registrasi Akun Mandiri" vertex="1">
                    <mxGeometry height="50" width="230" x="40" y="210" as="geometry" />
                </mxCell>

                <mxCell id="uc_catalog" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-05: Lihat Katalog &amp;amp; Syarat Surat" vertex="1">
                    <mxGeometry height="50" width="230" x="40" y="305" as="geometry" />
                </mxCell>

                <mxCell id="uc_apply" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-06: Mengajukan Permohonan Surat&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="40" y="405" as="geometry" />
                </mxCell>

                <mxCell id="uc_track" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-08: Melacak Status Surat (Real-time)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="40" y="520" as="geometry" />
                </mxCell>

                <mxCell id="uc_history" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-09: Melihat Riwayat Pengajuan" vertex="1">
                    <mxGeometry height="50" width="230" x="40" y="635" as="geometry" />
                </mxCell>

                <mxCell id="uc_download" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-10: Unduh Surat PDF Ber-QR Code&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="40" y="735" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 2: SISWA INCLUDE & EXTEND ==================== -->
                <mxCell id="uc_upload" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-07: Unggah Berkas Syarat&#10;(PDF &amp;le; 2MB)&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="305" y="407" as="geometry" />
                </mxCell>

                <mxCell id="inc_apply_up" edge="1" parent="sys_boundary" source="uc_apply" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_upload" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_revision" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-08A: Melihat Catatan Koreksi&#10;Revisi Berkas&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="305" y="522" as="geometry" />
                </mxCell>

                <mxCell id="ext_rev_track" edge="1" parent="sys_boundary" source="uc_revision" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_track" value="&amp;lt;&amp;lt;extend&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 3: PETUGAS INCLUDE ==================== -->
                <mxCell id="uc_qr" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-14A: Terbitkan No. Surat &amp;amp;&#10;TTE QR Code Resmi&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="715" y="407" as="geometry" />
                </mxCell>

                <mxCell id="inc_app_qr" edge="1" parent="sys_boundary" source="uc_approve" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_qr" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_note" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-15A: Input Alasan &amp;amp;&#10;Catatan Penolakan&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="715" y="522" as="geometry" />
                </mxCell>

                <mxCell id="inc_rej_note" edge="1" parent="sys_boundary" source="uc_reject" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_note" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 4: PETUGAS MAIN USE CASES (RIGHT) ==================== -->
                <mxCell id="uc_dashboard" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-11: Dashboard Antrean TU" vertex="1">
                    <mxGeometry height="50" width="230" x="960" y="210" as="geometry" />
                </mxCell>

                <mxCell id="uc_inbox" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-12: Kelola Antrean Surat Masuk" vertex="1">
                    <mxGeometry height="50" width="230" x="960" y="305" as="geometry" />
                </mxCell>

                <mxCell id="uc_approve" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-14: Setujui Permohonan (Approve)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="960" y="405" as="geometry" />
                </mxCell>

                <mxCell id="uc_reject" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-15: Tolak Permohonan (Reject)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="960" y="520" as="geometry" />
                </mxCell>

                <mxCell id="uc_verify" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-13: Verifikasi Berkas Dokumen&lt;/b&gt;" vertex="1">
                    <mxGeometry height="50" width="230" x="960" y="635" as="geometry" />
                </mxCell>

                <mxCell id="uc_master" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-16: Kelola Master Jenis Surat" vertex="1">
                    <mxGeometry height="50" width="230" x="960" y="725" as="geometry" />
                </mxCell>

                <mxCell id="uc_users" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-17: Kelola Data Siswa &amp;amp; Akun" vertex="1">
                    <mxGeometry height="50" width="230" x="960" y="810" as="geometry" />
                </mxCell>

                <mxCell id="uc_report" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-18: Ekspor Rekapitulasi Laporan&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="230" x="960" y="895" as="geometry" />
                </mxCell>

                <!-- ==================== ACTORS ==================== -->
                <mxCell id="act_siswa" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;fontStyle=1;fontSize=13;" value="&lt;b&gt;Siswa&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;(Aktor Pemohon)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="140" width="80" x="70" y="475" as="geometry" />
                </mxCell>

                <mxCell id="act_petugas" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;fontStyle=1;fontSize=13;" value="&lt;b&gt;Petugas TU&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;(Verifikator &amp;amp; TU)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="140" width="80" x="1560" y="475" as="geometry" />
                </mxCell>

                <!-- ==================== DIRECT FAN ASSOCIATIONS (ZERO CROSSING) ==================== -->
                <!-- SISWA FAN -->
                <mxCell id="edge_s_reg" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_register">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_cat" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_catalog">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_apply" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_apply">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_track" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_track">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_hist" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_history">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_down" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_download">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- SISWA TO TOP SHARED AUTH (Perimeter routing without crossing) -->
                <mxCell id="edge_s_logout" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_logout">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="110" y="475" />
                            <mxPoint x="110" y="165" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="edge_s_login" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0.25;entryY=0;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_login">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="90" y="475" />
                            <mxPoint x="90" y="65" />
                            <mxPoint x="825" y="65" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- PETUGAS FAN -->
                <mxCell id="edge_p_dash" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_dashboard">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_inbox" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_inbox">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_app" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_approve">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_rej" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_reject">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_ver" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_verify">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_mast" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_master">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_usr" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_users">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_rep" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_report">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- PETUGAS TO TOP SHARED AUTH -->
                <mxCell id="edge_p_prof" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_profile">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1600" y="475" />
                            <mxPoint x="1600" y="165" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="edge_p_login" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0.75;entryY=0;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_login">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1620" y="475" />
                            <mxPoint x="1620" y="65" />
                            <mxPoint x="935" y="65" />
                        </Array>
                    </mxGeometry>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""
    return xml

# =========================================================================
# 2. TUGAS 4: ULTRA-CLEAR 2-TAB DIAGRAM (ACTIVITY 3-SWIMLANE + 2 SEQUENCE BCE)
# =========================================================================
def generate_tugas_4_xml():
    # TAB 1: ACTIVITY DIAGRAM (Full width 3 Swimlanes, self-documenting steps, NO SQUEEZE)
    tab1_xml = """    <diagram id="act-terpadu" name="1. Activity Diagram (Siswa s.d Petugas)">
        <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1780" pageHeight="1350" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />

                <!-- HEADER BANNER -->
                <mxCell id="act_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;ACTIVITY DIAGRAM — ALUR TERPADU PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Standar Modul UNINDRA: Swimlane Terpadu (Aktor Siswa ➔ Sistem SIPESAT ➔ Petugas TU &amp;amp; Kepsek)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1680" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- SWIMLANE 1: SISWA (LEFT, WIDTH 500) -->
                <mxCell id="lane_siswa" parent="1" style="swimlane;startSize=32;fontStyle=1;align=center;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Siswa (Aktor Pemohon)" vertex="1">
                    <mxGeometry height="1200" width="500" x="50" y="95" as="geometry" />
                </mxCell>

                <mxCell id="act_start" parent="lane_siswa" style="ellipse;fillColor=#000000;strokeColor=#000000;fontColor=#000000" value="" vertex="1">
                    <mxGeometry height="34" width="34" x="233" y="45" as="geometry" />
                </mxCell>

                <mxCell id="s_step_1" parent="lane_siswa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="1. Buka Web SIPESAT &amp;amp; Login Akun&#10;(Input NISN &amp;amp; Kata Sandi)" vertex="1">
                    <mxGeometry height="52" width="290" x="105" y="110" as="geometry" />
                </mxCell>

                <mxCell id="s_step_2" parent="lane_siswa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="2. Masuk Menu 'Pengajuan Surat' &amp;amp;&#10;Pilih Jenis Surat yang Diperlukan" vertex="1">
                    <mxGeometry height="52" width="290" x="105" y="200" as="geometry" />
                </mxCell>

                <mxCell id="s_step_3" parent="lane_siswa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="3. Isi Formulir Keperluan &amp;amp;&#10;Unggah Dokumen Syarat (PDF &amp;le; 2MB)" vertex="1">
                    <mxGeometry height="52" width="290" x="105" y="290" as="geometry" />
                </mxCell>

                <mxCell id="s_step_4" parent="lane_siswa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="4. Klik Tombol 'Kirim Permohonan'" vertex="1">
                    <mxGeometry height="48" width="270" x="115" y="380" as="geometry" />
                </mxCell>

                <mxCell id="s_step_revisi" parent="lane_siswa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="Menerima Catatan Koreksi Revisi &amp;amp;&#10;Perbaiki Berkas yang Kurang" vertex="1">
                    <mxGeometry height="55" width="290" x="105" y="740" as="geometry" />
                </mxCell>

                <mxCell id="s_step_unduh" parent="lane_siswa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;fontStyle=1;" value="12. Terima Notifikasi Selesai &amp;amp;&#10;Unduh Berkas PDF Surat Resmi" vertex="1">
                    <mxGeometry height="55" width="290" x="105" y="1000" as="geometry" />
                </mxCell>

                <mxCell id="s_end_node" parent="lane_siswa" style="ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000" value="" vertex="1">
                    <mxGeometry height="36" width="36" x="232" y="1100" as="geometry" />
                </mxCell>

                <!-- SWIMLANE 2: SISTEM WEB SIPESAT (CENTER, WIDTH 580) -->
                <mxCell id="lane_sistem" parent="1" style="swimlane;startSize=32;fontStyle=1;align=center;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Sistem (Aplikasi Web SIPESAT)" vertex="1">
                    <mxGeometry height="1200" width="580" x="560" y="95" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_val" parent="lane_sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="5. Validasi Kelengkapan Formulir &amp;amp;&#10;Format / Ukuran File Dokumen" vertex="1">
                    <mxGeometry height="52" width="290" x="145" y="380" as="geometry" />
                </mxCell>

                <mxCell id="sys_dec_file" parent="lane_sistem" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=11;fontStyle=1;" value="Form Lengkap&#10;&amp;amp; File &amp;le; 2MB?" vertex="1">
                    <mxGeometry height="65" width="160" x="210" y="465" as="geometry" />
                </mxCell>

                <mxCell id="sys_err_alert" parent="lane_sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11;" value="Tampilkan Peringatan Validasi:&#10;'File &amp;gt; 2MB / Formulir Kosong'" vertex="1">
                    <mxGeometry height="48" width="220" x="20" y="555" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_save" parent="lane_sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="6. Simpan Database (Status: DIAJUKAN)&#10;&amp;amp; Terbitkan Nomor Resi Tiket Unik" vertex="1">
                    <mxGeometry height="52" width="290" x="145" y="565" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_forward" parent="lane_sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="7. Teruskan Berkas ke Meja Antrean TU" vertex="1">
                    <mxGeometry height="48" width="290" x="145" y="650" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_rej" parent="lane_sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="UPDATE Status: 'DITOLAK_PERLU_REVISI'&#10;&amp;amp; Kirim Notifikasi Koreksi ke Siswa" vertex="1">
                    <mxGeometry height="55" width="290" x="145" y="740" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_compile" parent="lane_sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;fontStyle=1;" value="11. Kompilasi Kop Sekolah, Data &amp;amp; QR Code&#10;ke File PDF (Status: SELESAI)" vertex="1">
                    <mxGeometry height="55" width="310" x="135" y="1000" as="geometry" />
                </mxCell>

                <!-- SWIMLANE 3: PETUGAS TU & KEPSEK (RIGHT, WIDTH 580) -->
                <mxCell id="lane_petugas" parent="1" style="swimlane;startSize=32;fontStyle=1;align=center;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Petugas TU &amp;amp; Kepala Sekolah" vertex="1">
                    <mxGeometry height="1200" width="580" x="1150" y="95" as="geometry" />
                </mxCell>

                <mxCell id="p_step_review" parent="lane_petugas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="8. Login ke Panel TU, Buka Antrean&#10;&amp;amp; Tinjau Berkas Dokumen Siswa" vertex="1">
                    <mxGeometry height="52" width="290" x="145" y="650" as="geometry" />
                </mxCell>

                <mxCell id="p_dec_valid" parent="lane_petugas" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=11;fontStyle=1;" value="Berkas Lengkap&#10;&amp;amp; Sah?" vertex="1">
                    <mxGeometry height="65" width="160" x="210" y="735" as="geometry" />
                </mxCell>

                <mxCell id="p_step_rej" parent="lane_petugas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="9A. Input Alasan / Catatan Koreksi &amp;amp;&#10;Klik 'Tolak &amp;amp; Minta Revisi'" vertex="1">
                    <mxGeometry height="52" width="260" x="20" y="830" as="geometry" />
                </mxCell>

                <mxCell id="p_step_app" parent="lane_petugas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="9B. Input No. Agenda Masuk TU &amp;amp;&#10;Teruskan Permohonan ke Kepsek" vertex="1">
                    <mxGeometry height="52" width="270" x="290" y="830" as="geometry" />
                </mxCell>

                <mxCell id="p_step_sign" parent="lane_petugas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;fontStyle=1;" value="10. Kepsek Menyetujui, Generate No. Surat&#10;Resmi &amp;amp; Bubuhkan TTE Kode QR" vertex="1">
                    <mxGeometry height="55" width="300" x="140" y="920" as="geometry" />
                </mxCell>

                <!-- ==================== FLOW CONNECTORS ==================== -->
                <mxCell id="c_1" edge="1" parent="1" source="act_start" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_1">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="c_2" edge="1" parent="1" source="s_step_1" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_2">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="c_3" edge="1" parent="1" source="s_step_2" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_3">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="c_4" edge="1" parent="1" source="s_step_3" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_4">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Siswa Kirim -> Sistem Validasi -->
                <mxCell id="c_5" edge="1" parent="1" source="s_step_4" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_step_val">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Sistem Validasi -> Decision 1 -->
                <mxCell id="c_6" edge="1" parent="1" source="sys_step_val" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_dec_file">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Decision 1: Tidak -->
                <mxCell id="c_7" edge="1" parent="1" source="sys_dec_file" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_err_alert" value="[Tidak]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Error Alert -> Siswa Step 3 (Loop back) -->
                <mxCell id="c_8" edge="1" parent="1" source="sys_err_alert" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0.5;entryY=1;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_3" value="Perbaiki File">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="690" y="630" />
                            <mxPoint x="300" y="630" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- Decision 1: Ya -->
                <mxCell id="c_9" edge="1" parent="1" source="sys_dec_file" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_step_save" value="[Ya]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="c_10" edge="1" parent="1" source="sys_step_save" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_step_forward">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Sistem Forward -> Petugas Review -->
                <mxCell id="c_11" edge="1" parent="1" source="sys_step_forward" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_step_review">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Petugas Review -> Decision 2 -->
                <mxCell id="c_12" edge="1" parent="1" source="p_step_review" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_dec_valid">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Decision 2: Tidak -->
                <mxCell id="c_13" edge="1" parent="1" source="p_dec_valid" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_step_rej" value="[Tidak / Buram]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Petugas Tolak -> Sistem Update Tolak -->
                <mxCell id="c_14" edge="1" parent="1" source="p_step_rej" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_step_rej">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Sistem Update Tolak -> Siswa Terima Catatan Revisi -->
                <mxCell id="c_15" edge="1" parent="1" source="sys_step_rej" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_revisi">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Siswa Revisi -> Kirim Ulang (Loop to Step 3) -->
                <mxCell id="c_16" edge="1" parent="1" source="s_step_revisi" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_3" value="Upload Ulang">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="100" y="860" />
                            <mxPoint x="100" y="411" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- Decision 2: Ya -->
                <mxCell id="c_17" edge="1" parent="1" source="p_dec_valid" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_step_app" value="[Ya / Sah]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Petugas App -> Kepsek Sign -->
                <mxCell id="c_18" edge="1" parent="1" source="p_step_app" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_step_sign">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Kepsek Sign -> Sistem Compile PDF -->
                <mxCell id="c_19" edge="1" parent="1" source="p_step_sign" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_step_compile">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Sistem Compile -> Siswa Unduh -->
                <mxCell id="c_20" edge="1" parent="1" source="sys_step_compile" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_unduh">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Siswa Unduh -> Selesai -->
                <mxCell id="c_21" edge="1" parent="1" source="s_step_unduh" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_end_node">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>"""

    # TAB 2: SEQUENCE DIAGRAMS (2 CLEAN WIDE DIAGRAMS, HIGH READABILITY)
    tab2_xml = """    <diagram id="sequence-diagrams" name="2. Sequence Diagrams (Pola BCE UNINDRA)">
        <mxGraphModel dx="1600" dy="1400" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1780" pageHeight="1450" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />

                <!-- HEADER BANNER -->
                <mxCell id="seq_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;SEQUENCE DIAGRAMS — SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Format Standar Bahan Ajar RPL UNINDRA (Slide 18-26): Pola Arsitektur Boundary (|O), Control (↺O), Entity (_O_) + Frame Alt&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1680" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- ==================== DIAGRAM 1: PENGAJUAN SURAT (SISWA) ==================== -->
                <mxCell id="box_seq1" parent="1" style="swimlane;startSize=28;fontStyle=1;align=center;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="1. SEQUENCE DIAGRAM: PENGAJUAN SURAT OLEH SISWA (POLA BCE)" vertex="1">
                    <mxGeometry height="580" width="1680" x="50" y="95" as="geometry" />
                </mxCell>

                <!-- LIFELINES SEQ 1 -->
                <mxCell id="act_siswa_seq" parent="box_seq1" style="shape=umlActor;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="Siswa&#10;(Aktor)" vertex="1">
                    <mxGeometry height="80" width="45" x="140" y="45" as="geometry" />
                </mxCell>

                <mxCell id="bnd_form_seq" parent="box_seq1" style="shape=umlBoundary;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="FormPengajuanUI&#10;(Boundary |O)" vertex="1">
                    <mxGeometry height="65" width="70" x="520" y="55" as="geometry" />
                </mxCell>

                <mxCell id="ctrl_surat_seq" parent="box_seq1" style="shape=umlControl;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="SuratController&#10;(Control ↺O)" vertex="1">
                    <mxGeometry height="65" width="65" x="940" y="55" as="geometry" />
                </mxCell>

                <mxCell id="ent_surat_seq" parent="box_seq1" style="shape=umlEntity;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="tb_pengajuan_surat&#10;(Entity _O_)" vertex="1">
                    <mxGeometry height="65" width="65" x="1360" y="55" as="geometry" />
                </mxCell>

                <!-- DASHED VERTICAL LINES -->
                <mxCell id="line_s1_act" edge="1" parent="box_seq1" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="162" y="140" as="sourcePoint" />
                        <mxPoint x="162" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s1_bnd" edge="1" parent="box_seq1" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="140" as="sourcePoint" />
                        <mxPoint x="555" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s1_ctrl" edge="1" parent="box_seq1" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="972" y="140" as="sourcePoint" />
                        <mxPoint x="972" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s1_ent" edge="1" parent="box_seq1" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1392" y="140" as="sourcePoint" />
                        <mxPoint x="1392" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- MESSAGES SEQ 1 -->
                <mxCell id="m_s1_1" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="1. bukaMenuPengajuan()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="162" y="160" as="sourcePoint" />
                        <mxPoint x="555" y="160" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s1_2" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="2. tampilkanFormulirSurat()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="195" as="sourcePoint" />
                        <mxPoint x="162" y="195" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s1_3" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="3. submitPermohonan(jenisSurat, keperluan, fileBerkas)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="162" y="235" as="sourcePoint" />
                        <mxPoint x="555" y="235" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s1_4" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="4. validasiPayloadBerkas(fileSize, fileType)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="265" as="sourcePoint" />
                        <mxPoint x="972" y="265" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- FRAME ALT SEQ 1 -->
                <mxCell id="frame_alt_s1" parent="box_seq1" style="shape=umlFrame;whiteSpace=wrap;html=1;width=140;height=22;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontSize=11;fontColor=#000000;" value="alt [Berkas &amp;le; 2MB &amp;amp; Valid]" vertex="1">
                    <mxGeometry height="240" width="1320" x="120" y="295" as="geometry" />
                </mxCell>

                <mxCell id="m_s1_5" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="5. insertPengajuan(nisn, jenis, status='DIAJUKAN')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="972" y="335" as="sourcePoint" />
                        <mxPoint x="1392" y="335" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s1_6" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="6. returnRecord(idPengajuan, nomorTiketResi)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1392" y="370" as="sourcePoint" />
                        <mxPoint x="972" y="370" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s1_7" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="7. tampilkanResiSukses(nomorTiket)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="405" as="sourcePoint" />
                        <mxPoint x="162" y="405" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- ALT DIVIDER LINE -->
                <mxCell id="alt_line_s1" edge="1" parent="box_seq1" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.2;" value="[Berkas &amp;gt; 2MB / Form Kosong]">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="120" y="445" as="sourcePoint" />
                        <mxPoint x="1440" y="445" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s1_8" edge="1" parent="box_seq1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="8. responseError('Ukuran file melebihi 2MB, silakan unggah ulang')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="490" as="sourcePoint" />
                        <mxPoint x="162" y="490" as="targetPoint" />
                    </mxGeometry>
                </mxCell>


                <!-- ==================== DIAGRAM 2: VERIFIKASI & APPROVAL (PETUGAS TU) ==================== -->
                <mxCell id="box_seq2" parent="1" style="swimlane;startSize=28;fontStyle=1;align=center;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="2. SEQUENCE DIAGRAM: VERIFIKASI &amp;amp; PENGESAHAN DOKUMEN OLEH PETUGAS TU (POLA BCE)" vertex="1">
                    <mxGeometry height="580" width="1680" x="50" y="700" as="geometry" />
                </mxCell>

                <!-- LIFELINES SEQ 2 -->
                <mxCell id="act_tu_seq" parent="box_seq2" style="shape=umlActor;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="Petugas TU&#10;(Aktor)" vertex="1">
                    <mxGeometry height="80" width="45" x="140" y="45" as="geometry" />
                </mxCell>

                <mxCell id="bnd_tu_seq" parent="box_seq2" style="shape=umlBoundary;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="VerifikasiTUUI&#10;(Boundary |O)" vertex="1">
                    <mxGeometry height="65" width="70" x="520" y="55" as="geometry" />
                </mxCell>

                <mxCell id="ctrl_tu_seq" parent="box_seq2" style="shape=umlControl;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="VerifikasiController&#10;(Control ↺O)" vertex="1">
                    <mxGeometry height="65" width="65" x="940" y="55" as="geometry" />
                </mxCell>

                <mxCell id="ent_tu_seq" parent="box_seq2" style="shape=umlEntity;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;" value="tb_pengajuan_surat&#10;(Entity _O_)" vertex="1">
                    <mxGeometry height="65" width="65" x="1360" y="55" as="geometry" />
                </mxCell>

                <!-- DASHED VERTICAL LINES -->
                <mxCell id="line_s2_act" edge="1" parent="box_seq2" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="162" y="140" as="sourcePoint" />
                        <mxPoint x="162" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s2_bnd" edge="1" parent="box_seq2" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="140" as="sourcePoint" />
                        <mxPoint x="555" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s2_ctrl" edge="1" parent="box_seq2" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="972" y="140" as="sourcePoint" />
                        <mxPoint x="972" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s2_ent" edge="1" parent="box_seq2" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1392" y="140" as="sourcePoint" />
                        <mxPoint x="1392" y="550" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- MESSAGES SEQ 2 -->
                <mxCell id="m_s2_1" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="1. bukaAntreanSuratMasuk()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="162" y="160" as="sourcePoint" />
                        <mxPoint x="555" y="160" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_2" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="2. getDaftarPengajuanStatus('DIAJUKAN')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="190" as="sourcePoint" />
                        <mxPoint x="972" y="190" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_3" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="3. selectQuery(status='DIAJUKAN')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="972" y="215" as="sourcePoint" />
                        <mxPoint x="1392" y="215" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_4" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="4. returnDaftarBerkas()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1392" y="240" as="sourcePoint" />
                        <mxPoint x="555" y="240" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- FRAME ALT SEQ 2 -->
                <mxCell id="frame_alt_s2" parent="box_seq2" style="shape=umlFrame;whiteSpace=wrap;html=1;width=140;height=22;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontSize=11;fontColor=#000000;" value="alt [Berkas Sah &amp;amp; Disetujui]" vertex="1">
                    <mxGeometry height="260" width="1320" x="120" y="275" as="geometry" />
                </mxCell>

                <mxCell id="m_s2_5" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="5. approvePermohonan(id, nomorAgenda, qrCodeHash)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="162" y="315" as="sourcePoint" />
                        <mxPoint x="555" y="315" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_6" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="6. updateStatus(status='SELESAI', noSurat, qrCode)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="972" y="345" as="sourcePoint" />
                        <mxPoint x="1392" y="345" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_7" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="7. tampilkanKonfirmasiSukses('Surat resmi berhasil disahkan dan terbit')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="380" as="sourcePoint" />
                        <mxPoint x="162" y="380" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- ALT DIVIDER LINE 2 -->
                <mxCell id="alt_line_s2" edge="1" parent="box_seq2" style="endArrow=none;dashed=1;strokeColor=#000000;strokeWidth=1.2;" value="[Berkas Buram / Perlu Revisi]">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="120" y="420" as="sourcePoint" />
                        <mxPoint x="1440" y="420" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_8" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="8. tolakPermohonan(id, catatanKoreksi)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="162" y="455" as="sourcePoint" />
                        <mxPoint x="555" y="455" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_9" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="9. updateStatus(status='DITOLAK_PERLU_REVISI', catatan)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="972" y="485" as="sourcePoint" />
                        <mxPoint x="1392" y="485" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <mxCell id="m_s2_10" edge="1" parent="box_seq2" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="10. notifikasiCatatanRevisiKeSiswa(idSiswa)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="555" y="515" as="sourcePoint" />
                        <mxPoint x="162" y="515" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>"""

    full_xml = f"""<mxfile host="65bd71144e">
{tab1_xml}
{tab2_xml}
</mxfile>
"""
    return full_xml


# =========================================================================
# 3. TUGAS 5: ULTRA-CLEAR LINEAR STATE MACHINE DIAGRAM (1 TAB TUNGGAL)
# =========================================================================
def generate_tugas_5_xml():
    xml = """<mxfile host="65bd71144e">
    <diagram id="state-machine-surat" name="State Machine (SuratPengajuan)">
        <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1780" pageHeight="750" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="sm_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;STATE MACHINE DIAGRAM — SIKLUS HIDUP PERMOHONAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Pemodelan UML 2.5 Entitas Dokumen Permohonan (tb_pengajuan_surat) — Kelompok 7 (RPL_XD 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1680" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- START NODE -->
                <mxCell id="sm_init" parent="1" style="ellipse;fillColor=#000000;strokeColor=#000000;fontColor=#000000" value="" vertex="1">
                    <mxGeometry height="35" width="35" x="65" y="220" as="geometry" />
                </mxCell>

                <!-- STATE 1: DRAFT -->
                <mxCell id="sm_draft" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;1. DRAFT&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Tampilkan Form Surat&lt;br&gt;do / Input Data &amp;amp; Unggah Berkas&lt;br&gt;exit / Validasi Format Berkas&lt;/div&gt;" vertex="1">
                    <mxGeometry height="95" width="220" x="160" y="190" as="geometry" />
                </mxCell>

                <!-- STATE 2: MENUNGGU VERIFIKASI -->
                <mxCell id="sm_menunggu" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;2. MENUNGGU_VERIFIKASI&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Generate Kode Tiket Resi&lt;br&gt;do / Masuk Antrean Verifikasi TU&lt;br&gt;exit / Notifikasi ke Meja Staf TU&lt;/div&gt;" vertex="1">
                    <mxGeometry height="95" width="240" x="470" y="190" as="geometry" />
                </mxCell>

                <!-- SUB-BRANCH: STATE DITOLAK PERLU REVISI -->
                <mxCell id="sm_revisi" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;DITOLAK_PERLU_REVISI&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Catat Alasan Penolakan&lt;br&gt;do / Siswa Mengunggah Berkas Baru&lt;br&gt;exit / Notifikasi Perbaikan Selesai&lt;/div&gt;" vertex="1">
                    <mxGeometry height="95" width="240" x="470" y="380" as="geometry" />
                </mxCell>

                <!-- STATE 3: DIVERIFIKASI TU -->
                <mxCell id="sm_diverifikasi" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;3. DIVERIFIKASI_TU&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Tetapkan No. Agenda Masuk&lt;br&gt;do / Teruskan ke Meja Kepsek&lt;br&gt;exit / Siap Ditandatangani&lt;/div&gt;" vertex="1">
                    <mxGeometry height="95" width="230" x="800" y="190" as="geometry" />
                </mxCell>

                <!-- STATE 4: DISETUJUI KEPSEK -->
                <mxCell id="sm_disetujui" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;4. DISETUJUI_KEPSEK&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Generate Nomor Surat Keluar&lt;br&gt;do / Terbitkan QR Code Tanda Tangan&lt;br&gt;exit / Render Dokumen PDF Resmi&lt;/div&gt;" vertex="1">
                    <mxGeometry height="95" width="230" x="1120" y="190" as="geometry" />
                </mxCell>

                <!-- STATE 5: SELESAI SIAP UNDUH -->
                <mxCell id="sm_selesai" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.5;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;5. SELESAI_SIAP_UNDUH&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Kirim Notifikasi Surat Terbit&lt;br&gt;do / Layani Unduh File PDF Siswa&lt;br&gt;exit / Catat Riwayat Pengambilan&lt;/div&gt;" vertex="1">
                    <mxGeometry height="95" width="230" x="1440" y="190" as="geometry" />
                </mxCell>

                <!-- SUB-BRANCH: STATE 6 DIARSIPKAN -->
                <mxCell id="sm_arsip" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;6. DIARSIPKAN&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Kunci Record Data Surat&lt;br&gt;do / Masuk Arsip Statis Sekolah&lt;/div&gt;" vertex="1">
                    <mxGeometry height="85" width="230" x="1440" y="385" as="geometry" />
                </mxCell>

                <!-- END NODE -->
                <mxCell id="sm_final" parent="1" style="ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=#000000;strokeWidth=2;fontColor=#000000" value="" vertex="1">
                    <mxGeometry height="36" width="36" x="1290" y="410" as="geometry" />
                </mxCell>

                <!-- ==================== CLEAN STRAIGHT TRANSITIONS ==================== -->
                <!-- Init -> Draft -->
                <mxCell id="tr_1" edge="1" parent="1" source="sm_init" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_draft" value="Pilih Surat">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Draft -> Menunggu -->
                <mxCell id="tr_2" edge="1" parent="1" source="sm_draft" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_menunggu" value="Kirim Permohonan&#10;[Berkas Lengkap &amp;le; 2MB]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Menunggu -> Revisi (Down) -->
                <mxCell id="tr_3" edge="1" parent="1" source="sm_menunggu" style="endArrow=block;endFill=1;strokeWidth=1.8;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_revisi" value="Tolak TU [Berkas Buram/Kurang]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Revisi -> Menunggu (Loop back up) -->
                <mxCell id="tr_4" edge="1" parent="1" source="sm_revisi" style="endArrow=block;endFill=1;strokeWidth=1.8;strokeColor=#000000;edgeStyle=orthogonalEdgeStyle;entryX=0.25;entryY=1;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_menunggu" value="Unggah Ulang Berkas&#10;[Ukuran Sesuai]">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="430" y="427" />
                            <mxPoint x="430" y="320" />
                            <mxPoint x="530" y="320" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- Menunggu -> Diverifikasi TU -->
                <mxCell id="tr_5" edge="1" parent="1" source="sm_menunggu" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_diverifikasi" value="Verifikasi TU&#10;[Berkas Lengkap &amp;amp; Sah]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Diverifikasi TU -> Disetujui Kepsek -->
                <mxCell id="tr_6" edge="1" parent="1" source="sm_diverifikasi" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_disetujui" value="Persetujuan Kepsek&#10;[Disahkan]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Disetujui -> Selesai -->
                <mxCell id="tr_7" edge="1" parent="1" source="sm_disetujui" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_selesai" value="Kompilasi PDF&#10;Berhasil">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Selesai -> Arsip (Down) -->
                <mxCell id="tr_8" edge="1" parent="1" source="sm_selesai" style="endArrow=block;endFill=1;strokeWidth=1.8;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_arsip" value="Selesai Diunduh /&#10;Masa Retensi Aktif">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Arsip -> End (Left) -->
                <mxCell id="tr_9" edge="1" parent="1" source="sm_arsip" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_final" value="Arsip Permanen">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""
    return xml

# =========================================================================
# EXECUTION
# =========================================================================
if __name__ == "__main__":
    t3_path = os.path.join(RPL_DIR, "tugas-3-usecase.drawio")
    with open(t3_path, "w", encoding="utf-8") as f:
        f.write(generate_tugas_3_xml().strip() + "\n")
    print(f"[OK] Successfully built ultra-clear: {t3_path}")

    t4_path = os.path.join(RPL_DIR, "tugas-4-activity-sequence.drawio")
    with open(t4_path, "w", encoding="utf-8") as f:
        f.write(generate_tugas_4_xml().strip() + "\n")
    print(f"[OK] Successfully built ultra-clear: {t4_path}")

    t5_path = os.path.join(RPL_DIR, "tugas-5-state-machine.drawio")
    with open(t5_path, "w", encoding="utf-8") as f:
        f.write(generate_tugas_5_xml().strip() + "\n")
    print(f"[OK] Successfully built ultra-clear: {t5_path}")
