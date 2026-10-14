'use client';

import React, { useState, useEffect } from 'react';
import { PengajuanItem, JenisSuratItem } from '@/lib/types';
import { formatDate } from '@/lib/utils';
import { api } from '@/lib/api';
import { Printer, Search } from 'lucide-react';

export default function LaporanPage() {
  const [list, setList] = useState<PengajuanItem[]>([]);
  const [jenisList, setJenisList] = useState<JenisSuratItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Filters
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [status, setStatus] = useState('');
  const [jenisSuratId, setJenisSuratId] = useState('');

  const fetchLaporan = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (startDate) params.append('startDate', startDate);
      if (endDate) params.append('endDate', endDate);
      if (status) params.append('status', status);
      if (jenisSuratId) params.append('jenisSuratId', jenisSuratId);

      const [resPengajuan, resJenis] = await Promise.all([
        api.get(`/pengajuan?${params.toString()}`),
        api.get('/jenis-surat'),
      ]);

      setList(resPengajuan?.data || []);
      setJenisList(resJenis?.data || []);
    } catch (err) {
      console.error('Error load laporan:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLaporan();
  }, []);

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="space-y-6">
      {/* Title Bar (Hidden when printing) */}
      <div className="no-print flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-slate-800">
            Laporan & Rekapitulasi Pengajuan Surat
          </h1>
          <p className="text-xs text-slate-500 mt-0.5">
            Rekap seluruh permohonan surat masuk, persetujuan, dan penerbitan nomor surat
          </p>
        </div>

        <button
          onClick={handlePrint}
          className="inline-flex items-center gap-2 px-4 py-2 bg-navy-900 hover:bg-slate-800 text-white rounded-lg text-xs font-semibold shadow-sm transition-colors self-start sm:self-auto"
        >
          <Printer className="w-4 h-4" />
          <span>Cetak / Ekspor Laporan</span>
        </button>
      </div>

      {/* Filter Panel (Hidden when printing) */}
      <div className="no-print bg-white rounded-xl border border-surface-border p-4 shadow-sm space-y-3">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
          <div>
            <label className="block text-[11px] font-semibold text-slate-500 uppercase tracking-wider mb-1">
              Mulai Tanggal
            </label>
            <input
              type="date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              className="w-full px-3 py-1.5 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-800 focus:outline-none focus:bg-white"
            />
          </div>

          <div>
            <label className="block text-[11px] font-semibold text-slate-500 uppercase tracking-wider mb-1">
              Sampai Tanggal
            </label>
            <input
              type="date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              className="w-full px-3 py-1.5 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-800 focus:outline-none focus:bg-white"
            />
          </div>

          <div>
            <label className="block text-[11px] font-semibold text-slate-500 uppercase tracking-wider mb-1">
              Status Pengajuan
            </label>
            <select
              value={status}
              onChange={(e) => setStatus(e.target.value)}
              className="w-full px-3 py-1.5 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-800 focus:outline-none focus:bg-white"
            >
              <option value="">Semua Status</option>
              <option value="MENUNGGU">Menunggu</option>
              <option value="DIPROSES">Diproses</option>
              <option value="DISETUJUI">Disetujui</option>
              <option value="DITOLAK">Ditolak</option>
            </select>
          </div>

          <div>
            <label className="block text-[11px] font-semibold text-slate-500 uppercase tracking-wider mb-1">
              Jenis Dokumen
            </label>
            <select
              value={jenisSuratId}
              onChange={(e) => setJenisSuratId(e.target.value)}
              className="w-full px-3 py-1.5 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-800 focus:outline-none focus:bg-white"
            >
              <option value="">Semua Jenis</option>
              {jenisList.map((j) => (
                <option key={j.id} value={j.id}>
                  {j.namaSurat}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="flex justify-end gap-2 pt-1 border-t border-slate-100">
          <button
            onClick={() => {
              setStartDate('');
              setEndDate('');
              setStatus('');
              setJenisSuratId('');
              setTimeout(fetchLaporan, 10);
            }}
            className="px-3 py-1.5 text-xs font-semibold text-slate-600 hover:bg-slate-100 rounded-lg"
          >
            Reset Filter
          </button>
          <button
            onClick={fetchLaporan}
            className="px-4 py-1.5 text-xs font-semibold text-white bg-brand-500 hover:bg-brand-600 rounded-lg shadow-sm flex items-center gap-1.5"
          >
            <Search className="w-3.5 h-3.5" />
            <span>Terapkan Filter</span>
          </button>
        </div>
      </div>

      {/* Report Sheet Area */}
      <div className="bg-white rounded-xl border border-surface-border p-6 shadow-sm print-area">
        {/* Print Header */}
        <div className="border-b-2 border-slate-800 pb-4 mb-4 text-center">
          <h2 className="text-base font-bold uppercase tracking-wider text-slate-900">
            {process.env.NEXT_PUBLIC_SCHOOL_NAME || 'SMK NEGERI 1 CONTOH KOTA'}
          </h2>
          <p className="text-xs text-slate-600">
            {process.env.NEXT_PUBLIC_SCHOOL_ADDRESS || 'Jl. Pendidikan No. 123, Komplek Sekolah Menengah'}
          </p>
          <h3 className="text-sm font-bold text-slate-800 mt-3 underline">
            REKAPITULASI PELAYANAN PENGAJUAN SURAT SISWA
          </h3>
          <p className="text-[11px] text-slate-500 mt-0.5">
            Periode: {startDate ? formatDate(startDate) : 'Awal'} s.d. {endDate ? formatDate(endDate) : 'Sekarang'}
          </p>
        </div>

        {/* Quick summary numbers */}
        <div className="grid grid-cols-4 gap-2 mb-4 p-3 bg-slate-50 border border-slate-200 rounded-lg text-center text-xs">
          <div>
            <span className="text-slate-500 text-[10px] uppercase font-semibold">Total Pengajuan</span>
            <p className="text-base font-bold text-slate-800">{list.length}</p>
          </div>
          <div>
            <span className="text-slate-500 text-[10px] uppercase font-semibold">Disetujui</span>
            <p className="text-base font-bold text-emerald-600">
              {list.filter((l) => l.status === 'DISETUJUI').length}
            </p>
          </div>
          <div>
            <span className="text-slate-500 text-[10px] uppercase font-semibold">Menunggu/Proses</span>
            <p className="text-base font-bold text-amber-600">
              {list.filter((l) => l.status === 'MENUNGGU' || l.status === 'DIPROSES').length}
            </p>
          </div>
          <div>
            <span className="text-slate-500 text-[10px] uppercase font-semibold">Ditolak</span>
            <p className="text-base font-bold text-rose-600">
              {list.filter((l) => l.status === 'DITOLAK').length}
            </p>
          </div>
        </div>

        {/* Table */}
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border border-slate-300">
            <thead className="bg-slate-100 text-slate-800 font-semibold border-b border-slate-300">
              <tr>
                <th className="px-3 py-2 border-r border-slate-300">No.</th>
                <th className="px-3 py-2 border-r border-slate-300">No. Pengajuan</th>
                <th className="px-3 py-2 border-r border-slate-300">No. Surat Resmi</th>
                <th className="px-3 py-2 border-r border-slate-300">Nama Siswa</th>
                <th className="px-3 py-2 border-r border-slate-300">Kelas</th>
                <th className="px-3 py-2 border-r border-slate-300">Jenis Dokumen</th>
                <th className="px-3 py-2 border-r border-slate-300">Keperluan</th>
                <th className="px-3 py-2 border-r border-slate-300">Tanggal</th>
                <th className="px-3 py-2 text-center">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {list.length === 0 ? (
                <tr>
                  <td colSpan={9} className="px-4 py-8 text-center text-slate-400">
                    Tidak ada data untuk periode dan kriteria ini.
                  </td>
                </tr>
              ) : (
                list.map((item, idx) => (
                  <tr key={item.id} className="hover:bg-slate-50">
                    <td className="px-3 py-2 border-r border-slate-300 text-center">{idx + 1}</td>
                    <td className="px-3 py-2 border-r border-slate-300 font-mono">{item.nomorPengajuan}</td>
                    <td className="px-3 py-2 border-r border-slate-300 font-mono text-[11px] text-slate-800 font-semibold">
                      {item.nomorSuratResmi || '-'}
                    </td>
                    <td className="px-3 py-2 border-r border-slate-300 font-semibold text-slate-800">
                      {item.siswa?.nama}
                    </td>
                    <td className="px-3 py-2 border-r border-slate-300">{item.siswa?.kelas}</td>
                    <td className="px-3 py-2 border-r border-slate-300">{item.jenisSurat?.namaSurat}</td>
                    <td className="px-3 py-2 border-r border-slate-300 max-w-[200px] truncate">{item.keperluan}</td>
                    <td className="px-3 py-2 border-r border-slate-300 whitespace-nowrap">
                      {formatDate(item.tanggalPengajuan)}
                    </td>
                    <td className="px-3 py-2 text-center whitespace-nowrap">
                      <span
                        className={`inline-block px-2 py-0.5 rounded text-[10px] font-bold ${
                          item.status === 'DISETUJUI'
                            ? 'bg-emerald-100 text-emerald-800'
                            : item.status === 'MENUNGGU'
                            ? 'bg-amber-100 text-amber-800'
                            : item.status === 'DIPROSES'
                            ? 'bg-blue-100 text-blue-800'
                            : 'bg-rose-100 text-rose-800'
                        }`}
                      >
                        {item.status}
                      </span>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>

        {/* Print Sign Footer */}
        <div className="hidden print:flex justify-between items-end mt-12 pt-8 text-xs text-slate-800">
          <div>
            <p>Mengetahui,</p>
            <p className="font-semibold mt-1">Kepala Sekolah</p>
            <div className="h-16"></div>
            <p className="font-bold underline">Drs. H. Mulyadi, M.Pd.</p>
            <p className="text-[11px] text-slate-600">NIP. 19680512 199403 1 004</p>
          </div>
          <div className="text-right">
            <p>Dicetak Pada: {formatDate(new Date())}</p>
            <p className="font-semibold mt-1">Koordinator Tata Usaha</p>
            <div className="h-16"></div>
            <p className="font-bold underline">Rina Kartika, S.AP.</p>
            <p className="text-[11px] text-slate-600">NIP. 19820315 200801 2 011</p>
          </div>
        </div>
      </div>
    </div>
  );
}
