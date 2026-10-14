'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { PengajuanItem } from '@/lib/types';
import StatusBadge from '@/components/StatusBadge';
import { formatDate } from '@/lib/utils';
import { api } from '@/lib/api';
import { PlusCircle, Printer, Eye, Trash2 } from 'lucide-react';

export default function RiwayatSiswaPage() {
  const [list, setList] = useState<PengajuanItem[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchRiwayat = async () => {
    setLoading(true);
    try {
      const res = await api.get('/pengajuan');
      setList(res?.data || []);
    } catch (err) {
      console.error('Error load riwayat:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRiwayat();
  }, []);

  const handleCancel = async (id: string) => {
    if (!confirm('Apakah Anda yakin ingin membatalkan pengajuan surat ini?')) return;
    try {
      await api.delete(`/pengajuan/${id}`);
      fetchRiwayat();
    } catch (err: any) {
      alert(err.message || 'Gagal membatalkan pengajuan');
    }
  };

  return (
    <div className="space-y-6">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-slate-800">
            Riwayat Permohonan Surat Saya
          </h1>
          <p className="text-xs text-slate-500 mt-0.5">
            Pantau progres dan unduh surat resmi yang telah disetujui pihak sekolah
          </p>
        </div>

        <Link
          href="/dashboard/pengajuan/baru"
          className="inline-flex items-center gap-2 px-4 py-2 bg-brand-500 hover:bg-brand-600 text-white rounded-lg text-xs font-semibold shadow-sm transition-colors self-start sm:self-auto"
        >
          <PlusCircle className="w-4 h-4" />
          <span>Buat Pengajuan Baru</span>
        </Link>
      </div>

      {/* Table */}
      <div className="bg-white rounded-xl border border-surface-border shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 text-slate-700 border-b border-surface-border font-semibold uppercase text-[11px] tracking-wider">
              <tr>
                <th className="px-5 py-3">No. Pengajuan</th>
                <th className="px-5 py-3">Jenis Surat</th>
                <th className="px-5 py-3">Maksud Keperluan</th>
                <th className="px-5 py-3">Tanggal Pengajuan</th>
                <th className="px-5 py-3">Status</th>
                <th className="px-5 py-3 text-right">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-surface-border">
              {loading ? (
                <tr>
                  <td colSpan={6} className="px-5 py-10 text-center text-slate-400">
                    <div className="flex flex-col items-center justify-center gap-2">
                      <div className="w-6 h-6 border-2 border-brand-500 border-t-transparent rounded-full animate-spin"></div>
                      <span>Memuat riwayat pengajuan...</span>
                    </div>
                  </td>
                </tr>
              ) : list.length === 0 ? (
                <tr>
                  <td colSpan={6} className="px-5 py-10 text-center text-slate-400">
                    <p>Anda belum pernah mengajukan permohonan surat.</p>
                    <Link
                      href="/dashboard/pengajuan/baru"
                      className="inline-block mt-2 text-xs font-semibold text-brand-600 hover:underline"
                    >
                      Ajukan Surat Sekarang &rarr;
                    </Link>
                  </td>
                </tr>
              ) : (
                list.map((item) => (
                  <tr key={item.id} className="hover:bg-slate-50 transition-colors">
                    <td className="px-5 py-3.5 font-mono font-medium text-slate-800 whitespace-nowrap">
                      {item.nomorPengajuan}
                      {item.nomorSuratResmi && (
                        <p className="font-sans text-[10px] text-emerald-600 font-semibold mt-0.5">
                          {item.nomorSuratResmi}
                        </p>
                      )}
                    </td>
                    <td className="px-5 py-3.5">
                      <span className="font-semibold text-slate-800">
                        {item.jenisSurat?.namaSurat}
                      </span>
                    </td>
                    <td className="px-5 py-3.5 max-w-[240px] truncate text-slate-600" title={item.keperluan}>
                      {item.keperluan}
                    </td>
                    <td className="px-5 py-3.5 whitespace-nowrap">
                      {formatDate(item.tanggalPengajuan)}
                    </td>
                    <td className="px-5 py-3.5 whitespace-nowrap">
                      <StatusBadge status={item.status} />
                    </td>
                    <td className="px-5 py-3.5 text-right whitespace-nowrap">
                      <div className="inline-flex items-center gap-1.5">
                        <Link
                          href={`/dashboard/pengajuan/${item.id}`}
                          className="p-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded transition-colors"
                          title="Lihat Detail"
                        >
                          <Eye className="w-4 h-4" />
                        </Link>

                        {item.status === 'DISETUJUI' && (
                          <Link
                            href={`/cetak/${item.id}`}
                            target="_blank"
                            className="inline-flex items-center gap-1 px-2.5 py-1 bg-brand-50 hover:bg-brand-100 text-brand-600 rounded border border-brand-200 text-xs font-semibold transition-colors"
                            title="Cetak Surat Resmi"
                          >
                            <Printer className="w-3.5 h-3.5" />
                            <span>Cetak</span>
                          </Link>
                        )}

                        {item.status === 'MENUNGGU' && (
                          <button
                            onClick={() => handleCancel(item.id)}
                            className="p-1.5 text-rose-500 hover:text-rose-700 hover:bg-rose-50 rounded transition-colors"
                            title="Batalkan Pengajuan"
                          >
                            <Trash2 className="w-4 h-4" />
                          </button>
                        )}
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
