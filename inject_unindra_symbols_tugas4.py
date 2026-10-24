import os
import xml.etree.ElementTree as ET

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"
tugas4_path = os.path.join(RPL_DIR, "tugas-4-activity-sequence.drawio")

# Read existing file to preserve Tab 1 (Activity) and Tab 2 (Sequence BCE)
tree = ET.parse(tugas4_path)
root = tree.getroot()
existing_diagrams = root.findall("diagram")

# Tab 1 from existing file is Activity Diagram
act_xml_elem = existing_diagrams[0]
# Tab 2 from existing file is Sequence Diagram
seq_xml_elem = existing_diagrams[1]

# Convert existing diagrams to string
act_str = ET.tostring(act_xml_elem, encoding="utf-8").decode("utf-8")
seq_str = ET.tostring(seq_xml_elem, encoding="utf-8").decode("utf-8")

# Ensure s_end_node uses the official shape=endState
act_str = act_str.replace('shape=doubleEllipse;html=1;fillColor=#000000;strokeColor=#000000;strokeWidth=2.2;', 'ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;')

# Create the Official UNINDRA Symbol Table Tab (Slide 5, 6, 7)
symbol_tab_xml = """    <diagram id="simbol-unindra-slide5-7" name="Standar Simbol UNINDRA (Slide 5-7)">
        <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1500" pageHeight="1100" math="0" shadow="0">
            <root>
                <mxCell id="0" />
                <mxCell id="1" parent="0" />

                <!-- HEADER BANNER -->
                <mxCell id="sym_banner" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;align=center;verticalAlign=middle;strokeWidth=2;" value="&lt;b style='font-size:16px;'&gt;TABEL SIMBOL RESMI ACTIVITY DIAGRAM — MODUL RPL UNINDRA (SLIDE 5, 6, 7)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#000000;'&gt;Bahan Ajar Perkuliahan Rekayasa Perangkat Lunak — Standar Pemodelan Unified Modeling Language (UML)&lt;/span&gt;" vertex="1">
                    <mxGeometry height="55" width="1380" x="60" y="20" as="geometry" />
                </mxCell>

                <!-- TABLE HEADER -->
                <mxCell id="th_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#ffffff;fontStyle=1;fontSize=12;align=center;" value="NO" vertex="1">
                    <mxGeometry height="42" width="60" x="60" y="95" as="geometry" />
                </mxCell>
                <mxCell id="th_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#ffffff;fontStyle=1;fontSize=12;align=center;" value="NAMA SIMBOL" vertex="1">
                    <mxGeometry height="42" width="280" x="120" y="95" as="geometry" />
                </mxCell>
                <mxCell id="th_visual" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#ffffff;fontStyle=1;fontSize=12;align=center;" value="BENTUK SIMBOL VISUAL" vertex="1">
                    <mxGeometry height="42" width="320" x="400" y="95" as="geometry" />
                </mxCell>
                <mxCell id="th_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#ffffff;fontStyle=1;fontSize=12;align=center;" value="DESKRIPSI &amp;amp; KAIDAH PENGGUNAAN (MODUL UNINDRA)" vertex="1">
                    <mxGeometry height="42" width="720" x="720" y="95" as="geometry" />
                </mxCell>

                <!-- ROW 1: STATUS AWAL -->
                <mxCell id="r1_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=center;fontSize=12;" value="1" vertex="1">
                    <mxGeometry height="75" width="60" x="60" y="137" as="geometry" />
                </mxCell>
                <mxCell id="r1_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=12;fontStyle=1;spacingLeft=12;" value="STATUS AWAL (Start Point)" vertex="1">
                    <mxGeometry height="75" width="280" x="120" y="137" as="geometry" />
                </mxCell>
                <mxCell id="r1_vis_box" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="75" width="320" x="400" y="137" as="geometry" />
                </mxCell>
                <mxCell id="sym_start" parent="1" style="ellipse;html=1;shape=startState;fillColor=#000000;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="32" width="32" x="544" y="158" as="geometry" />
                </mxCell>
                <mxCell id="r1_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=11.5;spacingLeft=12;" value="• Status awal dimulainya aktivitas sistem.&lt;br&gt;• Diagram aktivitas wajib memiliki sebuah status awal sebagai gerbang eksekusi proses." vertex="1">
                    <mxGeometry height="75" width="720" x="720" y="137" as="geometry" />
                </mxCell>

                <!-- ROW 2: AKTIVITAS / STATE -->
                <mxCell id="r2_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=center;fontSize=12;" value="2" vertex="1">
                    <mxGeometry height="80" width="60" x="60" y="212" as="geometry" />
                </mxCell>
                <mxCell id="r2_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=12;fontStyle=1;spacingLeft=12;" value="AKTIVITAS / STATE" vertex="1">
                    <mxGeometry height="80" width="280" x="120" y="212" as="geometry" />
                </mxCell>
                <mxCell id="r2_vis_box" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="80" width="320" x="400" y="212" as="geometry" />
                </mxCell>
                <mxCell id="sym_state" parent="1" style="rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontSize=11;fontStyle=1;align=center;" value="Aktivitas / State" vertex="1">
                    <mxGeometry height="42" width="180" x="470" y="231" as="geometry" />
                </mxCell>
                <mxCell id="r2_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=11.5;spacingLeft=12;" value="• Aktivitas yang dilakukan oleh sistem atau aktor pengguna.&lt;br&gt;• Kaidah Baku UNINDRA: Penamaan aktivitas biasanya DIAWALI DENGAN KATA KERJA (contoh: Buka, Input, Validasi, Simpan, Unduh)." vertex="1">
                    <mxGeometry height="80" width="720" x="720" y="212" as="geometry" />
                </mxCell>

                <!-- ROW 3: PERCABANGAN / DECISION -->
                <mxCell id="r3_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=center;fontSize=12;" value="3" vertex="1">
                    <mxGeometry height="85" width="60" x="60" y="292" as="geometry" />
                </mxCell>
                <mxCell id="r3_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=12;fontStyle=1;spacingLeft=12;" value="PERCABANGAN / DECISION" vertex="1">
                    <mxGeometry height="85" width="280" x="120" y="292" as="geometry" />
                </mxCell>
                <mxCell id="r3_vis_box" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="85" width="320" x="400" y="292" as="geometry" />
                </mxCell>
                <mxCell id="sym_decision" parent="1" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontSize=10.5;align=center;fontStyle=1;" value="Decision" vertex="1">
                    <mxGeometry height="54" width="110" x="505" y="307" as="geometry" />
                </mxCell>
                <mxCell id="r3_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=11.5;spacingLeft=12;" value="• Titik percabangan logika pemilihan di mana terdapat pilihan aktivitas lebih dari satu.&lt;br&gt;• Memiliki panah keluar alternatif yang wajib disertai kondisi guard (contoh: [Ya / Valid] atau [Tidak / Gagal])." vertex="1">
                    <mxGeometry height="85" width="720" x="720" y="292" as="geometry" />
                </mxCell>

                <!-- ROW 4: STATUS AKHIR / END POINT -->
                <mxCell id="r4_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=center;fontSize=12;" value="4" vertex="1">
                    <mxGeometry height="75" width="60" x="60" y="377" as="geometry" />
                </mxCell>
                <mxCell id="r4_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=12;fontStyle=1;spacingLeft=12;" value="STATUS AKHIR (End Point)" vertex="1">
                    <mxGeometry height="75" width="280" x="120" y="377" as="geometry" />
                </mxCell>
                <mxCell id="r4_vis_box" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="75" width="320" x="400" y="377" as="geometry" />
                </mxCell>
                <mxCell id="sym_end" parent="1" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="32" width="32" x="544" y="398" as="geometry" />
                </mxCell>
                <mxCell id="r4_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=11.5;spacingLeft=12;" value="• Status akhir atau terminasi proses yang menandakan seluruh aktivitas sistem telah selesai dilaksanakan." vertex="1">
                    <mxGeometry height="75" width="720" x="720" y="377" as="geometry" />
                </mxCell>

                <!-- ROW 5: FORK & JOIN -->
                <mxCell id="r5_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=center;fontSize=12;" value="5" vertex="1">
                    <mxGeometry height="90" width="60" x="60" y="452" as="geometry" />
                </mxCell>
                <mxCell id="r5_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=12;fontStyle=1;spacingLeft=12;" value="PERCABANGAN (Fork) &amp;amp;&lt;br&gt;PENGGABUNGAN (Join)" vertex="1">
                    <mxGeometry height="90" width="280" x="120" y="452" as="geometry" />
                </mxCell>
                <mxCell id="r5_vis_box" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="90" width="320" x="400" y="452" as="geometry" />
                </mxCell>
                <mxCell id="sym_fork" parent="1" style="rounded=0;fillColor=#000000;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="8" width="160" x="480" y="493" as="geometry" />
                </mxCell>
                <mxCell id="r5_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=11.5;spacingLeft=12;" value="• Percabangan (Fork): Memecah satu aliran aktivitas menjadi dua atau lebih aliran paralel secara bersamaan.&lt;br&gt;• Penggabungan (Join): Menggabungkan kembali beberapa aliran paralel menjadi satu aliran tunggal." vertex="1">
                    <mxGeometry height="90" width="720" x="720" y="452" as="geometry" />
                </mxCell>

                <!-- ROW 6: SOLID LINE / TRANSISI -->
                <mxCell id="r6_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=center;fontSize=12;" value="6" vertex="1">
                    <mxGeometry height="75" width="60" x="60" y="542" as="geometry" />
                </mxCell>
                <mxCell id="r6_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=12;fontStyle=1;spacingLeft=12;" value="SOLID LINE / TRANSISI" vertex="1">
                    <mxGeometry height="75" width="280" x="120" y="542" as="geometry" />
                </mxCell>
                <mxCell id="r6_vis_box" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="75" width="320" x="400" y="542" as="geometry" />
                </mxCell>
                <mxCell id="sym_line_start" parent="1" style="ellipse;fillColor=none;strokeColor=none;" value="" vertex="1">
                    <mxGeometry height="1" width="1" x="460" y="579" as="geometry" />
                </mxCell>
                <mxCell id="sym_line_end" parent="1" style="ellipse;fillColor=none;strokeColor=none;" value="" vertex="1">
                    <mxGeometry height="1" width="1" x="660" y="579" as="geometry" />
                </mxCell>
                <mxCell id="edge_sym_line" edge="1" parent="1" source="sym_line_start" style="endArrow=classic;html=1;strokeColor=#000000;strokeWidth=2;" target="sym_line_end">
                    <mxGeometry relative="1" as="geometry" />
                </mxCell>
                <mxCell id="r6_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=11.5;spacingLeft=12;" value="• Garis lurus dengan panah solid yang menunjukkan urutan perpindahan kontrol aktivitas dari satu tahap ke tahap berikutnya." vertex="1">
                    <mxGeometry height="75" width="720" x="720" y="542" as="geometry" />
                </mxCell>

                <!-- ROW 7: SWIMLANE -->
                <mxCell id="r7_no" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=center;fontSize=12;" value="7" vertex="1">
                    <mxGeometry height="95" width="60" x="60" y="617" as="geometry" />
                </mxCell>
                <mxCell id="r7_nama" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=12;fontStyle=1;spacingLeft=12;" value="SWIMLANE (KOLOM)" vertex="1">
                    <mxGeometry height="95" width="280" x="120" y="617" as="geometry" />
                </mxCell>
                <mxCell id="r7_vis_box" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;" value="" vertex="1">
                    <mxGeometry height="95" width="320" x="400" y="617" as="geometry" />
                </mxCell>
                <mxCell id="sym_swim_1" parent="1" style="swimlane;startSize=22;fontSize=10;fontStyle=1;align=center;fillColor=#ffffff;strokeColor=#000000;" value="Aktor" vertex="1">
                    <mxGeometry height="65" width="100" x="450" y="632" as="geometry" />
                </mxCell>
                <mxCell id="sym_swim_2" parent="1" style="swimlane;startSize=22;fontSize=10;fontStyle=1;align=center;fillColor=#ffffff;strokeColor=#000000;" value="Sistem" vertex="1">
                    <mxGeometry height="65" width="110" x="560" y="632" as="geometry" />
                </mxCell>
                <mxCell id="r7_desc" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;align=left;fontSize=11.5;spacingLeft=12;" value="• Penggambaran aktivitas berdasarkan aktor atau mengelompokkan aktivitas dalam sebuah urutan yang sama.&lt;br&gt;• Memisahkan batasan tanggung jawab organisasi bisnis (contoh: Siswa, Sistem SIPESAT, Staf TU &amp;amp; Kepala Sekolah)." vertex="1">
                    <mxGeometry height="95" width="720" x="720" y="617" as="geometry" />
                </mxCell>

            </root>
        </mxGraphModel>
    </diagram>"""

# Assemble 3-Tab XML
full_tugas4_xml = f"""<mxfile host="65bd71144e">
{symbol_tab_xml}
{act_str}
{seq_str}
</mxfile>"""

with open(tugas4_path, "w", encoding="utf-8") as f:
    f.write(full_tugas4_xml)

print(f"[OK] tugas-4-activity-sequence.drawio upgraded to 3 Official Tabs:")
print(f"  Tab 1: Standar Simbol UNINDRA (Slide 5-7)")
print(f"  Tab 2: 1. Activity Diagram (Siswa s.d Petugas)")
print(f"  Tab 3: 2. Sequence Diagrams (Pola BCE)")
