import os
import re
import xml.etree.ElementTree as ET

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

# =========================================================================
# 1. TUGAS 3: ULTRA-CLEAR USE CASE DIAGRAM (1 TAB, ALL GLOBAL COORDS)
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

                <!-- SYSTEM BOUNDARY (Background Container on parent=1) -->
                <mxCell id="sys_boundary" parent="1" style="swimlane;startSize=34;fontStyle=1;align=center;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Boundary: Sistem Informasi Pengajuan Surat Siswa (SIPESAT)" vertex="1">
                    <mxGeometry height="1000" width="1240" x="260" y="95" as="geometry" />
                </mxCell>

                <!-- ==================== SHARED AUTH (TOP CENTER, CLEAR HORIZONTAL ACCESS) ==================== -->
                <mxCell id="uc_login" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-01: Login ke Sistem&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="220" x="770" y="150" as="geometry" />
                </mxCell>

                <mxCell id="uc_validate" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-01B: Validasi Kredensial &amp;amp; Hak Akses&lt;/i&gt;" vertex="1">
                    <mxGeometry height="50" width="230" x="765" y="245" as="geometry" />
                </mxCell>

                <mxCell id="inc_login_val" edge="1" parent="1" source="uc_login" style="html=1;verticalAlign=middle;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="uc_validate" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 1: SISWA MAIN USE CASES (LEFT: x=300..530) ==================== -->
                <mxCell id="uc_register" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-02: Registrasi Akun Mandiri" vertex="1">
                    <mxGeometry height="50" width="230" x="300" y="235" as="geometry" />
                </mxCell>

                <mxCell id="uc_catalog" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-05: Lihat Katalog &amp;amp; Syarat Surat" vertex="1">
                    <mxGeometry height="50" width="230" x="300" y="330" as="geometry" />
                </mxCell>

                <mxCell id="uc_apply" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-06: Mengajukan Permohonan Surat&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="300" y="430" as="geometry" />
                </mxCell>

                <mxCell id="uc_track" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-08: Melacak Status Surat (Real-time)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="300" y="540" as="geometry" />
                </mxCell>

                <mxCell id="uc_history" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-09: Melihat Riwayat Pengajuan" vertex="1">
                    <mxGeometry height="50" width="230" x="300" y="650" as="geometry" />
                </mxCell>

                <mxCell id="uc_download" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-10: Unduh Surat PDF Ber-QR Code&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="300" y="750" as="geometry" />
                </mxCell>

                <mxCell id="uc_logout" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-04: Logout Sesi" vertex="1">
                    <mxGeometry height="50" width="230" x="300" y="855" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 2: SISWA INCLUDE & EXTEND (x=610..815) ==================== -->
                <mxCell id="uc_upload" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-07: Unggah Berkas Syarat&lt;br&gt;(PDF &amp;le; 2MB)&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="610" y="432" as="geometry" />
                </mxCell>

                <mxCell id="inc_apply_up" edge="1" parent="1" source="uc_apply" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_upload" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_revision" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-08A: Melihat Catatan Koreksi&lt;br&gt;Revisi Berkas&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="610" y="542" as="geometry" />
                </mxCell>

                <mxCell id="ext_rev_track" edge="1" parent="1" source="uc_revision" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_track" value="&amp;lt;&amp;lt;extend&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 3: PETUGAS INCLUDE (x=945..1150) ==================== -->
                <mxCell id="uc_qr" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-14A: Terbitkan No. Surat &amp;amp;&lt;br&gt;TTE QR Code Resmi&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="945" y="432" as="geometry" />
                </mxCell>

                <mxCell id="uc_note" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-15A: Input Alasan &amp;amp;&lt;br&gt;Catatan Penolakan&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="205" x="945" y="542" as="geometry" />
                </mxCell>

                <!-- ==================== COLUMN 4: PETUGAS MAIN USE CASES (RIGHT: x=1230..1460) ==================== -->
                <mxCell id="uc_dashboard" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-11: Dashboard Antrean TU" vertex="1">
                    <mxGeometry height="50" width="230" x="1230" y="235" as="geometry" />
                </mxCell>

                <mxCell id="uc_inbox" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-12: Kelola Antrean Surat Masuk" vertex="1">
                    <mxGeometry height="50" width="230" x="1230" y="330" as="geometry" />
                </mxCell>

                <mxCell id="uc_approve" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-14: Setujui Permohonan (Approve)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="1230" y="430" as="geometry" />
                </mxCell>

                <mxCell id="inc_app_qr" edge="1" parent="1" source="uc_approve" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_qr" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_reject" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-15: Tolak Permohonan (Reject)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="1230" y="540" as="geometry" />
                </mxCell>

                <mxCell id="inc_rej_note" edge="1" parent="1" source="uc_reject" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_note" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_verify" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-13: Verifikasi Berkas Dokumen&lt;/b&gt;" vertex="1">
                    <mxGeometry height="50" width="230" x="1230" y="650" as="geometry" />
                </mxCell>

                <mxCell id="uc_master" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-16: Kelola Master Jenis Surat" vertex="1">
                    <mxGeometry height="50" width="230" x="1230" y="740" as="geometry" />
                </mxCell>

                <mxCell id="uc_users" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-17: Kelola Data Siswa &amp;amp; Akun" vertex="1">
                    <mxGeometry height="50" width="230" x="1230" y="830" as="geometry" />
                </mxCell>

                <mxCell id="uc_report" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-18: Ekspor Rekapitulasi Laporan&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="230" x="1230" y="920" as="geometry" />
                </mxCell>

                <mxCell id="uc_profile" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-03: Kelola Profil &amp;amp; Sandi" vertex="1">
                    <mxGeometry height="50" width="230" x="1230" y="1010" as="geometry" />
                </mxCell>

                <!-- ==================== ACTORS ==================== -->
                <mxCell id="act_siswa" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;fontStyle=1;fontSize=13;labelBackgroundColor=#ffffff;" value="&lt;b&gt;Siswa&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;(Aktor Pemohon)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="130" width="75" x="75" y="490" as="geometry" />
                </mxCell>

                <mxCell id="act_petugas" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;fontStyle=1;fontSize=13;labelBackgroundColor=#ffffff;" value="&lt;b&gt;Petugas TU&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;(Verifikator &amp;amp; TU)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="130" width="75" x="1610" y="490" as="geometry" />
                </mxCell>

                <!-- ==================== ASSOCIATIONS (ZERO CROSSING) ==================== -->
                <!-- SISWA SHARED LOGIN (Orthogonal below boundary title bar at y=176) -->
                <mxCell id="edge_s_login" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_login">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="112" y="176" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- SISWA DIRECT FAN -->
                <mxCell id="edge_s_reg" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.2;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_register">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_cat" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.3;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_catalog">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_apply" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;exitX=1;exitY=0.45;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_apply">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_track" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;exitX=1;exitY=0.55;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_track">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_hist" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.7;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_history">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_down" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;exitX=1;exitY=0.85;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_download">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_s_logout" edge="1" parent="1" source="act_siswa" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="uc_logout">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- PETUGAS SHARED LOGIN (Orthogonal below boundary title bar at y=176) -->
                <mxCell id="edge_p_login" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.8;edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_login">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1647" y="176" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- PETUGAS DIRECT FAN -->
                <mxCell id="edge_p_dash" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0;exitY=0.15;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_dashboard">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_inbox" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0;exitY=0.28;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_inbox">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_app" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;exitX=0;exitY=0.4;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_approve">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_rej" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;exitX=0;exitY=0.52;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_reject">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_ver" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;exitX=0;exitY=0.65;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_verify">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_mast" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0;exitY=0.75;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_master">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_usr" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0;exitY=0.85;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_users">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_rep" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;exitX=0;exitY=0.92;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_report">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="edge_p_prof" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="uc_profile">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""
    return xml


# =========================================================================
# 2. TUGAS 4: ULTRA-CLEAR 2-TAB DIAGRAM (ALL GLOBAL COORDS, ZERO OVERLAP)
# =========================================================================
def generate_tugas_4_xml():
    # TAB 1: ACTIVITY DIAGRAM (100% Global Coordinates on parent="1")
    tab1_xml = """    <diagram id="act-terpadu" name="1. Activity Diagram (Siswa s.d Petugas)">
        <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1800" pageHeight="1350" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />

                <!-- HEADER BANNER -->
                <mxCell id="act_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;ACTIVITY DIAGRAM — ALUR TERPADU PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Standar Modul UNINDRA: Swimlane Terpadu (Aktor Siswa ➔ Sistem SIPESAT ➔ Petugas TU &amp;amp; Kepala Sekolah)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1700" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- SWIMLANE BACKGROUNDS (All on parent=1) -->
                <mxCell id="lane_siswa" parent="1" style="swimlane;startSize=34;fontStyle=1;align=center;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Siswa (Aktor Pemohon)" vertex="1">
                    <mxGeometry height="1210" width="520" x="50" y="95" as="geometry" />
                </mxCell>
                <mxCell id="lane_sistem" parent="1" style="swimlane;startSize=34;fontStyle=1;align=center;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Sistem (Aplikasi Web SIPESAT)" vertex="1">
                    <mxGeometry height="1210" width="620" x="570" y="95" as="geometry" />
                </mxCell>
                <mxCell id="lane_petugas" parent="1" style="swimlane;startSize=34;fontStyle=1;align=center;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Petugas TU &amp;amp; Kepala Sekolah" vertex="1">
                    <mxGeometry height="1210" width="560" x="1190" y="95" as="geometry" />
                </mxCell>

                <!-- ==================== NODES IN LANE 1: SISWA (x=190..470, center x=330) ==================== -->
                <mxCell id="act_start" parent="1" style="ellipse;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#000000;" value="" vertex="1">
                    <mxGeometry height="34" width="34" x="313" y="145" as="geometry" />
                </mxCell>

                <mxCell id="s_step_1" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="1. Buka Web SIPESAT &amp;amp; Login Akun&lt;br&gt;(Input NISN &amp;amp; Kata Sandi)" vertex="1">
                    <mxGeometry height="52" width="280" x="190" y="210" as="geometry" />
                </mxCell>

                <mxCell id="s_step_2" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="2. Masuk Menu 'Pengajuan Surat' &amp;amp;&lt;br&gt;Pilih Jenis Surat yang Diperlukan" vertex="1">
                    <mxGeometry height="52" width="280" x="190" y="295" as="geometry" />
                </mxCell>

                <mxCell id="s_step_3" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="3. Isi Formulir Keperluan &amp;amp;&lt;br&gt;Unggah Dokumen Syarat (PDF &amp;le; 2MB)" vertex="1">
                    <mxGeometry height="54" width="280" x="190" y="380" as="geometry" />
                </mxCell>

                <mxCell id="s_step_4" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="4. Klik Tombol 'Kirim Permohonan'" vertex="1">
                    <mxGeometry height="52" width="280" x="190" y="470" as="geometry" />
                </mxCell>

                <mxCell id="s_step_revisi" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="Menerima Catatan Koreksi Revisi &amp;amp;&lt;br&gt;Perbaiki Berkas yang Kurang" vertex="1">
                    <mxGeometry height="54" width="280" x="190" y="950" as="geometry" />
                </mxCell>

                <mxCell id="s_step_unduh" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;fontStyle=1;" value="12. Terima Notifikasi Selesai &amp;amp;&lt;br&gt;Unduh Berkas PDF Surat Resmi" vertex="1">
                    <mxGeometry height="54" width="280" x="190" y="1130" as="geometry" />
                </mxCell>

                <mxCell id="s_end_node" parent="1" style="ellipse;shape=doubleEllipse;html=1;fillColor=#000000;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;" value="" vertex="1">
                    <mxGeometry height="36" width="36" x="312" y="1225" as="geometry" />
                </mxCell>

                <!-- ==================== NODES IN LANE 2: SISTEM (Main x=860..1140, Alert x=600..810) ==================== -->
                <mxCell id="sys_step_val" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="5. Validasi Kelengkapan Formulir &amp;amp;&lt;br&gt;Format / Ukuran File Dokumen" vertex="1">
                    <mxGeometry height="52" width="280" x="860" y="470" as="geometry" />
                </mxCell>

                <mxCell id="sys_dec_file" parent="1" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=11.5;fontStyle=1;" value="Form Lengkap&lt;br&gt;&amp;amp; File &amp;le; 2MB?" vertex="1">
                    <mxGeometry height="70" width="180" x="910" y="565" as="geometry" />
                </mxCell>

                <mxCell id="sys_err_alert" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=11;" value="Peringatan Validasi:&lt;br&gt;'File &amp;gt; 2MB / Form Kosong'" vertex="1">
                    <mxGeometry height="52" width="210" x="600" y="574" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_save" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="6. Simpan Database (Status: DIAJUKAN)&lt;br&gt;&amp;amp; Terbitkan Nomor Resi Tiket Unik" vertex="1">
                    <mxGeometry height="52" width="280" x="860" y="680" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_forward" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="7. Teruskan Berkas ke Meja Antrean TU" vertex="1">
                    <mxGeometry height="52" width="280" x="860" y="765" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_rej" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=12;" value="UPDATE Status: 'DITOLAK_PERLU_REVISI'&lt;br&gt;&amp;amp; Kirim Notifikasi Koreksi ke Siswa" vertex="1">
                    <mxGeometry height="54" width="280" x="860" y="950" as="geometry" />
                </mxCell>

                <mxCell id="sys_step_compile" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;fontStyle=1;" value="11. Kompilasi Kop Sekolah, Data &amp;amp; QR Code&lt;br&gt;ke File PDF (Status: SELESAI)" vertex="1">
                    <mxGeometry height="54" width="280" x="860" y="1130" as="geometry" />
                </mxCell>

                <!-- ==================== NODES IN LANE 3: PETUGAS TU & KEPSEK (x=1190..1750) ==================== -->
                <mxCell id="p_step_review" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="8. Login ke Panel TU, Buka Antrean&lt;br&gt;&amp;amp; Tinjau Berkas Dokumen Siswa" vertex="1">
                    <mxGeometry height="52" width="280" x="1330" y="765" as="geometry" />
                </mxCell>

                <mxCell id="p_dec_valid" parent="1" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=11.5;fontStyle=1;" value="Berkas Lengkap&lt;br&gt;&amp;amp; Sah?" vertex="1">
                    <mxGeometry height="68" width="180" x="1380" y="845" as="geometry" />
                </mxCell>

                <mxCell id="p_step_rej" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=11.5;" value="9A. Input Alasan Koreksi &amp;amp;&lt;br&gt;Klik 'Tolak &amp;amp; Minta Revisi'" vertex="1">
                    <mxGeometry height="54" width="210" x="1210" y="950" as="geometry" />
                </mxCell>

                <mxCell id="p_step_app" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=11.5;" value="9B. Input No. Agenda TU &amp;amp;&lt;br&gt;Teruskan ke Kepsek" vertex="1">
                    <mxGeometry height="54" width="220" x="1505" y="950" as="geometry" />
                </mxCell>

                <mxCell id="p_step_sign" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;fontStyle=1;" value="10. Kepsek Menyetujui, Generate No. Surat&lt;br&gt;Resmi &amp;amp; Bubuhkan TTE Kode QR" vertex="1">
                    <mxGeometry height="54" width="280" x="1320" y="1040" as="geometry" />
                </mxCell>

                <!-- ==================== EXPLICIT ORTHOGONAL CONNECTORS (ZERO COLLISION) ==================== -->
                <mxCell id="c_1" edge="1" parent="1" source="act_start" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="s_step_1">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="c_2" edge="1" parent="1" source="s_step_1" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="s_step_2">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="c_3" edge="1" parent="1" source="s_step_2" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="s_step_3">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="c_4" edge="1" parent="1" source="s_step_3" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="s_step_4">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 4 -> 5 (Straight horizontal at y=496) -->
                <mxCell id="c_5" edge="1" parent="1" source="s_step_4" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="sys_step_val">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 5 -> Decision 1 -->
                <mxCell id="c_6" edge="1" parent="1" source="sys_step_val" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="sys_dec_file">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Decision 1 -> Error Alert (Straight horizontal left at y=600) -->
                <mxCell id="c_7" edge="1" parent="1" source="sys_dec_file" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="sys_err_alert" value="[Tidak]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Error Alert -> Step 3 (Inner Highway Track: x=135, turns right early at y=420.5) -->
                <mxCell id="c_8" edge="1" parent="1" source="sys_err_alert" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.6;edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.75;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_3" value="Perbaiki File">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="135" y="600" />
                            <mxPoint x="135" y="420.5" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- Decision 1 -> 6. Simpan DB (Straight vertical down at x=1000) -->
                <mxCell id="c_9" edge="1" parent="1" source="sys_dec_file" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="sys_step_save" value="[Ya / Valid]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 6 -> 7 -->
                <mxCell id="c_10" edge="1" parent="1" source="sys_step_save" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="sys_step_forward">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 7 -> 8 (Straight horizontal at y=791) -->
                <mxCell id="c_11" edge="1" parent="1" source="sys_step_forward" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="p_step_review">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 8 -> Decision 2 -->
                <mxCell id="c_12" edge="1" parent="1" source="p_step_review" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="p_dec_valid">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Decision 2 -> 9A Tolak (Clean L-bend left then down) -->
                <mxCell id="c_13" edge="1" parent="1" source="p_dec_valid" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_step_rej" value="[Tidak]">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1315" y="879" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- 9A Tolak -> Sistem UPDATE Ditolak (Straight horizontal left at y=977) -->
                <mxCell id="c_14" edge="1" parent="1" source="p_step_rej" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="sys_step_rej">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Sistem UPDATE Ditolak -> Siswa Terima Revisi (Straight horizontal left at y=977) -->
                <mxCell id="c_15" edge="1" parent="1" source="sys_step_rej" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="s_step_revisi">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Siswa Revisi -> Step 3 (Outer Highway Track: x=85, wraps above inner track to y=393.5) -->
                <mxCell id="c_16" edge="1" parent="1" source="s_step_revisi" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.6;edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.25;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="s_step_3" value="Upload Ulang">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="85" y="977" />
                            <mxPoint x="85" y="393.5" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- Decision 2 -> 9B Setuju TU (Clean L-bend right then down) -->
                <mxCell id="c_17" edge="1" parent="1" source="p_dec_valid" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_step_app" value="[Ya / Sah]">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1615" y="879" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- 9B -> 10 Kepsek Sign (Clean L-bend down then left) -->
                <mxCell id="c_18" edge="1" parent="1" source="p_step_app" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=1.8;edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="p_step_sign">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1615" y="1067" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- 10 Kepsek Sign -> 11 Sistem Compile PDF (Clean L-bend down then left) -->
                <mxCell id="c_19" edge="1" parent="1" source="p_step_sign" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sys_step_compile">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1460" y="1157" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- 11 Sistem Compile -> 12 Siswa Unduh (Straight horizontal left at y=1157) -->
                <mxCell id="c_20" edge="1" parent="1" source="sys_step_compile" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="s_step_unduh">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- 12 Siswa Unduh -> Final Node (Straight vertical down at x=330) -->
                <mxCell id="c_21" edge="1" parent="1" source="s_step_unduh" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="s_end_node">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>"""

    # TAB 2: SEQUENCE DIAGRAMS (100% Global Coordinates on parent="1", Labels Below Icons)
    tab2_xml = """    <diagram id="sequence-diagrams" name="2. Sequence Diagrams (Pola BCE UNINDRA)">
        <mxGraphModel dx="1600" dy="1400" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1780" pageHeight="1420" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />

                <!-- HEADER BANNER -->
                <mxCell id="seq_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;SEQUENCE DIAGRAMS — SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Format Standar Bahan Ajar RPL UNINDRA (Slide 18-26): Pola Arsitektur Boundary (|O), Control (↺O), Entity (_O_) + Frame Alt&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1680" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- ==================== DIAGRAM 1: PENGAJUAN SURAT (SISWA) ==================== -->
                <mxCell id="box_seq1" parent="1" style="swimlane;startSize=30;fontStyle=1;align=center;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12.5;" value="1. SEQUENCE DIAGRAM: PENGAJUAN SURAT OLEH SISWA (POLA BCE)" vertex="1">
                    <mxGeometry height="600" width="1680" x="50" y="95" as="geometry" />
                </mxCell>

                <!-- LIFELINE ICONS SEQ 1 (verticalLabelPosition=bottom so text is cleanly below icon!) -->
                <mxCell id="act_siswa_seq" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="Siswa&lt;br&gt;(Aktor)" vertex="1">
                    <mxGeometry height="55" width="35" x="192" y="140" as="geometry" />
                </mxCell>

                <mxCell id="bnd_form_seq" parent="1" style="shape=umlBoundary;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="FormPengajuanUI&lt;br&gt;(Boundary)" vertex="1">
                    <mxGeometry height="50" width="60" x="580" y="142" as="geometry" />
                </mxCell>

                <mxCell id="ctrl_surat_seq" parent="1" style="shape=umlControl;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="SuratController&lt;br&gt;(Control)" vertex="1">
                    <mxGeometry height="55" width="50" x="1002" y="140" as="geometry" />
                </mxCell>

                <mxCell id="ent_surat_seq" parent="1" style="shape=umlEntity;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="tb_pengajuan_surat&lt;br&gt;(Entity)" vertex="1">
                    <mxGeometry height="50" width="50" x="1422" y="142" as="geometry" />
                </mxCell>

                <!-- DASHED VERTICAL LIFELINES SEQ 1 (Start at y=238, well below text labels!) -->
                <mxCell id="line_s1_act" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="210" y="238" as="sourcePoint" />
                        <mxPoint x="210" y="675" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s1_bnd" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="238" as="sourcePoint" />
                        <mxPoint x="610" y="675" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s1_ctrl" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1027" y="238" as="sourcePoint" />
                        <mxPoint x="1027" y="675" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s1_ent" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1447" y="238" as="sourcePoint" />
                        <mxPoint x="1447" y="675" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- FRAME ALT SEQ 1 -->
                <mxCell id="frame_alt_s1" parent="1" style="shape=umlFrame;whiteSpace=wrap;html=1;width=175;height=24;fillColor=none;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontSize=11;fontStyle=1;fontColor=#000000;" value="alt [Berkas &amp;le; 2MB &amp;amp; Valid]" vertex="1">
                    <mxGeometry height="245" width="1360" x="150" y="410" as="geometry" />
                </mxCell>

                <mxCell id="alt_line_s1" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.3;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;fontStyle=1;" value="[Else: Berkas &amp;gt; 2MB / Form Kosong]">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="150" y="575" as="sourcePoint" />
                        <mxPoint x="1510" y="575" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- MESSAGES SEQ 1 -->
                <mxCell id="m_s1_1" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="1. bukaMenuPengajuan()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="210" y="265" as="sourcePoint" />
                        <mxPoint x="610" y="265" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s1_2" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="2. tampilkanFormulirSurat()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="305" as="sourcePoint" />
                        <mxPoint x="210" y="305" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s1_3" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="3. submitPermohonan(jenisSurat, keperluan, fileBerkas)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="210" y="345" as="sourcePoint" />
                        <mxPoint x="610" y="345" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s1_4" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="4. validasiPayloadBerkas(fileSize, fileType)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="385" as="sourcePoint" />
                        <mxPoint x="1027" y="385" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s1_5" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="5. insertPengajuan(nisn, jenis, status='DIAJUKAN')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1027" y="455" as="sourcePoint" />
                        <mxPoint x="1447" y="455" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s1_6" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="6. returnRecord(idPengajuan, nomorTiketResi)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1447" y="495" as="sourcePoint" />
                        <mxPoint x="1027" y="495" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s1_7" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="7. tampilkanResiSukses(nomorTiket)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="535" as="sourcePoint" />
                        <mxPoint x="210" y="535" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s1_8" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="8. responseError('Ukuran file melebihi 2MB, silakan unggah ulang')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="625" as="sourcePoint" />
                        <mxPoint x="210" y="625" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- ==================== DIAGRAM 2: VERIFIKASI & APPROVAL (PETUGAS TU) ==================== -->
                <mxCell id="box_seq2" parent="1" style="swimlane;startSize=30;fontStyle=1;align=center;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12.5;" value="2. SEQUENCE DIAGRAM: VERIFIKASI &amp;amp; PENGESAHAN DOKUMEN OLEH PETUGAS TU (POLA BCE)" vertex="1">
                    <mxGeometry height="640" width="1680" x="50" y="720" as="geometry" />
                </mxCell>

                <!-- LIFELINE ICONS SEQ 2 -->
                <mxCell id="act_tu_seq" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="Petugas TU&lt;br&gt;(Aktor)" vertex="1">
                    <mxGeometry height="55" width="35" x="192" y="765" as="geometry" />
                </mxCell>

                <mxCell id="bnd_tu_seq" parent="1" style="shape=umlBoundary;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="VerifikasiTUUI&lt;br&gt;(Boundary)" vertex="1">
                    <mxGeometry height="50" width="60" x="580" y="767" as="geometry" />
                </mxCell>

                <mxCell id="ctrl_tu_seq" parent="1" style="shape=umlControl;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="VerifikasiController&lt;br&gt;(Control)" vertex="1">
                    <mxGeometry height="55" width="50" x="1002" y="765" as="geometry" />
                </mxCell>

                <mxCell id="ent_tu_seq" parent="1" style="shape=umlEntity;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=11.5;labelBackgroundColor=#ffffff;" value="tb_pengajuan_surat&lt;br&gt;(Entity)" vertex="1">
                    <mxGeometry height="50" width="50" x="1422" y="767" as="geometry" />
                </mxCell>

                <!-- DASHED VERTICAL LIFELINES SEQ 2 (Start at y=865, well below text labels!) -->
                <mxCell id="line_s2_act" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="210" y="865" as="sourcePoint" />
                        <mxPoint x="210" y="1340" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s2_bnd" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="865" as="sourcePoint" />
                        <mxPoint x="610" y="1340" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s2_ctrl" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1027" y="865" as="sourcePoint" />
                        <mxPoint x="1027" y="1340" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="line_s2_ent" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.5;" value="">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1447" y="865" as="sourcePoint" />
                        <mxPoint x="1447" y="1340" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- FRAME ALT SEQ 2 -->
                <mxCell id="frame_alt_s2" parent="1" style="shape=umlFrame;whiteSpace=wrap;html=1;width=185;height=24;fillColor=none;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontSize=11;fontStyle=1;fontColor=#000000;" value="alt [Berkas Sah &amp;amp; Disetujui]" vertex="1">
                    <mxGeometry height="295" width="1360" x="150" y="1025" as="geometry" />
                </mxCell>

                <mxCell id="alt_line_s2" edge="1" parent="1" style="endArrow=none;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.3;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;fontStyle=1;" value="[Else: Berkas Buram / Perlu Revisi]">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="150" y="1180" as="sourcePoint" />
                        <mxPoint x="1510" y="1180" as="targetPoint" />
                    </mxGeometry>
                </mxCell>

                <!-- MESSAGES SEQ 2 -->
                <mxCell id="m_s2_1" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="1. bukaAntreanSuratMasuk()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="210" y="890" as="sourcePoint" />
                        <mxPoint x="610" y="890" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_2" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="2. getDaftarPengajuanStatus('DIAJUKAN')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="928" as="sourcePoint" />
                        <mxPoint x="1027" y="928" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_3" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="3. selectQuery(status='DIAJUKAN')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1027" y="965" as="sourcePoint" />
                        <mxPoint x="1447" y="965" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_4" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="4. returnDaftarBerkas()">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1447" y="1002" as="sourcePoint" />
                        <mxPoint x="610" y="1002" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_5" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="5. approvePermohonan(id, nomorAgenda, qrCodeHash)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="210" y="1070" as="sourcePoint" />
                        <mxPoint x="610" y="1070" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_6" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="6. updateStatus(status='SELESAI', noSurat, qrCode)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1027" y="1108" as="sourcePoint" />
                        <mxPoint x="1447" y="1108" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_7" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="7. tampilkanKonfirmasiSukses('Surat resmi berhasil disahkan')">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="1146" as="sourcePoint" />
                        <mxPoint x="210" y="1146" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_8" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="8. tolakPermohonan(id, catatanKoreksi)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="210" y="1225" as="sourcePoint" />
                        <mxPoint x="610" y="1225" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_9" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="9. updateStatus(status='DITOLAK_PERLU_REVISI', catatan)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="1027" y="1263" as="sourcePoint" />
                        <mxPoint x="1447" y="1263" as="targetPoint" />
                    </mxGeometry>
                </mxCell>
                <mxCell id="m_s2_10" edge="1" parent="1" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;labelBackgroundColor=#ffffff;fontSize=11;" value="10. notifikasiCatatanRevisiKeSiswa(idSiswa)">
                    <mxGeometry relative="1" as="geometry">
                        <mxPoint x="610" y="1301" as="sourcePoint" />
                        <mxPoint x="210" y="1301" as="targetPoint" />
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
# 3. TUGAS 5: ULTRA-CLEAR STATE MACHINE DIAGRAM (WIDE GAPS, ZERO COLLISION)
# =========================================================================
def generate_tugas_5_xml():
    xml = """<mxfile host="65bd71144e">
    <diagram id="state-machine-surat" name="State Machine (SuratPengajuan)">
        <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1720" pageHeight="680" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="sm_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;STATE MACHINE DIAGRAM — SIKLUS HIDUP PERMOHONAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Pemodelan UML 2.5 Entitas Dokumen Permohonan (tb_pengajuan_surat) — Kelompok 7 (RPL_XD 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1620" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- START NODE -->
                <mxCell id="sm_init" parent="1" style="ellipse;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#000000;" value="" vertex="1">
                    <mxGeometry height="36" width="36" x="60" y="210" as="geometry" />
                </mxCell>

                <!-- STATE 1: DRAFT -->
                <mxCell id="sm_draft" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;1. DRAFT&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Tampilkan Form Surat&lt;br&gt;do / Input Data &amp;amp; Unggah Berkas&lt;br&gt;exit / Validasi Format Berkas&lt;/div&gt;" vertex="1">
                    <mxGeometry height="96" width="230" x="180" y="180" as="geometry" />
                </mxCell>

                <!-- STATE 2: MENUNGGU VERIFIKASI -->
                <mxCell id="sm_menunggu" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;2. MENUNGGU_VERIFIKASI&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Generate Kode Tiket Resi&lt;br&gt;do / Masuk Antrean Verifikasi TU&lt;br&gt;exit / Notifikasi ke Meja Staf TU&lt;/div&gt;" vertex="1">
                    <mxGeometry height="96" width="240" x="560" y="180" as="geometry" />
                </mxCell>

                <!-- SUB-BRANCH: STATE DITOLAK PERLU REVISI (Directly below State 2) -->
                <mxCell id="sm_revisi" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;DITOLAK_PERLU_REVISI&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Catat Alasan Penolakan&lt;br&gt;do / Siswa Mengunggah Berkas Baru&lt;br&gt;exit / Notifikasi Perbaikan Selesai&lt;/div&gt;" vertex="1">
                    <mxGeometry height="96" width="240" x="560" y="410" as="geometry" />
                </mxCell>

                <!-- STATE 3: DIVERIFIKASI TU -->
                <mxCell id="sm_diverifikasi" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;3. DIVERIFIKASI_TU&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Tetapkan No. Agenda Masuk&lt;br&gt;do / Teruskan ke Meja Kepsek&lt;br&gt;exit / Siap Ditandatangani&lt;/div&gt;" vertex="1">
                    <mxGeometry height="96" width="230" x="950" y="180" as="geometry" />
                </mxCell>

                <!-- STATE 4: DISETUJUI KEPSEK -->
                <mxCell id="sm_disetujui" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;4. DISETUJUI_KEPSEK&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Generate Nomor Surat Keluar&lt;br&gt;do / Terbitkan QR Code Tanda Tangan&lt;br&gt;exit / Render Dokumen PDF Resmi&lt;/div&gt;" vertex="1">
                    <mxGeometry height="96" width="240" x="1330" y="180" as="geometry" />
                </mxCell>

                <!-- STATE 5: SELESAI SIAP UNDUH (Directly below State 4) -->
                <mxCell id="sm_selesai" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.5;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;5. SELESAI_SIAP_UNDUH&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Kirim Notifikasi Surat Terbit&lt;br&gt;do / Layani Unduh File PDF Siswa&lt;br&gt;exit / Catat Riwayat Pengambilan&lt;/div&gt;" vertex="1">
                    <mxGeometry height="96" width="240" x="1330" y="410" as="geometry" />
                </mxCell>

                <!-- STATE 6: DIARSIPKAN (Left of State 5) -->
                <mxCell id="sm_arsip" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=top;spacingTop=6;" value="&lt;b style='font-size:13px;'&gt;6. DIARSIPKAN&lt;/b&gt;&lt;hr style='border:0.5px solid #000000;margin:4px 0;'&gt;&lt;div style='font-size:11px;text-align:left;padding:0 8px;line-height:1.4;'&gt;entry / Kunci Record Data Surat&lt;br&gt;do / Masuk Arsip Statis Sekolah&lt;/div&gt;" vertex="1">
                    <mxGeometry height="96" width="230" x="950" y="410" as="geometry" />
                </mxCell>

                <!-- END NODE -->
                <mxCell id="sm_final" parent="1" style="ellipse;shape=doubleEllipse;html=1;fillColor=#000000;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;" value="" vertex="1">
                    <mxGeometry height="38" width="38" x="835" y="439" as="geometry" />
                </mxCell>

                <!-- ==================== EXPLICIT STRAIGHT TRANSITIONS ==================== -->
                <mxCell id="tr_1" edge="1" parent="1" source="sm_init" style="endArrow=block;endFill=1;html=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;exitY=0.5;entryY=0.5;entryDx=0;entryDy=0;" target="sm_draft" value="Pilih Surat">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="tr_2" edge="1" parent="1" source="sm_draft" style="endArrow=block;endFill=1;html=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="sm_menunggu" value="Kirim Permohonan&lt;br&gt;[Berkas &amp;le; 2MB]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Menunggu -> Revisi (Straight vertical down on right half x=716) -->
                <mxCell id="tr_3" edge="1" parent="1" source="sm_menunggu" style="endArrow=block;endFill=1;html=1;strokeWidth=1.8;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.65;exitY=1;exitDx=0;exitDy=0;entryX=0.65;entryY=0;entryDx=0;entryDy=0;" target="sm_revisi" value="Tolak TU&lt;br&gt;[Berkas Kurang]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Revisi -> Menunggu (Clean loop on left side x=485) -->
                <mxCell id="tr_4" edge="1" parent="1" source="sm_revisi" style="endArrow=block;endFill=1;html=1;strokeWidth=1.8;strokeColor=#000000;edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0.2;entryY=1;entryDx=0;entryDy=0;fontColor=#000000;labelBackgroundColor=#ffffff;" target="sm_menunggu" value="Unggah Ulang&lt;br&gt;[Valid]">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="485" y="458" />
                            <mxPoint x="485" y="340" />
                            <mxPoint x="608" y="340" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <mxCell id="tr_5" edge="1" parent="1" source="sm_menunggu" style="endArrow=block;endFill=1;html=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="sm_diverifikasi" value="Verifikasi TU&lt;br&gt;[Berkas Sah]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="tr_6" edge="1" parent="1" source="sm_diverifikasi" style="endArrow=block;endFill=1;html=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="sm_disetujui" value="Approve Kepsek&lt;br&gt;[Disahkan]">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="tr_7" edge="1" parent="1" source="sm_disetujui" style="endArrow=block;endFill=1;html=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="sm_selesai" value="Kompilasi PDF&lt;br&gt;Berhasil">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="tr_8" edge="1" parent="1" source="sm_selesai" style="endArrow=block;endFill=1;html=1;strokeWidth=1.8;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="sm_arsip" value="Selesai Diunduh /&lt;br&gt;Retensi Aktif">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="tr_9" edge="1" parent="1" source="sm_arsip" style="endArrow=block;endFill=1;html=1;strokeWidth=2;strokeColor=#000000;fontColor=#000000;labelBackgroundColor=#ffffff;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="sm_final" value="Arsip">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""
    return xml


# =========================================================================
# AUTOMATED MATHEMATICAL COLLISION & GEOMETRY AUDITOR
# =========================================================================
def parse_style_float(style, key, default=0.5):
    m = re.search(rf"{key}=([0-9.]+)", style)
    return float(m.group(1)) if m else default

def seg_intersects_box(p1, p2, box):
    # Check if segment p1-p2 passes through interior of box (x1, y1, x2, y2)
    bx1, by1, bx2, by2 = box
    # Shrink box by 2px to ignore grazing touch
    bx1 += 2; by1 += 2; bx2 -= 2; by2 -= 2
    x1, y1 = p1
    x2, y2 = p2
    # Bounding box quick reject
    if max(x1, x2) < bx1 or min(x1, x2) > bx2 or max(y1, y2) < by1 or min(y1, y2) > by2:
        return False
    # Sample 25 points along the segment
    for i in range(1, 25):
        t = i / 25.0
        px = x1 + t * (x2 - x1)
        py = y1 + t * (y2 - y1)
        if bx1 < px < bx2 and by1 < py < by2:
            return True
    return False

def seg_intersects_seg(p1, p2, q1, q2):
    # Check proper intersection between segment p1-p2 and q1-q2
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    # Ignore if they share an endpoint
    for pa in (p1, p2):
        for qa in (q1, q2):
            if abs(pa[0] - qa[0]) < 2 and abs(pa[1] - qa[1]) < 2:
                return False
    return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))

def verify_diagram_geometry(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    errors = []

    for diag in root.findall("diagram"):
        dname = diag.attrib.get("name", "unnamed")
        cells = diag.findall(".//mxCell")

        # 1. Check html=1 on all cells with entities or tags
        for c in cells:
            val = c.attrib.get("value", "")
            style = c.attrib.get("style", "")
            cid = c.attrib.get("id", "")
            if ("&" in val or "<" in val) and "html=1" not in style:
                errors.append(f"[{dname}] Cell '{cid}' has HTML/entities in value but missing html=1 in style!")

        # 2. Check all vertices have parent="1" (no nested coordinate confusion)
        boxes = {}
        containers = {"sys_boundary", "lane_siswa", "lane_sistem", "lane_petugas", "box_seq1", "box_seq2", "frame_alt_s1", "frame_alt_s2"}
        for c in cells:
            if c.attrib.get("vertex") == "1":
                cid = c.attrib.get("id")
                parent = c.attrib.get("parent")
                if parent != "1":
                    errors.append(f"[{dname}] Vertex '{cid}' has nested parent='{parent}' instead of '1'!")
                geom = c.find("mxGeometry")
                if geom is not None:
                    x = float(geom.attrib.get("x", 0))
                    y = float(geom.attrib.get("y", 0))
                    w = float(geom.attrib.get("width", 0))
                    h = float(geom.attrib.get("height", 0))
                    boxes[cid] = (x, y, x + w, y + h)

        # 3. Check Box-to-Box Overlap (excluding background containers)
        non_container_ids = [k for k in boxes if k not in containers]
        for i in range(len(non_container_ids)):
            for j in range(i + 1, len(non_container_ids)):
                id1, id2 = non_container_ids[i], non_container_ids[j]
                x1, y1, x2, y2 = boxes[id1]
                ax1, ay1, ax2, ay2 = boxes[id2]
                if not (x2 + 8 <= ax1 or ax2 + 8 <= x1 or y2 + 8 <= ay1 or ay2 + 8 <= y1):
                    errors.append(f"[{dname}] BOX OVERLAP: '{id1}' {boxes[id1]} overlaps with '{id2}' {boxes[id2]}!")

        # 4. Check Edge-to-Box and Edge-to-Edge Collisions (for connected graph edges)
        edge_segments = []
        for c in cells:
            if c.attrib.get("edge") == "1":
                cid = c.attrib.get("id")
                src = c.attrib.get("source")
                tgt = c.attrib.get("target")
                style = c.attrib.get("style", "")
                if src in boxes and tgt in boxes:
                    sx1, sy1, sx2, sy2 = boxes[src]
                    tx1, ty1, tx2, ty2 = boxes[tgt]
                    ex_x = parse_style_float(style, "exitX", 0.5)
                    ex_y = parse_style_float(style, "exitY", 0.5)
                    en_x = parse_style_float(style, "entryX", 0.5)
                    en_y = parse_style_float(style, "entryY", 0.5)
                    p_start = (sx1 + ex_x * (sx2 - sx1), sy1 + ex_y * (sy2 - sy1))
                    p_end = (tx1 + en_x * (tx2 - tx1), ty1 + en_y * (ty2 - ty1))
                    pts = [p_start]
                    geom = c.find("mxGeometry")
                    if geom is not None:
                        arr = geom.find("Array")
                        if arr is not None:
                            for mp in arr.findall("mxPoint"):
                                pts.append((float(mp.attrib.get("x", 0)), float(mp.attrib.get("y", 0))))
                    pts.append(p_end)
                    for k in range(len(pts) - 1):
                        seg = (pts[k], pts[k + 1])
                        edge_segments.append((cid, src, tgt, seg))
                        # Check against all non-container boxes
                        for bid in non_container_ids:
                            if bid not in (src, tgt):
                                if seg_intersects_box(seg[0], seg[1], boxes[bid]):
                                    errors.append(f"[{dname}] LINE-TO-BOX COLLISION: Edge '{cid}' segment {seg} cuts through box '{bid}' {boxes[bid]}!")

        # Check Edge-to-Edge crossings
        for i in range(len(edge_segments)):
            for j in range(i + 1, len(edge_segments)):
                cid1, s1, t1, seg1 = edge_segments[i]
                cid2, s2, t2, seg2 = edge_segments[j]
                if cid1 != cid2:
                    if seg_intersects_seg(seg1[0], seg1[1], seg2[0], seg2[1]):
                        errors.append(f"[{dname}] LINE-TO-LINE CROSSING: Edge '{cid1}' {seg1} crosses Edge '{cid2}' {seg2}!")

    return errors


if __name__ == "__main__":
    files = {
        "tugas-3-usecase.drawio": generate_tugas_3_xml(),
        "tugas-4-activity-sequence.drawio": generate_tugas_4_xml(),
        "tugas-5-state-machine.drawio": generate_tugas_5_xml(),
    }

    for fname, content in files.items():
        fpath = os.path.join(RPL_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        errs = verify_diagram_geometry(fpath)
        if errs:
            print(f"[FAIL] {fname} has {len(errs)} geometry errors:")
            for e in errs:
                print("  -", e)
        else:
            print(f"[PASS 100%] {fname}: 0 box overlaps, 0 line-to-box collisions, 0 line-to-line crossings, 0 missing html=1 tags!")
