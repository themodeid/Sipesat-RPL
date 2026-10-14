'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { PengajuanItem } from '@/lib/types';
import StatusBadge from '@/components/StatusBadge';
import { formatDate, formatDateTime } from '@/lib/utils';
import { api } from '@/lib/api';
import {
  ArrowLeft,
  Printer,
  FileText,
  User,
  Clock,
  ExternalLink,
  ShieldCheck,
  FileCheck2,
} from 'lucide-react';

export default function DetailPengajuanPage({
  params,
}: {
  params: { id: string };
}) {
  const router = useRouter();
  const [data, setData] = useState<PengajuanItem | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDetail() {
      try {
        const res = await api.get(`/pengajuan/${params.id}`);
        setData(res?.data || null);
      } catch (err) {
        console.error('Error detail:', err);
        router.back();
      } finally {
        setLoading(false);
      }
    }
    loadDetail();
  }, [params.id, router]);

  if (loading) {
    return (
      <div className="flex items-center justify-center p-12">
        <div className="flex flex-col items-center gap-2">
          <div className="w-8 h-8 border-3 border-brand-500 border-t-transparent rounded-full animate-spin"></div>
          <p className="text-xs text-slate-500 font-medium">Memuat detail permohonan...</p>
        </div>
      </div>
    );
  }

  if (!data) return null;

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Header Bar */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <button
            onClick={() => router.back()}
            className="p-2 bg-white rounded-lg border border-surface-border text-slate-600 hover:text-slate-900 transition-colors shadow-sm"
          >
            <ArrowLeft className="w-4 h-4" />
          </button>
          <div>
            <div className="flex items-center gap-2.5">
              <h1 className="text-xl font-bold text-slate-800">
                Detail Permohonan Surat
              </h1>
              <StatusBadge status={data.status} />
            </div>
            <p className="text-xs text-slate-500 font-mono mt-0.5">
              No. Pengajuan: {data.nomorPengajuan}
            </p>
          </div>
        </div>

        {data.status === 'DISETUJUI' && (
          <Link
            href={`/cetak/${data.id}`}
            target="_blank"
            className="inline-flex items-center gap-2 px-4 py-2 bg-brand-500 hover:bg-brand-600 text-white rounded-lg text-xs font-semibold shadow-sm transition-colors"
          >
            <Printer className="w-4 h-4" />
            <span>Cetak Dokumen Resmi</span>
          </Link>
        )}
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-2 space-y-5">
          {data.nomorSuratResmi && (
            <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-xl flex items-start gap-3">
              <ShieldCheck className="w-6 h-6 text-emerald-600 shrink-0 mt-0.5" />
              <div>
                <p className="text-xs font-semibold uppercase tracking-wider text-emerald-800">
                  Nomor Registrasi Surat Resmi Telah Diterbitkan
                </p>
                <p className="text-base font-bold font-mono text-emerald-900 mt-0.5">
                  {data.nomorSuratResmi}
                </p>
                <p className="text-xs text-emerald-700 mt-1">
                  Surat sah dapat langsung dicetak atau diunduh sebagai berkas PDF resmi.
                </p>
              </div>
            </div>
          )}

          <div className="bg-white rounded-xl border border-surface-border p-6 shadow-sm space-y-4">
            <h2 className="text-sm font-bold text-slate-800 border-b border-surface-border pb-3 flex items-center gap-2">
              <FileText className="w-4 h-4 text-brand-500" />
              <span>Informasi Surat & Maksud Permohonan</span>
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
              <div>
                <span className="font-semibold text-slate-400 uppercase text-[10px]">Jenis Dokumen</span>
                <p className="text-slate-800 font-semibold text-sm mt-0.5">
                  {data.jenisSurat?.namaSurat}
                </p>
                <p className="text-slate-500 font-mono text-[11px]">
                  Kode: {data.jenisSurat?.kodeSurat}
                </p>
              </div>

              <div>
                <span className="font-semibold text-slate-400 uppercase text-[10px]">Tanggal Pengajuan</span>
                <p className="text-slate-800 font-semibold text-sm mt-0.5">
                  {formatDate(data.tanggalPengajuan)}
                </p>
              </div>
            </div>

            <div className="pt-2 border-t border-slate-100 text-xs">
              <span className="font-semibold text-slate-400 uppercase text-[10px]">Keperluan / Alasan</span>
              <p className="text-slate-800 font-medium mt-1 bg-slate-50 p-3 rounded-lg border border-slate-200">
                {data.keperluan}
              </p>
            </div>

            {data.keterangan && (
              <div className="text-xs">
                <span className="font-semibold text-slate-400 uppercase text-[10px]">Keterangan Tambahan</span>
                <p className="text-slate-600 mt-1 bg-slate-50 p-3 rounded-lg border border-slate-200">
                  {data.keterangan}
                </p>
              </div>
            )}

            {data.lampiran && (
              <div className="pt-2 border-t border-slate-100 text-xs">
                <span className="font-semibold text-slate-400 uppercase text-[10px]">Berkas Lampiran</span>
                <div className="mt-1">
                  <a
                    href={data.lampiran}
                    target="_blank"
                    rel="noreferrer"
                    className="inline-flex items-center gap-2 px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium rounded-lg border border-slate-200 transition-colors"
                  >
                    <FileCheck2 className="w-4 h-4 text-brand-500" />
                    <span>Buka / Unduh Berkas Terlampir</span>
                    <ExternalLink className="w-3.5 h-3.5 text-slate-400 ml-1" />
                  </a>
                </div>
              </div>
            )}

            {data.catatanPetugas && (
              <div className="pt-2 border-t border-slate-100 text-xs">
                <span className="font-semibold text-slate-400 uppercase text-[10px]">Catatan Petugas Tata Usaha</span>
                <p className="text-slate-700 mt-1 bg-amber-50 p-3 rounded-lg border border-amber-200">
                  {data.catatanPetugas}
                </p>
              </div>
            )}
          </div>
        </div>

        <div className="space-y-5">
          <div className="bg-white rounded-xl border border-surface-border p-5 shadow-sm space-y-3">
            <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider border-b border-surface-border pb-2 flex items-center gap-2">
              <User className="w-4 h-4 text-brand-500" />
              <span>Data Siswa Pemohon</span>
            </h3>
            <div className="text-xs space-y-2">
              <div>
                <span className="text-slate-400 text-[11px]">Nama Lengkap</span>
                <p className="font-semibold text-slate-800">{data.siswa?.nama}</p>
              </div>
              <div>
                <span className="text-slate-400 text-[11px]">NISN</span>
                <p className="font-mono text-slate-700">{data.siswa?.nisn || '-'}</p>
              </div>
              <div>
                <span className="text-slate-400 text-[11px]">Kelas & Jurusan</span>
                <p className="text-slate-700 font-medium">
                  {data.siswa?.kelas || '-'} ({data.siswa?.jurusan || '-'})
                </p>
              </div>
              <div>
                <span className="text-slate-400 text-[11px]">No. Telepon / WhatsApp</span>
                <p className="text-slate-700">{data.siswa?.noTelepon || '-'}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl border border-surface-border p-5 shadow-sm space-y-3">
            <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider border-b border-surface-border pb-2 flex items-center gap-2">
              <Clock className="w-4 h-4 text-brand-500" />
              <span>Riwayat Aktivitas Status</span>
            </h3>

            <div className="space-y-4 pt-1">
              {data.logs && data.logs.length > 0 ? (
                data.logs.map((log) => (
                  <div key={log.id} className="relative pl-5 text-xs border-l-2 border-slate-200 last:border-l-transparent pb-3">
                    <div className="absolute -left-[5px] top-0 w-2.5 h-2.5 rounded-full bg-brand-500"></div>
                    <p className="font-semibold text-slate-800">
                      Status: {log.statusSesudah}
                    </p>
                    {log.catatan && (
                      <p className="text-slate-600 text-[11px] mt-0.5">{log.catatan}</p>
                    )}
                    <p className="text-[10px] text-slate-400 mt-1">
                      {formatDateTime(log.createdAt)} {log.user?.nama ? `• Oleh ${log.user.nama}` : ''}
                    </p>
                  </div>
                ))
              ) : (
                <p className="text-xs text-slate-400">Belum ada riwayat aktivitas.</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
