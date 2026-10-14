'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { PengajuanItem, JenisSuratItem, StatusPengajuan } from '@/lib/types';
import StatusBadge from '@/components/StatusBadge';
import Modal from '@/components/Modal';
import { formatDate } from '@/lib/utils';
import { api } from '@/lib/api';
import {
  FileText,
  Search,
  CheckCircle,
  XCircle,
  Clock,
  Printer,
  Eye,
  RefreshCw,
  ExternalLink,
} from 'lucide-react';

export default function DataPengajuanPage() {
  const [list, setList] = useState<PengajuanItem[]>([]);
  const [jenisList, setJenisList] = useState<JenisSuratItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Filters
  const [activeStatus, setActiveStatus] = useState<string>('SEMUA');
  const [search, setSearch] = useState('');
  const [selectedJenisId, setSelectedJenisId] = useState('');

  // Modal State
  const [selectedItem, setSelectedItem] = useState<PengajuanItem | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [targetStatus, setTargetStatus] = useState<StatusPengajuan>('DISETUJUI');
  const [catatan, setCatatan] = useState('');
  const [nomorSuratCustom, setNomorSuratCustom] = useState('');
  const [submitting, setSubmitting] = useState(false);

  const fetchPengajuan = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (activeStatus !== 'SEMUA') params.append('status', activeStatus);
      if (search) params.append('search', search);
      if (selectedJenisId) params.append('jenisSuratId', selectedJenisId);

      const [resPengajuan, resJenis] = await Promise.all([
        api.get(`/pengajuan?${params.toString()}`),
        api.get('/jenis-surat'),
      ]);

      setList(resPengajuan?.data || []);
      setJenisList(resJenis?.data || []);
    } catch (err) {
      console.error('Gagal mengambil data pengajuan:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPengajuan();
  }, [activeStatus, selectedJenisId]);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetchPengajuan();
  };

  const handleOpenActionModal = (item: PengajuanItem, status: StatusPengajuan) => {
    setSelectedItem(item);
    setTargetStatus(status);
    setCatatan(item.catatanPetugas || '');
    setNomorSuratCustom(item.nomorSuratResmi || '');
    setIsModalOpen(true);
  };

  const handleUpdateStatus = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedItem) return;

    setSubmitting(true);
    try {
      await api.patch(`/pengajuan/${selectedItem.id}`, {
        status: targetStatus,
        catatanPetugas: catatan,
        nomorSuratResmi: nomorSuratCustom.trim() || undefined,
      });

      setIsModalOpen(false);
      fetchPengajuan();
    } catch (err: any) {
      alert(err.message || 'Gagal memperbarui status');
    } finally {
      setSubmitting(false);
    }
  };

  const statusTabs = [
    { label: 'Semua Status', value: 'SEMUA' },
    { label: 'Menunggu', value: 'MENUNGGU' },
    { label: 'Diproses', value: 'DIPROSES' },
    { label: 'Disetujui', value: 'DISETUJUI' },
    { label: 'Ditolak', value: 'DITOLAK' },
  ];

  return (
    <div className="space-y-6">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-slate-800">
            Verifikasi & Pengelolaan Pengajuan Surat
          </h1>
          <p className="text-xs text-slate-500 mt-0.5">
            Tinjau berkas permohonan siswa, tetapkan nomor surat resmi, dan berikan persetujuan
          </p>
        </div>
      </div>

      {/* Filter Bar */}
      <div className="bg-white rounded-xl border border-surface-border p-4 shadow-sm space-y-4">
        {/* Status Tabs */}
        <div className="flex items-center gap-1 overflow-x-auto pb-1 border-b border-surface-border">
          {statusTabs.map((tab) => (
            <button
              key={tab.value}
              onClick={() => setActiveStatus(tab.value)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-colors ${
                activeStatus === tab.value
                  ? 'bg-brand-500 text-white shadow-sm'
                  : 'text-slate-600 hover:bg-slate-100'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Search & Kategori */}
        <div className="flex flex-col md:flex-row gap-3">
          <form onSubmit={handleSearchSubmit} className="flex-1 relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
            <input
              type="text"
              placeholder="Cari nama siswa, NISN, no. pengajuan, keperluan..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full pl-9 pr-4 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 focus:border-brand-500 text-slate-800"
            />
          </form>

          <div className="w-full md:w-64">
            <select
              value={selectedJenisId}
              onChange={(e) => setSelectedJenisId(e.target.value)}
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 focus:border-brand-500 text-slate-800"
            >
              <option value="">Semua Jenis Dokumen</option>
              {jenisList.map((j) => (
                <option key={j.id} value={j.id}>
                  {j.namaSurat}
                </option>
              ))}
            </select>
          </div>

          <button
            onClick={fetchPengajuan}
            className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-semibold flex items-center justify-center gap-1.5 transition-colors"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span>Segarkan</span>
          </button>
        </div>
      </div>

      {/* Main Table */}
      <div className="bg-white rounded-xl border border-surface-border shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 text-slate-700 border-b border-surface-border font-semibold uppercase text-[11px] tracking-wider">
              <tr>
                <th className="px-5 py-3">No. Pengajuan</th>
                <th className="px-5 py-3">Data Siswa Pemohon</th>
                <th className="px-5 py-3">Jenis Surat</th>
                <th className="px-5 py-3">Maksud Keperluan</th>
                <th className="px-5 py-3">Tanggal</th>
                <th className="px-5 py-3">Status</th>
                <th className="px-5 py-3 text-right">Tindakan Petugas</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-surface-border">
              {loading ? (
                <tr>
                  <td colSpan={7} className="px-5 py-10 text-center text-slate-400">
                    <div className="flex flex-col items-center justify-center gap-2">
                      <div className="w-6 h-6 border-2 border-brand-500 border-t-transparent rounded-full animate-spin"></div>
                      <span>Memuat data pengajuan...</span>
                    </div>
                  </td>
                </tr>
              ) : list.length === 0 ? (
                <tr>
                  <td colSpan={7} className="px-5 py-10 text-center text-slate-400">
                    Tidak ditemukan pengajuan surat dengan filter ini.
                  </td>
                </tr>
              ) : (
                list.map((item) => (
                  <tr key={item.id} className="hover:bg-slate-50 transition-colors">
                    <td className="px-5 py-3.5 font-mono font-medium text-slate-800 whitespace-nowrap">
                      {item.nomorPengajuan}
                      {item.nomorSuratResmi && (
                        <p className="font-sans text-[10px] text-brand-600 font-semibold mt-0.5">
                          {item.nomorSuratResmi}
                        </p>
                      )}
                    </td>
                    <td className="px-5 py-3.5">
                      <p className="font-semibold text-slate-800">{item.siswa?.nama}</p>
                      <p className="text-[11px] text-slate-400">
                        NISN: {item.siswa?.nisn} &bull; {item.siswa?.kelas}
                      </p>
                    </td>
                    <td className="px-5 py-3.5">
                      <span className="font-medium text-slate-800">
                        {item.jenisSurat?.namaSurat}
                      </span>
                    </td>
                    <td className="px-5 py-3.5 max-w-[220px]">
                      <p className="truncate text-slate-700" title={item.keperluan}>
                        {item.keperluan}
                      </p>
                      {item.lampiran && (
                        <a
                          href={item.lampiran}
                          target="_blank"
                          rel="noreferrer"
                          className="text-[11px] text-brand-600 hover:underline inline-flex items-center gap-1 mt-0.5"
                        >
                          <span>Lampiran Berkas</span>
                          <ExternalLink className="w-3 h-3" />
                        </a>
                      )}
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
                          title="Lihat Detail & Log"
                        >
                          <Eye className="w-4 h-4" />
                        </Link>

                        {item.status === 'DISETUJUI' && (
                          <Link
                            href={`/cetak/${item.id}`}
                            target="_blank"
                            className="p-1.5 text-brand-600 hover:bg-brand-50 rounded transition-colors"
                            title="Cetak Surat Resmi"
                          >
                            <Printer className="w-4 h-4" />
                          </Link>
                        )}

                        {item.status !== 'DISETUJUI' && (
                          <button
                            onClick={() => handleOpenActionModal(item, 'DISETUJUI')}
                            className="px-2 py-1 bg-emerald-50 hover:bg-emerald-100 text-emerald-700 rounded border border-emerald-200 text-[11px] font-semibold transition-colors flex items-center gap-1"
                          >
                            <CheckCircle className="w-3 h-3 text-emerald-600" />
                            <span>Setujui</span>
                          </button>
                        )}

                        {item.status === 'MENUNGGU' && (
                          <button
                            onClick={() => handleOpenActionModal(item, 'DIPROSES')}
                            className="px-2 py-1 bg-blue-50 hover:bg-blue-100 text-blue-700 rounded border border-blue-200 text-[11px] font-semibold transition-colors flex items-center gap-1"
                          >
                            <Clock className="w-3 h-3 text-blue-600" />
                            <span>Proses</span>
                          </button>
                        )}

                        {item.status !== 'DITOLAK' && item.status !== 'DISETUJUI' && (
                          <button
                            onClick={() => handleOpenActionModal(item, 'DITOLAK')}
                            className="px-2 py-1 bg-rose-50 hover:bg-rose-100 text-rose-700 rounded border border-rose-200 text-[11px] font-semibold transition-colors flex items-center gap-1"
                          >
                            <XCircle className="w-3 h-3 text-rose-600" />
                            <span>Tolak</span>
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

      {/* Action / Verification Modal */}
      <Modal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title={`Konfirmasi Verifikasi: ${targetStatus}`}
        maxWidth="md"
      >
        <form onSubmit={handleUpdateStatus} className="space-y-4">
          <div className="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-1">
            <p>
              <span className="font-semibold text-slate-700">Nomor Pengajuan:</span>{' '}
              <span className="font-mono">{selectedItem?.nomorPengajuan}</span>
            </p>
            <p>
              <span className="font-semibold text-slate-700">Pemohon:</span>{' '}
              {selectedItem?.siswa?.nama} ({selectedItem?.siswa?.kelas})
            </p>
            <p>
              <span className="font-semibold text-slate-700">Jenis Surat:</span>{' '}
              {selectedItem?.jenisSurat?.namaSurat}
            </p>
          </div>

          {targetStatus === 'DISETUJUI' && (
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                Nomor Surat Resmi Sekolah (Opsional / Otomatis)
              </label>
              <input
                type="text"
                placeholder="Biarkan kosong untuk penomoran otomatis"
                value={nomorSuratCustom}
                onChange={(e) => setNomorSuratCustom(e.target.value)}
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
              />
              <p className="text-[11px] text-slate-400 mt-1">
                Format standar: {selectedItem?.jenisSurat?.formatNomor}
              </p>
            </div>
          )}

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
              {targetStatus === 'DITOLAK'
                ? 'Alasan Penolakan (Wajib Diisi)'
                : 'Catatan Petugas (Opsional)'}
            </label>
            <textarea
              required={targetStatus === 'DITOLAK'}
              rows={3}
              placeholder={
                targetStatus === 'DITOLAK'
                  ? 'Jelaskan alasan penolakan, contoh: Syarat fotokopi kartu pelajar belum disertakan...'
                  : 'Catatan pengambilan surat / pengesahan...'
              }
              value={catatan}
              onChange={(e) => setCatatan(e.target.value)}
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
            />
          </div>

          <div className="flex items-center justify-end gap-2 pt-2 border-t border-slate-100">
            <button
              type="button"
              onClick={() => setIsModalOpen(false)}
              className="px-3 py-2 text-xs font-semibold text-slate-600 hover:bg-slate-100 rounded-lg"
            >
              Batal
            </button>
            <button
              type="submit"
              disabled={submitting}
              className={`px-4 py-2 text-xs font-semibold text-white rounded-lg transition-colors ${
                targetStatus === 'DISETUJUI'
                  ? 'bg-emerald-600 hover:bg-emerald-700'
                  : targetStatus === 'DITOLAK'
                  ? 'bg-rose-600 hover:bg-rose-700'
                  : 'bg-brand-500 hover:bg-brand-600'
              }`}
            >
              {submitting ? 'Menyimpan...' : `Simpan Status: ${targetStatus}`}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
}
