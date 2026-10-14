'use client';

import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { PengajuanItem } from '@/lib/types';
import { formatDate } from '@/lib/utils';
import { api } from '@/lib/api';
import { Printer, ArrowLeft, School, QrCode } from 'lucide-react';

export default function CetakSuratResmiPage({
  params,
}: {
  params: { id: string };
}) {
  const router = useRouter();
  const [data, setData] = useState<PengajuanItem | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const res = await api.get(`/pengajuan/${params.id}`);
        setData(res?.data || null);
      } catch (err) {
        console.error('Error load detail surat:', err);
        router.back();
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, [params.id, router]);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-100 flex items-center justify-center">
        <p className="text-xs font-semibold text-slate-500">Menyiapkan format surat resmi...</p>
      </div>
    );
  }

  if (!data) return null;

  const schoolName = process.env.NEXT_PUBLIC_SCHOOL_NAME || 'PEMERINTAH PROVINSI JAWA BARAT';
  const schoolSub = 'DINAS PENDIDIKAN DAN KEBUDAYAAN';
  const schoolTitle = 'CABANG DINAS PENDIDIKAN WILAYAH III';
  const smkName = 'SMK NEGERI 1 CONTOH KOTA';
  const address = 'Jalan Pendidikan No. 123 Komplek Sekolah Menengah, Telp. (021) 8876543, Email: info@smkn1contoh.sch.id';

  return (
    <div className="min-h-screen bg-slate-200/70 p-4 sm:p-8 flex flex-col items-center">
      {/* Top Floating Bar for user actions (hidden on print) */}
      <div className="no-print w-full max-w-[210mm] bg-white border border-surface-border rounded-xl p-4 mb-6 shadow-sm flex items-center justify-between">
        <button
          onClick={() => {
            if (window.history.length > 1) {
              router.back();
            } else {
              window.close();
            }
          }}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-lg transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Kembali</span>
        </button>

        <div className="text-center">
          <p className="text-xs font-bold text-slate-800">
            Pratinjau Format Cetak Dokumen Resmi
          </p>
          <p className="text-[11px] text-slate-500 font-mono">
            {data.nomorSuratResmi || data.nomorPengajuan}
          </p>
        </div>

        <button
          onClick={() => window.print()}
          className="inline-flex items-center gap-2 px-4 py-2 text-xs font-semibold text-white bg-brand-500 hover:bg-brand-600 rounded-lg shadow-sm transition-colors"
        >
          <Printer className="w-4 h-4" />
          <span>Cetak Dokumen (Print/PDF)</span>
        </button>
      </div>

      {/* A4 Sheet Container */}
      <div className="print-area bg-white w-full max-w-[210mm] min-h-[297mm] p-10 sm:p-14 shadow-lg text-black font-serif relative">
        {/* Kop Surat Resmi */}
        <div className="text-center border-b-4 border-double border-black pb-3 mb-6">
          <div className="flex items-center justify-center gap-4 mb-2">
            <div className="w-16 h-16 border-2 border-black rounded flex items-center justify-center">
              <School className="w-10 h-10 text-black" />
            </div>
            <div>
              <p className="text-xs uppercase font-sans tracking-widest font-semibold">{schoolName}</p>
              <p className="text-xs uppercase font-sans tracking-wider">{schoolSub}</p>
              <p className="text-[11px] uppercase font-sans tracking-wider">{schoolTitle}</p>
              <h1 className="text-xl font-bold uppercase font-sans tracking-tight mt-0.5">
                {smkName}
              </h1>
            </div>
          </div>
          <p className="text-[10px] font-sans text-slate-800 leading-tight">
            {address}
          </p>
        </div>

        {/* Judul & Nomor Surat */}
        <div className="text-center mb-6">
          <h2 className="text-base font-bold uppercase underline tracking-wider">
            {data.jenisSurat?.namaSurat}
          </h2>
          <p className="text-xs font-mono mt-1">
            Nomor: {data.nomorSuratResmi || `421.3/${data.nomorPengajuan}/SMKN1/2026`}
          </p>
        </div>

        {/* Pembuka */}
        <div className="text-xs leading-relaxed space-y-4 text-justify font-sans">
          <p>
            Yang bertanda tangan di bawah ini Kepala {smkName}, dengan ini menerangkan dengan sesungguhnya bahwa:
          </p>

          {/* Biodata Pemohon */}
          <div className="pl-6 space-y-1.5 my-3">
            <div className="grid grid-cols-12">
              <span className="col-span-4 font-semibold">Nama Lengkap</span>
              <span className="col-span-1">:</span>
              <span className="col-span-7 font-bold uppercase">{data.siswa?.nama}</span>
            </div>
            <div className="grid grid-cols-12">
              <span className="col-span-4 font-semibold">NISN / NIS</span>
              <span className="col-span-1">:</span>
              <span className="col-span-7 font-mono">{data.siswa?.nisn || '-'}</span>
            </div>
            <div className="grid grid-cols-12">
              <span className="col-span-4 font-semibold">Kelas</span>
              <span className="col-span-1">:</span>
              <span className="col-span-7">{data.siswa?.kelas || '-'}</span>
            </div>
            <div className="grid grid-cols-12">
              <span className="col-span-4 font-semibold">Kompetensi Keahlian</span>
              <span className="col-span-1">:</span>
              <span className="col-span-7">{data.siswa?.jurusan || '-'}</span>
            </div>
            <div className="grid grid-cols-12">
              <span className="col-span-4 font-semibold">Keperluan Permohonan</span>
              <span className="col-span-1">:</span>
              <span className="col-span-7 font-medium">{data.keperluan}</span>
            </div>
          </div>

          {/* Isi Surat */}
          <p>
            {data.jenisSurat?.templateIsi ||
              'Adalah benar nama tersebut di atas terdaftar sebagai siswa aktif pada Sekolah Menengah Kejuruan Negeri 1 Contoh Kota Tahun Ajaran 2026/2027 dan senantiasa menaati seluruh tata tertib sekolah.'}
          </p>

          <p>
            Demikian surat keterangan ini kami buat dengan sebenarnya agar dapat dipergunakan sebagaimana mestinya oleh yang bersangkutan.
          </p>
        </div>

        {/* Bagian Tanda Tangan & QR Verifikasi */}
        <div className="mt-14 pt-4 flex justify-between items-start font-sans text-xs">
          {/* QR Code Verifikasi Dokumen */}
          <div className="border border-slate-300 p-3 rounded text-center w-36">
            <div className="w-20 h-20 mx-auto bg-slate-50 border border-slate-300 flex items-center justify-center">
              <QrCode className="w-16 h-16 text-slate-800" />
            </div>
            <p className="text-[9px] font-mono text-slate-500 mt-1">
              Verifikasi Keaslian
            </p>
            <p className="text-[8px] font-mono text-slate-400">
              {data.nomorPengajuan}
            </p>
          </div>

          {/* Tanda Tangan Kepala Sekolah */}
          <div className="text-left w-64 pl-6">
            <p>Ditetapkan di : Kota Contoh</p>
            <p>Pada tanggal : {formatDate(data.tanggalSelesai || data.tanggalPengajuan)}</p>
            <p className="font-bold mt-2">Kepala SMK Negeri 1 Contoh Kota</p>

            <div className="h-20 my-1 flex items-center pl-2">
              <div className="text-[10px] text-slate-400 border border-dashed border-slate-300 px-2 py-1 rounded">
                [Tanda Tangan & Cap Sah]
              </div>
            </div>

            <p className="font-bold underline text-sm">Drs. H. Mulyadi, M.Pd.</p>
            <p className="text-[11px] text-slate-700">Pembina Tk. I / IV b</p>
            <p className="text-[11px] text-slate-700 font-mono">NIP. 19680512 199403 1 004</p>
          </div>
        </div>
      </div>
    </div>
  );
}
