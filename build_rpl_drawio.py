import os
import re

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"
MASTER_DRAWIO = os.path.join(RPL_DIR, "use-case-siswa-admin.drawio")

with open(MASTER_DRAWIO, "r", encoding="utf-8") as f:
    master_content = f.read()

diagram_pattern = re.compile(r'<diagram\b[^>]*>.*?</diagram>', re.DOTALL)
diagrams = diagram_pattern.findall(master_content)

print(f"Total diagram tabs found in master: {len(diagrams)}")
tabs = {}
for d in diagrams:
    m = re.search(r'id="([^"]+)"', d)
    diag_id = m.group(1) if m else "unknown"
    tabs[diag_id] = d
    m_name = re.search(r'name="([^"]+)"', d)
    name = m_name.group(1) if m_name else "Unnamed"
    print(f" - ID: {diag_id} | Name: {name}")

# =========================================================================
# FILE 1: TUGAS 3 - USE CASE DIAGRAM
# =========================================================================
tugas_3_content = f"""<mxfile host="65bd71144e">
{tabs.get("usecase-siswa-admin", "")}
{tabs.get("rbac-matrix", "")}
</mxfile>
"""

tugas_3_path = os.path.join(RPL_DIR, "tugas-3-usecase.drawio")
with open(tugas_3_path, "w", encoding="utf-8") as f:
    f.write(tugas_3_content.strip() + "\n")
print(f"[OK] Generated: {tugas_3_path}")

# =========================================================================
# FILE 2: TUGAS 4 - ACTIVITY & SEQUENCE DIAGRAM
# =========================================================================
tugas_4_content = f"""<mxfile host="65bd71144e">
{tabs.get("tabel-simbol-unindra", "")}
{tabs.get("act-role-siswa", "")}
{tabs.get("act-role-petugas", "")}
{tabs.get("act-siswa-petugas", "")}
{tabs.get("sequence-diagrams", "")}
</mxfile>
"""

tugas_4_path = os.path.join(RPL_DIR, "tugas-4-activity-sequence.drawio")
with open(tugas_4_path, "w", encoding="utf-8") as f:
    f.write(tugas_4_content.strip() + "\n")
print(f"[OK] Generated: {tugas_4_path}")

# =========================================================================
# FILE 3: TUGAS 5 - STATE MACHINE DIAGRAM
# =========================================================================
# Let's construct a dedicated Draw.io XML for State Machine diagrams
state_machine_tab1_xml = """    <diagram id="state-machine-surat" name="1. State Machine (SuratPengajuan)">
        <mxGraphModel dx="1800" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="1400" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="sm_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0f172a;strokeColor=#38bdf8;fontColor=#f8fafc;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;🔄 STATE MACHINE DIAGRAM 1: SIKLUS HIDUP PERMOHONAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#94a3b8;'&gt;Pemodelan UML 2.5 Entitas Dokumen Permohonan (tb_pengajuan_surat) — Kelompok 7 (RPL_XD 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="60" width="1900" x="50" y="20" as="geometry"/>
                </mxCell>
                
                <mxCell id="sm_init" parent="1" style="ellipse;fillColor=#000000;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="35" width="35" x="80" y="250" as="geometry"/>
                </mxCell>
                
                <mxCell id="sm_draft" parent="1" style="swimlane;rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#3b82f6;strokeWidth=2;fontColor=#1e3a8a;fontSize=12;fontStyle=1;startSize=28;" value="STATE: DRAFT (Siswa Mengisi Permohonan)" vertex="1">
                    <mxGeometry height="220" width="360" x="180" y="160" as="geometry"/>
                </mxCell>
                <mxCell id="sub_d1" parent="sm_draft" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e0f2fe;strokeColor=#0284c7;fontColor=#0369a1;fontSize=11;fontStyle=1;" value="entry / renderFormPengajuan()&#xa;do / validasiInputSiswa()&#xa;exit / lockInitialDraft()" vertex="1">
                    <mxGeometry height="140" width="300" x="30" y="45" as="geometry"/>
                </mxCell>

                <mxCell id="sm_menunggu" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fefce8;strokeColor=#eab308;strokeWidth=2;fontColor=#854d0e;fontSize=12;fontStyle=1;" value="STATE: MENUNGGU_VERIFIKASI&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#713f12;'&gt;entry / generateTicketCode()&#xa;entry / notifyTataUsahaQueue()&#xa;do / listenCancellation()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="260" x="630" y="225" as="geometry"/>
                </mxCell>

                <mxCell id="sm_revisi" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#ef4444;strokeWidth=2;fontColor=#991b1b;fontSize=12;fontStyle=1;" value="STATE: DITOLAK_PERLU_REVISI&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#7f1d1d;'&gt;entry / recordCatatanPenolakan()&#xa;entry / notifySiswaRevisi()&#xa;do / awaitReuploadFile()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="260" x="630" y="420" as="geometry"/>
                </mxCell>

                <mxCell id="sm_diverifikasi" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=2;fontColor=#1e40af;fontSize=12;fontStyle=1;" value="STATE: DIVERIFIKASI_TU&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#1e3a8a;'&gt;entry / setNomorAgendaMasuk()&#xa;entry / forwardToKepsekQueue()&#xa;do / monitorApprovalTimeout()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="260" x="980" y="225" as="geometry"/>
                </mxCell>

                <mxCell id="sm_disetujui" parent="1" style="swimlane;rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=2;fontColor=#14532d;fontSize=12;fontStyle=1;startSize=28;" value="STATE: DISETUJUI_KEPSEK (Pengesahan Digital)" vertex="1">
                    <mxGeometry height="220" width="380" x="1330" y="160" as="geometry"/>
                </mxCell>
                <mxCell id="sub_app1" parent="sm_disetujui" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dcfce7;strokeColor=#22c55e;fontColor=#15803d;fontSize=11;fontStyle=1;" value="1. GenerateNomorSuratResmi()&#xa;2. GenerateQRCodeSecurityHash()&#xa;3. KompilasiStreamPDFWithWatermark()" vertex="1">
                    <mxGeometry height="140" width="320" x="30" y="45" as="geometry"/>
                </mxCell>

                <mxCell id="sm_selesai" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ecfdf5;strokeColor=#10b981;strokeWidth=2.5;fontColor=#065f46;fontSize=12;fontStyle=1;" value="STATE: SELESAI_SIAP_UNDUH&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#047857;'&gt;entry / notifySiswaSuratTerbit()&#xa;do / serveDownloadPDF()&#xa;exit / logUnduhActivity()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="260" x="1390" y="480" as="geometry"/>
                </mxCell>

                <mxCell id="sm_arsip" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=2;fontColor=#334155;fontSize=12;fontStyle=1;" value="STATE: DIARSIPKAN&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#475569;'&gt;entry / freezeDatabaseRecord()&#xa;entry / moveToPermanentArchive()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="240" x="1000" y="480" as="geometry"/>
                </mxCell>

                <mxCell id="sm_final" parent="1" style="ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=#ffffff;strokeWidth=3;" value="" vertex="1">
                    <mxGeometry height="35" width="35" x="870" y="507" as="geometry"/>
                </mxCell>

                <!-- Transitions -->
                <mxCell id="tr_init" edge="1" parent="1" source="sm_init" target="sm_draft" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#0284c7;" value="openMenuPengajuan()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_submit" edge="1" parent="1" source="sm_draft" target="sm_menunggu" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#16a34a;" value="submitPermohonan()&#xa;[berkas_valid == true]&#xa;/ generateTicketCode()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_reject_tu" edge="1" parent="1" source="sm_menunggu" target="sm_revisi" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#dc2626;" value="rejectTU() [berkas_kurang]&#xa;/ setCatatanRevisi()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_reupload" edge="1" parent="1" source="sm_revisi" target="sm_menunggu" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#0284c7;edgeStyle=orthogonalEdgeStyle;entryX=0.25;entryY=1;entryDx=0;entryDy=0;" value="reuploadBerkas()&#xa;[file_size &lt;= 2MB]">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_approve_tu" edge="1" parent="1" source="sm_menunggu" target="sm_diverifikasi" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#2563eb;" value="approveTU()&#xa;[berkas_lengkap]&#xa;/ setNoAgenda()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_approve_kepsek" edge="1" parent="1" source="sm_diverifikasi" target="sm_disetujui" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#16a34a;" value="approveKepsek()&#xa;[evaluasi_disetujui]&#xa;/ createQR_TTE()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_compile" edge="1" parent="1" source="sm_disetujui" target="sm_selesai" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#10b981;" value="autoGeneratePDF()&#xa;[pdf_compiled == true]">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_unduh" edge="1" parent="1" source="sm_selesai" target="sm_arsip" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#64748b;" value="unduhSurat() / retentionExpired">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_term" edge="1" parent="1" source="sm_arsip" target="sm_final" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;" value="purgeRetention()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>"""

state_machine_tab2_xml = """    <diagram id="state-machine-auth" name="2. State Machine (UserSession RBAC)">
        <mxGraphModel dx="1800" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="1400" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="auth_header" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0f172a;strokeColor=#818cf8;fontColor=#f8fafc;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;🔐 STATE MACHINE DIAGRAM 2: SIKLUS SESI AUTENTIKASI PENGGUNA (RBAC JWT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#94a3b8;'&gt;Pemodelan UML 2.5 Siklus Hidup Sesi Pengguna Multi-Role — Kelompok 7 (SIPESAT 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="60" width="1900" x="50" y="20" as="geometry"/>
                </mxCell>
                
                <mxCell id="auth_init" parent="1" style="ellipse;fillColor=#000000;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="35" width="35" x="80" y="250" as="geometry"/>
                </mxCell>

                <mxCell id="st_anon" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=2;fontColor=#334155;fontSize=12;fontStyle=1;" value="STATE: ANONYMOUS (Tamu)&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#475569;'&gt;entry / blockProtectedRoutes()&#xa;do / serveLandingPage()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="240" x="180" y="222" as="geometry"/>
                </mxCell>

                <mxCell id="st_authenticating" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fefce8;strokeColor=#eab308;strokeWidth=2;fontColor=#854d0e;fontSize=12;fontStyle=1;" value="STATE: AUTHENTICATING&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#713f12;'&gt;entry / checkRateLimit()&#xa;do / verifyBcryptHash()&#xa;exit / generateJWTToken()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="240" x="520" y="222" as="geometry"/>
                </mxCell>

                <mxCell id="st_active_session" parent="1" style="swimlane;rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=2;fontColor=#14532d;fontSize=12;fontStyle=1;startSize=28;" value="STATE: AUTHENTICATED_SESSION (Peran Terverifikasi)" vertex="1">
                    <mxGeometry height="280" width="450" x="870" y="130" as="geometry"/>
                </mxCell>
                <mxCell id="role_siswa" parent="st_active_session" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e0f2fe;strokeColor=#0284c7;fontColor=#0369a1;fontSize=11;fontStyle=1;" value="Substate: SiswaSession&#xa;Hak: Form Pengajuan, Tracking, Unduh PDF" vertex="1">
                    <mxGeometry height="55" width="390" x="30" y="45" as="geometry"/>
                </mxCell>
                <mxCell id="role_tu" parent="st_active_session" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ede9fe;strokeColor=#6366f1;fontColor=#4338ca;fontSize=11;fontStyle=1;" value="Substate: StafTUSession&#xa;Hak: Verifikasi Berkas, Penomoran Agenda, Laporan" vertex="1">
                    <mxGeometry height="55" width="390" x="30" y="120" as="geometry"/>
                </mxCell>
                <mxCell id="role_kepsek" parent="st_active_session" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fae8ff;strokeColor=#c026d3;fontColor=#86198f;fontSize=11;fontStyle=1;" value="Substate: KepsekSession&#xa;Hak: Disposisi Approval, Pengesahan QR TTE" vertex="1">
                    <mxGeometry height="55" width="390" x="30" y="195" as="geometry"/>
                </mxCell>

                <mxCell id="st_expired" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#ef4444;strokeWidth=2;fontColor=#991b1b;fontSize=12;fontStyle=1;" value="STATE: TOKEN_EXPIRED&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#7f1d1d;'&gt;entry / promptRefreshToken()&#xa;do / countdownAutoLogout(60s)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="240" x="1420" y="225" as="geometry"/>
                </mxCell>

                <mxCell id="st_term" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=2;fontColor=#334155;fontSize=12;fontStyle=1;" value="STATE: TERMINATED&#xa;&lt;span style='font-size:10px;font-weight:normal;color:#475569;'&gt;entry / clearHttpOnlyCookie()&#xa;entry / invalidateTokenBlacklist()&lt;/span&gt;" vertex="1">
                    <mxGeometry height="90" width="240" x="1140" y="470" as="geometry"/>
                </mxCell>

                <mxCell id="auth_final" parent="1" style="ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=#ffffff;strokeWidth=3;" value="" vertex="1">
                    <mxGeometry height="35" width="35" x="1000" y="497" as="geometry"/>
                </mxCell>

                <!-- Transitions -->
                <mxCell id="tr_a_init" edge="1" parent="1" source="auth_init" target="st_anon" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#64748b;" value="accessWeb()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_a_login" edge="1" parent="1" source="st_anon" target="st_authenticating" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#0284c7;" value="submitLoginForm(user, pass)">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_a_fail" edge="1" parent="1" source="st_authenticating" target="st_anon" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#dc2626;edgeStyle=orthogonalEdgeStyle;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" value="[invalid_credentials] / showToastError()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_a_success" edge="1" parent="1" source="st_authenticating" target="st_active_session" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#16a34a;" value="[credentials_valid] / grantSession()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_a_timeout" edge="1" parent="1" source="st_active_session" target="st_expired" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#ef4444;" value="jwtTokenExpires() / trigger401()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_a_refresh" edge="1" parent="1" source="st_expired" target="st_active_session" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#16a34a;edgeStyle=orthogonalEdgeStyle;entryX=0.75;entryY=1;entryDx=0;entryDy=0;" value="refreshToken() [valid_refresh_token]">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_a_logout" edge="1" parent="1" source="st_active_session" target="st_term" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#dc2626;" value="clickLogout() / expireSession()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>

                <mxCell id="tr_a_end" edge="1" parent="1" source="st_term" target="auth_final" style="endArrow=block;endFill=1;strokeWidth=2;strokeColor=#000000;" value="sessionDestroyed()">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>"""

tugas_5_drawio_content = f"""<mxfile host="65bd71144e">
{state_machine_tab1_xml}
{state_machine_tab2_xml}
</mxfile>
"""

tugas_5_drawio_path = os.path.join(RPL_DIR, "tugas-5-state-machine.drawio")
with open(tugas_5_drawio_path, "w", encoding="utf-8") as f:
    f.write(tugas_5_drawio_content.strip() + "\n")
print(f"[OK] Generated: {tugas_5_drawio_path}")
