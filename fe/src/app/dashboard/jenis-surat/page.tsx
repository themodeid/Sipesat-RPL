'use client';

import React, { useState, useEffect } from 'react';
import Modal from '@/components/Modal';
import { api } from '@/lib/api';
import { Plus, Edit2, CheckCircle2, XCircle } from 'lucide-react';

export default function MasterJenisSuratPage() {
  const [list, setList] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  // Modal form state
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editId, setEditId] = useState('');
  const [kodeSurat, setKodeSurat] = useState('');
  const [namaSurat, setNamaSurat] = useState('');
  const [deskripsi, setDeskripsi] = useState('');
  const [persyaratan, setPersyaratan] = useState('');
  const [formatNomor, setFormatNomor] = useState('421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}');
  const [submitting, setSubmitting] = useState(false);

  const fetchList = async () => {
    setLoading(true);
    try {
      const res = await api.get('/jenis-surat');
      setList(res?.data || []);
    } catch (err) {
      console.error('Error load jenis surat:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchList();
  }, []);

  const openAddModal = () => {
    setIsEditing(false);
    setEditId('');
    setKodeSurat('');
    setNamaSurat('');
    setDeskripsi('');
    setPersyaratan('');
    setFormatNomor('421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}');
    setIsModalOpen(true);
  };

  const openEditModal = (item: any) => {
    setIsEditing(true);
    setEditId(item.id);
    setKodeSurat(item.kodeSurat);
    setNamaSurat(item.namaSurat);
    setDeskripsi(item.deskripsi);
    setPersyaratan(item.persyaratan || '');
    setFormatNomor(item.formatNomor);
    setIsModalOpen(true);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      if (isEditing) {
        await api.put('/jenis-surat', {
          id: editId,
          kodeSurat,
          namaSurat,
          deskripsi,
          persyaratan,
          formatNomor,
        });
      } else {
        await api.post('/jenis-surat', {
          kodeSurat,
          namaSurat,
          deskripsi,
          persyaratan,
          formatNomor,
        });
      }

      setIsModalOpen(false);
      fetchList();
    } catch (err: any) {
      alert(err.message || 'Gagal menyimpan jenis surat');
    } finally {
      setSubmitting(false);
    }
  };

  const toggleActive = async (item: any) => {
    try {
      await api.put('/jenis-surat', { id: item.id, isActive: !item.isActive });
      fetchList();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="space-y-6">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-slate-800">
            Master Jenis & Template Surat
          </h1>
          <p className="text-xs text-slate-500 mt-0.5">
            Konfigurasi jenis dokumen yang dapat diajukan siswa beserta format penomoran resmi
          </p>
        </div>

        <button
          onClick={openAddModal}
          className="inline-flex items-center gap-2 px-4 py-2 bg-brand-500 hover:bg-brand-600 text-white rounded-lg text-xs font-semibold shadow-sm transition-colors self-start sm:self-auto"
        >
          <Plus className="w-4 h-4" />
          <span>Tambah Jenis Surat</span>
        </button>
      </div>

      {/* Table */}
      <div className="bg-white rounded-xl border border-surface-border shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 text-slate-700 border-b border-surface-border font-semibold uppercase text-[11px] tracking-wider">
              <tr>
                <th className="px-5 py-3">Kode</th>
                <th className="px-5 py-3">Nama Surat</th>
                <th className="px-5 py-3">Deskripsi & Syarat</th>
                <th className="px-5 py-3">Format Penomoran</th>
                <th className="px-5 py-3">Total Pengajuan</th>
                <th className="px-5 py-3">Status</th>
                <th className="px-5 py-3 text-right">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-surface-border">
              {loading ? (
                <tr>
                  <td colSpan={7} className="px-5 py-8 text-center text-slate-400">
                    Memuat data master...
                  </td>
                </tr>
              ) : list.length === 0 ? (
                <tr>
                  <td colSpan={7} className="px-5 py-8 text-center text-slate-400">
                    Belum ada jenis surat yang dikonfigurasi.
                  </td>
                </tr>
              ) : (
                list.map((item) => (
                  <tr key={item.id} className="hover:bg-slate-50 transition-colors">
                    <td className="px-5 py-3.5 font-mono font-bold text-slate-800">
                      {item.kodeSurat}
                    </td>
                    <td className="px-5 py-3.5 font-semibold text-slate-800">
                      {item.namaSurat}
                    </td>
                    <td className="px-5 py-3.5 max-w-[260px]">
                      <p className="line-clamp-2 text-slate-600">{item.deskripsi}</p>
                      {item.persyaratan && (
                        <p className="text-[10px] text-slate-400 mt-1 line-clamp-1">
                          Syarat: {item.persyaratan}
                        </p>
                      )}
                    </td>
                    <td className="px-5 py-3.5 font-mono text-[11px] text-slate-700">
                      {item.formatNomor}
                    </td>
                    <td className="px-5 py-3.5 font-semibold text-slate-700">
                      {item._count?.pengajuan || 0} Pengajuan
                    </td>
                    <td className="px-5 py-3.5">
                      <button
                        onClick={() => toggleActive(item)}
                        className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold ${
                          item.isActive
                            ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                            : 'bg-slate-100 text-slate-500 border border-slate-200'
                        }`}
                      >
                        {item.isActive ? (
                          <>
                            <CheckCircle2 className="w-3 h-3" />
                            <span>Aktif</span>
                          </>
                        ) : (
                          <>
                            <XCircle className="w-3 h-3" />
                            <span>Non-Aktif</span>
                          </>
                        )}
                      </button>
                    </td>
                    <td className="px-5 py-3.5 text-right whitespace-nowrap">
                      <button
                        onClick={() => openEditModal(item)}
                        className="p-1.5 text-slate-600 hover:text-brand-600 hover:bg-slate-100 rounded transition-colors"
                        title="Edit Jenis Surat"
                      >
                        <Edit2 className="w-4 h-4" />
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal Add / Edit */}
      <Modal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title={isEditing ? 'Ubah Master Jenis Surat' : 'Tambah Master Jenis Surat Baru'}
        maxWidth="lg"
      >
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                Kode Surat (Unik)
              </label>
              <input
                type="text"
                required
                value={kodeSurat}
                onChange={(e) => setKodeSurat(e.target.value)}
                placeholder="Contoh: SK-AKTIF"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800 font-mono"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                Nama Surat Resmi
              </label>
              <input
                type="text"
                required
                value={namaSurat}
                onChange={(e) => setNamaSurat(e.target.value)}
                placeholder="Contoh: Surat Keterangan Siswa Aktif"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
              Deskripsi Fungsi Surat
            </label>
            <textarea
              required
              rows={2}
              value={deskripsi}
              onChange={(e) => setDeskripsi(e.target.value)}
              placeholder="Jelaskan peruntukan dokumen surat ini..."
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
              Persyaratan Dokumen (Daftar per baris)
            </label>
            <textarea
              rows={3}
              value={persyaratan}
              onChange={(e) => setPersyaratan(e.target.value)}
              placeholder="1. Fotokopi Kartu Pelajar&#10;2. Bebas Tunggakan SPP..."
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
              Format Penomoran Surat
            </label>
            <input
              type="text"
              required
              value={formatNomor}
              onChange={(e) => setFormatNomor(e.target.value)}
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800 font-mono"
            />
            <p className="text-[11px] text-slate-400 mt-1">
              Gunakan tag: <code className="text-slate-600 font-mono">&#123;NOMOR&#125;</code>, <code className="text-slate-600 font-mono">&#123;BULAN_ROMAWI&#125;</code>, <code className="text-slate-600 font-mono">&#123;TAHUN&#125;</code>
            </p>
          </div>

          <div className="flex items-center justify-end gap-2 pt-3 border-t border-slate-100">
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
              className="px-4 py-2 text-xs font-semibold text-white bg-brand-500 hover:bg-brand-600 rounded-lg shadow-sm"
            >
              {submitting ? 'Menyimpan...' : isEditing ? 'Simpan Perubahan' : 'Tambah Jenis Surat'}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
}
