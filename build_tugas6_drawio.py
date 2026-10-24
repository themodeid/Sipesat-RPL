import os

drawio_content = """<mxfile host="65bd71144e">
    <diagram id="class-diagram-sipesat" name="1. Class Diagram (SIPESAT)">
        <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1100" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />
                
                <!-- HEADER BANNER -->
                <mxCell id="hdr_class" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;CLASS DIAGRAM — SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Pemodelan UML 2.5 Struktur Statis, Enkapsulasi, Relasi &amp;amp; Multiplisitas — Kelompok 7 (RPL_XD UNINDRA 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1600" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- SUPERCLASS: PENGGUNA -->
                <mxCell id="cls_pengguna" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="&amp;laquo;Abstract&amp;raquo;&#xa;Pengguna" vertex="1">
                    <mxGeometry x="680" y="100" width="240" height="150" as="geometry" />
                </mxCell>
                <mxCell id="cls_pengguna_attrs" parent="cls_pengguna" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- id_pengguna : UUID&#xa;- username : String&#xa;- password_hash : String&#xa;- email : String&#xa;- role : RoleEnum&#xa;- status_aktif : Boolean" vertex="1">
                    <mxGeometry y="26" width="240" height="74" as="geometry" />
                </mxCell>
                <mxCell id="cls_pengguna_sep" parent="cls_pengguna" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="100" width="240" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_pengguna_ops" parent="cls_pengguna" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ login(user, pass) : Boolean&#xa;+ logout() : Void&#xa;+ updatePassword(new) : Boolean" vertex="1">
                    <mxGeometry y="108" width="240" height="42" as="geometry" />
                </mxCell>

                <!-- SUBCLASS: SISWA -->
                <mxCell id="cls_siswa" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="Siswa" vertex="1">
                    <mxGeometry x="120" y="320" width="250" height="150" as="geometry" />
                </mxCell>
                <mxCell id="cls_siswa_attrs" parent="cls_siswa" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- nisn : String&#xa;- nis : String&#xa;- nama_lengkap : String&#xa;- kelas : String&#xa;- jurusan : String&#xa;- no_telepon : String" vertex="1">
                    <mxGeometry y="26" width="250" height="74" as="geometry" />
                </mxCell>
                <mxCell id="cls_siswa_sep" parent="cls_siswa" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="100" width="250" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_siswa_ops" parent="cls_siswa" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ buatPengajuanSurat() : PengajuanSurat&#xa;+ uploadBerkas() : BerkasPersyaratan&#xa;+ lacakStatus(tiket) : StatusSuratEnum" vertex="1">
                    <mxGeometry y="108" width="250" height="42" as="geometry" />
                </mxCell>

                <!-- SUBCLASS: PETUGAS TU -->
                <mxCell id="cls_tu" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="PetugasTU" vertex="1">
                    <mxGeometry x="675" y="320" width="250" height="150" as="geometry" />
                </mxCell>
                <mxCell id="cls_tu_attrs" parent="cls_tu" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- nip : String&#xa;- nama_petugas : String&#xa;- nomor_sk : String&#xa;- bagian : String" vertex="1">
                    <mxGeometry y="26" width="250" height="74" as="geometry" />
                </mxCell>
                <mxCell id="cls_tu_sep" parent="cls_tu" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="100" width="250" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_tu_ops" parent="cls_tu" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ verifikasiBerkas() : Boolean&#xa;+ generateNomorSurat() : String&#xa;+ forwardKeKepsek() : Void" vertex="1">
                    <mxGeometry y="108" width="250" height="42" as="geometry" />
                </mxCell>

                <!-- SUBCLASS: KEPALA SEKOLAH -->
                <mxCell id="cls_kepsek" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="KepalaSekolah" vertex="1">
                    <mxGeometry x="1220" y="320" width="250" height="150" as="geometry" />
                </mxCell>
                <mxCell id="cls_kepsek_attrs" parent="cls_kepsek" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- nip : String&#xa;- nama_lengkap : String&#xa;- pangkat_gol : String&#xa;- ttd_digital_hash : String" vertex="1">
                    <mxGeometry y="26" width="250" height="74" as="geometry" />
                </mxCell>
                <mxCell id="cls_kepsek_sep" parent="cls_kepsek" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="100" width="250" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_kepsek_ops" parent="cls_kepsek" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ reviewPengajuan() : PengajuanSurat&#xa;+ approveSurat() : Boolean&#xa;+ bubuhkanQRCodeTTE() : String" vertex="1">
                    <mxGeometry y="108" width="250" height="42" as="geometry" />
                </mxCell>

                <!-- INHERITANCE ARROWS -->
                <mxCell id="inh_siswa" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_siswa" target="cls_pengguna">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="inh_tu" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_tu" target="cls_pengguna">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="inh_kepsek" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_kepsek" target="cls_pengguna">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- CORE ENTITY: PENGAJUAN SURAT -->
                <mxCell id="cls_pengajuan" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="PengajuanSurat" vertex="1">
                    <mxGeometry x="120" y="580" width="260" height="170" as="geometry" />
                </mxCell>
                <mxCell id="cls_pengajuan_attrs" parent="cls_pengajuan" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- id_pengajuan : UUID&#xa;- nomor_tiket : String&#xa;- tanggal_pengajuan : DateTime&#xa;- keperluan : String&#xa;- status : StatusSuratEnum&#xa;- nomor_surat_resmi : String&#xa;- qr_code_hash : String" vertex="1">
                    <mxGeometry y="26" width="260" height="94" as="geometry" />
                </mxCell>
                <mxCell id="cls_pengajuan_sep" parent="cls_pengajuan" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="120" width="260" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_pengajuan_ops" parent="cls_pengajuan" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ updateStatus(newStatus) : Void&#xa;+ generateTiketCode() : String&#xa;+ batalkanPengajuan() : Boolean" vertex="1">
                    <mxGeometry y="128" width="260" height="42" as="geometry" />
                </mxCell>

                <!-- MASTER ENTITY: JENIS SURAT -->
                <mxCell id="cls_jenis" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="JenisSurat" vertex="1">
                    <mxGeometry x="120" y="850" width="260" height="130" as="geometry" />
                </mxCell>
                <mxCell id="cls_jenis_attrs" parent="cls_jenis" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- id_jenis : UUID&#xa;- kode_surat : String&#xa;- nama_surat : String&#xa;- masa_berlaku_hari : Integer" vertex="1">
                    <mxGeometry y="26" width="260" height="64" as="geometry" />
                </mxCell>
                <mxCell id="cls_jenis_sep" parent="cls_jenis" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="90" width="260" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_jenis_ops" parent="cls_jenis" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ getSyaratDokumen() : List&lt;String&gt;&#xa;+ generateFormatNomor() : String" vertex="1">
                    <mxGeometry y="98" width="260" height="32" as="geometry" />
                </mxCell>

                <!-- ATTACHMENT ENTITY: BERKAS PERSYARATAN -->
                <mxCell id="cls_berkas" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="BerkasPersyaratan" vertex="1">
                    <mxGeometry x="480" y="590" width="240" height="150" as="geometry" />
                </mxCell>
                <mxCell id="cls_berkas_attrs" parent="cls_berkas" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- id_berkas : UUID&#xa;- nama_file : String&#xa;- file_url : String&#xa;- file_size_kb : Integer&#xa;- status_valid : Boolean" vertex="1">
                    <mxGeometry y="26" width="240" height="74" as="geometry" />
                </mxCell>
                <mxCell id="cls_berkas_sep" parent="cls_berkas" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="100" width="240" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_berkas_ops" parent="cls_berkas" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ validasiUkuran() : Boolean&#xa;+ validasiEkstensi() : Boolean" vertex="1">
                    <mxGeometry y="108" width="240" height="42" as="geometry" />
                </mxCell>

                <!-- TRANSACTION LOG: VERIFIKASI TU -->
                <mxCell id="cls_verif" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="VerifikasiTU" vertex="1">
                    <mxGeometry x="840" y="590" width="240" height="150" as="geometry" />
                </mxCell>
                <mxCell id="cls_verif_attrs" parent="cls_verif" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- id_verifikasi : UUID&#xa;- tanggal_verifikasi : DateTime&#xa;- status_berkas : Boolean&#xa;- catatan_revisi : String" vertex="1">
                    <mxGeometry y="26" width="240" height="74" as="geometry" />
                </mxCell>
                <mxCell id="cls_verif_sep" parent="cls_verif" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="100" width="240" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_verif_ops" parent="cls_verif" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ simpanCatatan() : Void&#xa;+ kirimNotifRevisi() : Void" vertex="1">
                    <mxGeometry y="108" width="240" height="42" as="geometry" />
                </mxCell>

                <!-- TRANSACTION LOG: APPROVAL KEPSEK -->
                <mxCell id="cls_appr" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;" value="ApprovalKepsek" vertex="1">
                    <mxGeometry x="1220" y="590" width="250" height="150" as="geometry" />
                </mxCell>
                <mxCell id="cls_appr_attrs" parent="cls_appr" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="- id_approval : UUID&#xa;- tanggal_approval : DateTime&#xa;- keputusan : ApprovalEnum&#xa;- catatan_kepsek : String&#xa;- signature_token : String" vertex="1">
                    <mxGeometry y="26" width="250" height="74" as="geometry" />
                </mxCell>
                <mxCell id="cls_appr_sep" parent="cls_appr" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=#000000;" vertex="1">
                    <mxGeometry y="100" width="250" height="8" as="geometry" />
                </mxCell>
                <mxCell id="cls_appr_ops" parent="cls_appr" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontColor=#000000;fontSize=10;" value="+ generateSignature() : String&#xa;+ auditKeputusan() : Void" vertex="1">
                    <mxGeometry y="108" width="250" height="42" as="geometry" />
                </mxCell>

                <!-- RELATIONS -->
                <!-- Siswa to Pengajuan (1 to 0..*) -->
                <mxCell id="rel_s_p" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_siswa" target="cls_pengajuan">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="lbl_s_p" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontColor=#000000;" value="1 &amp;nbsp; &amp;nbsp; &amp;nbsp; mengajukan &amp;nbsp; &amp;nbsp; &amp;nbsp; 0..*" vertex="1">
                    <mxGeometry x="250" y="510" width="120" height="20" as="geometry" />
                </mxCell>

                <!-- Pengajuan to JenisSurat (0..* to 1) -->
                <mxCell id="rel_p_j" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_pengajuan" target="cls_jenis">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="lbl_p_j" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontColor=#000000;" value="0..* &amp;nbsp; &amp;nbsp; &amp;nbsp; memiliki &amp;nbsp; &amp;nbsp; &amp;nbsp; 1" vertex="1">
                    <mxGeometry x="250" y="790" width="120" height="20" as="geometry" />
                </mxCell>

                <!-- Pengajuan to Berkas (Composition: 1 to 1..*) -->
                <mxCell id="rel_p_b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;startArrow=diamond;startFill=1;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_pengajuan" target="cls_berkas">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="lbl_p_b" parent="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontColor=#000000;" value="1 &amp;nbsp; &amp;nbsp; &amp;nbsp; melampirkan &amp;nbsp; &amp;nbsp; &amp;nbsp; 1..*" vertex="1">
                    <mxGeometry x="380" y="640" width="100" height="20" as="geometry" />
                </mxCell>

                <!-- Pengajuan to VerifikasiTU -->
                <mxCell id="rel_p_v" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_pengajuan" target="cls_verif">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="250" y="780" />
                            <mxPoint x="960" y="780" />
                        </Array>
                    </mxGeometry>
                </mxCell>

                <!-- PetugasTU to VerifikasiTU -->
                <mxCell id="rel_tu_v" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_tu" target="cls_verif">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

                <!-- Kepsek to ApprovalKepsek -->
                <mxCell id="rel_k_a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#000000;strokeWidth=2;" edge="1" parent="1" source="cls_kepsek" target="cls_appr">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

            </root>
        </mxGraphModel>
    </diagram>

    <diagram id="object-diagram-sipesat" name="2. Object Diagram (Snapshot Runtime)">
        <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1100" math="0" shadow="0">
            <root>
                <mxCell id="0_obj" />
                <mxCell id="1_obj" parent="0_obj" />

                <!-- HEADER BANNER -->
                <mxCell id="hdr_obj" parent="1_obj" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:18px;'&gt;OBJECT DIAGRAM — SNAPSHOT INSTANSIASI RUNTIME PENERBITAN SURAT AKTIF&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Pemodelan UML 2.5 Instansiasi Objek Nyata Skenario Penerbitan Surat — Kelompok 7 (RPL_XD UNINDRA 2026)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1600" x="50" y="20" as="geometry" />
                </mxCell>

                <!-- OBJECT: adamSiswa -->
                <mxCell id="obj_adam" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;adamSiswa : Siswa&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_pengguna = &quot;USR-001&quot;&lt;br&gt;username = &quot;adam.wahyu&quot;&lt;br&gt;nisn = &quot;0051234567&quot;&lt;br&gt;nama_lengkap = &quot;Adam Wahyu Kurniawan&quot;&lt;br&gt;kelas = &quot;XII RPL 1&quot;&lt;br&gt;jurusan = &quot;Rekayasa Perangkat Lunak&quot;" vertex="1">
                    <mxGeometry x="100" y="140" width="280" height="150" as="geometry" />
                </mxCell>

                <!-- OBJECT: budiTU -->
                <mxCell id="obj_budi" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;budiTU : PetugasTU&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_pengguna = &quot;USR-002&quot;&lt;br&gt;username = &quot;budi.tu&quot;&lt;br&gt;nip = &quot;198503152010011002&quot;&lt;br&gt;nama_petugas = &quot;Budi Santoso, S.Kom&quot;&lt;br&gt;bagian = &quot;Administrasi Kesiswaan&quot;" vertex="1">
                    <mxGeometry x="660" y="140" width="280" height="150" as="geometry" />
                </mxCell>

                <!-- OBJECT: hasanKepsek -->
                <mxCell id="obj_hasan" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;hasanKepsek : KepalaSekolah&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_pengguna = &quot;USR-003&quot;&lt;br&gt;username = &quot;hasan.kepsek&quot;&lt;br&gt;nip = &quot;197204121998021001&quot;&lt;br&gt;nama_lengkap = &quot;Drs. H. Hasan Basri, M.Pd&quot;&lt;br&gt;pangkat_gol = &quot;Pembina Utama Muda / IV-C&quot;" vertex="1">
                    <mxGeometry x="1220" y="140" width="290" height="150" as="geometry" />
                </mxCell>

                <!-- OBJECT: pengajuan001 -->
                <mxCell id="obj_req" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;pengajuan001 : PengajuanSurat&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_pengajuan = &quot;REQ-202610-001&quot;&lt;br&gt;nomor_tiket = &quot;TKT-202610-001&quot;&lt;br&gt;tanggal_pengajuan = &quot;16-10-2026 09:15&quot;&lt;br&gt;keperluan = &quot;Persyaratan Beasiswa 2026&quot;&lt;br&gt;status = DISETUJUI&lt;br&gt;nomor_surat_resmi = &quot;421.3/088/SMK/X/2026&quot;&lt;br&gt;qr_code_hash = &quot;e3b0c44298fc1c149afbf4c8&quot;" vertex="1">
                    <mxGeometry x="100" y="400" width="300" height="170" as="geometry" />
                </mxCell>

                <!-- OBJECT: suratAktif -->
                <mxCell id="obj_surat" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;suratAktif : JenisSurat&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_jenis = &quot;JNS-001&quot;&lt;br&gt;kode_surat = &quot;SK-AKTIF&quot;&lt;br&gt;nama_surat = &quot;Surat Keterangan Siswa Aktif&quot;&lt;br&gt;masa_berlaku_hari = 30" vertex="1">
                    <mxGeometry x="100" y="690" width="290" height="130" as="geometry" />
                </mxCell>

                <!-- OBJECT: berkasKK -->
                <mxCell id="obj_doc" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;berkasKK : BerkasPersyaratan&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_berkas = &quot;DOC-001&quot;&lt;br&gt;nama_file = &quot;kartu_keluarga_adam.pdf&quot;&lt;br&gt;file_url = &quot;/uploads/kk_adam.pdf&quot;&lt;br&gt;file_size_kb = 485&lt;br&gt;status_valid = true" vertex="1">
                    <mxGeometry x="490" y="415" width="260" height="140" as="geometry" />
                </mxCell>

                <!-- OBJECT: verif001 -->
                <mxCell id="obj_verif" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;verif001 : VerifikasiTU&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_verifikasi = &quot;VRF-001&quot;&lt;br&gt;tanggal_verifikasi = &quot;16-10-2026 10:30&quot;&lt;br&gt;status_berkas = true&lt;br&gt;catatan_revisi = &quot;Berkas lengkap dan valid&quot;" vertex="1">
                    <mxGeometry x="840" y="415" width="260" height="140" as="geometry" />
                </mxCell>

                <!-- OBJECT: appr001 -->
                <mxCell id="obj_appr" parent="1_obj" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;align=left;verticalAlign=top;spacing=8;fontColor=#000000;" value="&lt;u&gt;&lt;b&gt;appr001 : ApprovalKepsek&lt;/b&gt;&lt;/u&gt;&lt;hr style='border:0.5px solid #000;'&gt;id_approval = &quot;APP-001&quot;&lt;br&gt;tanggal_approval = &quot;16-10-2026 11:45&quot;&lt;br&gt;keputusan = DISETUJUI&lt;br&gt;catatan_kepsek = &quot;Disetujui beasiswa prestasi&quot;" vertex="1">
                    <mxGeometry x="1220" y="415" width="280" height="140" as="geometry" />
                </mxCell>

                <!-- OBJECT LINKS -->
                <mxCell id="link_adam_req" style="strokeColor=#000000;strokeWidth=2;endArrow=none;html=1;" edge="1" parent="1_obj" source="obj_adam" target="obj_req">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="link_req_surat" style="strokeColor=#000000;strokeWidth=2;endArrow=none;html=1;" edge="1" parent="1_obj" source="obj_req" target="obj_surat">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="link_req_doc" style="strokeColor=#000000;strokeWidth=2;endArrow=none;html=1;" edge="1" parent="1_obj" source="obj_req" target="obj_doc">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="link_budi_verif" style="strokeColor=#000000;strokeWidth=2;endArrow=none;html=1;" edge="1" parent="1_obj" source="obj_budi" target="obj_verif">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="link_hasan_appr" style="strokeColor=#000000;strokeWidth=2;endArrow=none;html=1;" edge="1" parent="1_obj" source="obj_hasan" target="obj_appr">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="link_verif_req" style="strokeColor=#000000;strokeWidth=2;endArrow=none;html=1;" edge="1" parent="1_obj" source="obj_verif" target="obj_req">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="link_appr_req" style="strokeColor=#000000;strokeWidth=2;endArrow=none;html=1;" edge="1" parent="1_obj" source="obj_appr" target="obj_req">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>

            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""

out_file = r"c:\A_main_code\all-my-projek\RPL\tugas-6-class-object.drawio"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(drawio_content)

print(f"Successfully generated 2-Tab Draw.io file at: {out_file}")
