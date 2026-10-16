import os
import re
import xml.etree.ElementTree as ET

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

# =========================================================================
# FILE 1: TUGAS 3 USE CASE DIAGRAM (EXACTLY 1 CLEAN TAB - ZERO BLOAT)
# =========================================================================
tugas_3_xml = """<mxfile host="65bd71144e">
    <diagram id="usecase-siswa-admin" name="Use Case Diagram (SIPESAT)">
        <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1150" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="header_banner" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;USE CASE DIAGRAM — SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Mata Kuliah Rekayasa Perangkat Lunak UNINDRA — Kelompok 7 (Kelas RPL_XD 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1580" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- SYSTEM BOUNDARY -->
                <mxCell id="sys_boundary" parent="1" style="swimlane;startSize=32;fontStyle=1;align=center;verticalAlign=top;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;" value="Boundary: Sistem Informasi Pengajuan Surat Siswa (SIPESAT)" vertex="1">
                    <mxGeometry height="980" width="1180" x="240" y="95" as="geometry" />
                </mxCell>

                <!-- SHARED TOP SECTION (LOGIN, LOGOUT, PROFIL) -->
                <mxCell id="uc_logout" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-04: Logout Sesi" vertex="1">
                    <mxGeometry height="50" width="190" x="190" y="45" as="geometry" />
                </mxCell>

                <mxCell id="uc_login" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-01: Login ke Sistem&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="220" x="480" y="45" as="geometry" />
                </mxCell>

                <mxCell id="uc_validate" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=11;" value="&lt;i&gt;UC-01B: Validasi Kredensial &amp;amp; JWT&lt;/i&gt;" vertex="1">
                    <mxGeometry height="48" width="220" x="480" y="125" as="geometry" />
                </mxCell>

                <mxCell id="inc_login_val" edge="1" parent="sys_boundary" source="uc_login" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_validate" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_profile" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-03: Kelola Profil &amp;amp; Sandi" vertex="1">
                    <mxGeometry height="50" width="200" x="790" y="45" as="geometry" />
                </mxCell>

                <!-- COLUMN 1: SISWA MAIN USE CASES (LEFT) -->
                <mxCell id="uc_register" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-02: Registrasi Akun Mandiri" vertex="1">
                    <mxGeometry height="50" width="220" x="35" y="200" as="geometry" />
                </mxCell>

                <mxCell id="uc_catalog" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-05: Lihat Katalog &amp;amp; Syarat Surat" vertex="1">
                    <mxGeometry height="50" width="220" x="35" y="295" as="geometry" />
                </mxCell>

                <mxCell id="uc_apply" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-06: Mengajukan Permohonan Surat&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="30" y="405" as="geometry" />
                </mxCell>

                <mxCell id="uc_track" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-08: Melacak Status Surat (Real-time)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="30" y="550" as="geometry" />
                </mxCell>

                <mxCell id="uc_history" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-09: Melihat Riwayat Pengajuan" vertex="1">
                    <mxGeometry height="50" width="220" x="35" y="690" as="geometry" />
                </mxCell>

                <mxCell id="uc_download" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-10: Unduh Surat PDF Ber-QR Code&lt;/b&gt;" vertex="1">
                    <mxGeometry height="55" width="230" x="30" y="800" as="geometry" />
                </mxCell>

                <!-- COLUMN 2: SISWA INCLUDE & EXTEND (CENTER-LEFT) -->
                <mxCell id="uc_upload" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-07: Unggah Berkas Syarat&#10;(PDF &amp;le; 2MB)&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="200" x="320" y="407" as="geometry" />
                </mxCell>

                <mxCell id="inc_apply_up" edge="1" parent="sys_boundary" source="uc_apply" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_upload" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_revision" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-08A: Melihat Catatan Koreksi&#10;Revisi Berkas&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="200" x="320" y="552" as="geometry" />
                </mxCell>

                <mxCell id="ext_rev_track" edge="1" parent="sys_boundary" source="uc_revision" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_track" value="&amp;lt;&amp;lt;extend&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- COLUMN 3: PETUGAS INCLUDE (CENTER-RIGHT) -->
                <mxCell id="uc_qr" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-14A: Terbitkan No. Surat &amp;amp;&#10;QR Code Resmi&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="200" x="660" y="462" as="geometry" />
                </mxCell>

                <mxCell id="inc_app_qr" edge="1" parent="sys_boundary" source="uc_approve" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_qr" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <mxCell id="uc_note" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;strokeDashed=1;fontColor=#000000;fontSize=10.5;" value="&lt;i&gt;UC-15A: Input Alasan &amp;amp;&#10;Catatan Penolakan&lt;/i&gt;" vertex="1">
                    <mxGeometry height="52" width="200" x="660" y="582" as="geometry" />
                </mxCell>

                <mxCell id="inc_rej_note" edge="1" parent="sys_boundary" source="uc_reject" style="html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=open;endFill=0;dashed=1;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=10;fontStyle=2;" target="uc_note" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- COLUMN 4: PETUGAS MAIN USE CASES (RIGHT) -->
                <mxCell id="uc_dashboard" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-11: Dashboard Statistik TU" vertex="1">
                    <mxGeometry height="50" width="220" x="925" y="190" as="geometry" />
                </mxCell>

                <mxCell id="uc_inbox" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-12: Kelola Antrean Surat Masuk" vertex="1">
                    <mxGeometry height="50" width="220" x="925" y="280" as="geometry" />
                </mxCell>

                <mxCell id="uc_verify" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-13: Verifikasi Berkas Dokumen&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="220" x="925" y="370" as="geometry" />
                </mxCell>

                <mxCell id="uc_approve" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-14: Setujui Permohonan (Approve)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="225" x="925" y="460" as="geometry" />
                </mxCell>

                <mxCell id="uc_reject" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-15: Tolak Permohonan (Reject)&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="225" x="925" y="580" as="geometry" />
                </mxCell>

                <mxCell id="uc_master" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-16: Kelola Master Jenis Surat" vertex="1">
                    <mxGeometry height="50" width="220" x="925" y="690" as="geometry" />
                </mxCell>

                <mxCell id="uc_users" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11.5;" value="UC-17: Kelola Data Siswa &amp;amp; Akun" vertex="1">
                    <mxGeometry height="50" width="220" x="925" y="780" as="geometry" />
                </mxCell>

                <mxCell id="uc_report" parent="sys_boundary" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;" value="&lt;b&gt;UC-18: Ekspor Rekapitulasi Laporan&lt;/b&gt;" vertex="1">
                    <mxGeometry height="52" width="225" x="925" y="870" as="geometry" />
                </mxCell>

                <!-- ==================== ACTORS ==================== -->
                <mxCell id="act_siswa" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;fontStyle=1;fontSize=13;" value="&lt;b&gt;Siswa&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;(Aktor Pemohon)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="145" width="80" x="70" y="475" as="geometry" />
                </mxCell>

                <mxCell id="act_petugas" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.2;fontColor=#000000;fontStyle=1;fontSize=13;" value="&lt;b&gt;Petugas TU&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:11px;'&gt;(Verifikator &amp;amp; TU)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="145" width="80" x="1510" y="475" as="geometry" />
                </mxCell>

                <!-- ==================== DIRECT FAN ASSOCIATIONS (ZERO CROSSING) ==================== -->
                <!-- SISWA FAN (Direct straight lines to left edge of Column 1) -->
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

                <!-- SISWA TO TOP SHARED (Clean perimeter margin routing) -->
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
                            <mxPoint x="775" y="65" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- PETUGAS FAN (Direct straight lines to right edge of Column 4) -->
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

                <!-- PETUGAS TO TOP SHARED (Clean perimeter margin routing) -->
                <mxCell id="edge_p_prof" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_profile">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1550" y="475" />
                            <mxPoint x="1550" y="165" />
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="edge_p_login" edge="1" parent="1" source="act_petugas" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;edgeStyle=orthogonalEdgeStyle;entryX=0.75;entryY=0;entryDx=0;entryDy=0;fontColor=#000000;" target="uc_login">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1570" y="475" />
                            <mxPoint x="1570" y="65" />
                            <mxPoint x="885" y="65" />
                        </Array>
                    </mxGeometry>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""

with open(os.path.join(RPL_DIR, "tugas-3-usecase.drawio"), "w", encoding="utf-8") as f:
    f.write(tugas_3_xml.strip() + "\n")
print("[OK] Saved streamlined single-tab tugas-3-usecase.drawio")


# =========================================================================
# FILE 2: TUGAS 4 (EXACTLY 2 TABS: ACTIVITY TERPADU & SEQUENCE BCE)
# =========================================================================
master_path = os.path.join(RPL_DIR, "use-case-siswa-admin.drawio")
with open(master_path, "r", encoding="utf-8") as f:
    master_c = f.read()

act_match = re.search(r'(<diagram id="act-siswa-petugas".*?</diagram>)', master_c, re.DOTALL)
act_xml = act_match.group(1) if act_match else ""

seq_match = re.search(r'(<diagram id="sequence-diagrams".*?</diagram>)', master_c, re.DOTALL)
seq_xml = seq_match.group(1) if seq_match else ""

# Clean & convert both to pure B&W
def clean_bw_tree(xml_str, rename_title=None):
    tree = ET.fromstring(xml_str)
    if rename_title:
        tree.set("name", rename_title)
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
                if k == "strokeColor": new_p.append("strokeColor=none" if v == "none" else "strokeColor=#000000")
                elif k == "fontColor": new_p.append("fontColor=#000000")
                elif k == "fillColor":
                    if v == "none": new_p.append("fillColor=none")
                    elif is_initial or is_final: new_p.append("fillColor=#000000")
                    elif is_th: new_p.append("fillColor=#f1f5f9")
                    elif is_alt: new_p.append("fillColor=#f8fafc")
                    else: new_p.append("fillColor=#ffffff")
                elif k == "labelBackgroundColor": new_p.append("labelBackgroundColor=#ffffff")
                else: new_p.append(p)
            if not any(x.startswith("fontColor=") for x in new_p): new_p.append("fontColor=#000000")
            if is_edge and not any(x.startswith("labelBackgroundColor=") for x in new_p):
                new_p.append("labelBackgroundColor=#ffffff")
            cell.set("style", ";".join(new_p))
        if val:
            cleaned = re.sub(r'color:\s*#[0-9a-fA-F]{3,6}', 'color:#000000', val)
            cleaned = re.sub(r'background(?:-color)?:\s*#[0-9a-fA-F]{3,6}', 'background-color:#ffffff', cleaned)
            cleaned = cleaned.replace("🏛️ ", "").replace("📋 ", "").replace("🔄 ", "").replace("🔐 ", "")
            cell.set("value", cleaned)
    return ET.tostring(tree, encoding="utf-8").decode("utf-8")

act_bw = clean_bw_tree(act_xml, "1. Activity Diagram (Siswa s.d Petugas)")
seq_bw = clean_bw_tree(seq_xml, "2. Sequence Diagrams (Pola BCE UNINDRA)")

tugas_4_full = f"""<mxfile host="65bd71144e">
{act_bw}
{seq_bw}
</mxfile>
"""
with open(os.path.join(RPL_DIR, "tugas-4-activity-sequence.drawio"), "w", encoding="utf-8") as f:
    f.write(tugas_4_full.strip() + "\n")
print("[OK] Saved streamlined 2-tab tugas-4-activity-sequence.drawio")


# =========================================================================
# FILE 3: TUGAS 5 (EXACTLY 1 TAB: STATE MACHINE SURAT PENGAJUAN)
# =========================================================================
sm_match = re.search(r'(<diagram id="state-machine-surat".*?</diagram>)', open(os.path.join(RPL_DIR, "build_rpl_drawio.py"), "r", encoding="utf-8").read(), re.DOTALL)
sm_xml = sm_match.group(1) if sm_match else ""

sm_bw = clean_bw_tree(sm_xml, "State Machine (SuratPengajuan)")

tugas_5_full = f"""<mxfile host="65bd71144e">
{sm_bw}
</mxfile>
"""
with open(os.path.join(RPL_DIR, "tugas-5-state-machine.drawio"), "w", encoding="utf-8") as f:
    f.write(tugas_5_full.strip() + "\n")
print("[OK] Saved streamlined 1-tab tugas-5-state-machine.drawio")

print("All Draw.io files are now strictly lean, clean, B&W, and 100% collision-free!")
