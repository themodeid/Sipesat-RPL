'use client';

import React, { useState, useEffect } from 'react';
import { Plus, Search, RefreshCw } from 'lucide-react';
import Modal from '@/components/Modal';
import { api } from '@/lib/api';

export default function MasterSiswaPage() {
  const [list, setList] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');

  // Modal State
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [nisn, setNisn] = useState('');
  const [nama, setNama] = useState('');
  const [email, setEmail] = useState('');
  const [kelas, setKelas] = useState('');
  const [jurusan, setJurusan] = useState('');
  const [noTelepon, setNoTelepon] = useState('');
  const [password, setPassword] = useState('siswa123');
  const [submitting, setSubmitting] = useState(false);

  const fetchSiswa = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (search) params.append('search', search);

      const res = await api.get(`/siswa?${params.toString()}`);
      setList(res?.data || []);
    } catch (err) {
      console.error('Error load siswa:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSiswa();
  }, []);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetchSiswa();
  };

  const handleAddSiswa = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);

    try {
      await api.post('/siswa', {
        nisn,
        nama,
        email: email || null,
        kelas,
        jurusan: jurusan || null,
        noTelepon: noTelepon || null,
        password,
      });

      setIsModalOpen(false);
      setNisn('');
      setNama('');
      setEmail('');
      setKelas('');
      setJurusan('');
      setNoTelepon('');
      fetchSiswa();
    } catch (err: any) {
      alert(err.message || 'Gagal menambahkan data siswa');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-slate-800">
            Master Data Siswa
          </h1>
          <p className="text-xs text-slate-500 mt-0.5">
            Daftar profil siswa sekolah yang berhak mengajukan surat administrasi
          </p>
        </div>

        <button
          onClick={() => setIsModalOpen(true)}
          className="inline-flex items-center gap-2 px-4 py-2 bg-brand-500 hover:bg-brand-600 text-white rounded-lg text-xs font-semibold shadow-sm transition-colors self-start sm:self-auto"
        >
          <Plus className="w-4 h-4" />
          <span>Tambah Siswa Baru</span>
        </button>
      </div>

      {/* Filter & Search */}
      <div className="bg-white rounded-xl border border-surface-border p-4 shadow-sm flex flex-col sm:flex-row gap-3">
        <form onSubmit={handleSearchSubmit} className="flex-1 relative">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
          <input
            type="text"
            placeholder="Cari berdasarkan NISN, Nama, atau Kelas..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-9 pr-4 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
          />
        </form>

        <button
          onClick={fetchSiswa}
          className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-semibold flex items-center justify-center gap-1.5 transition-colors"
        >
          <RefreshCw className="w-3.5 h-3.5" />
          <span>Segarkan</span>
        </button>
      </div>

      {/* Table */}
      <div className="bg-white rounded-xl border border-surface-border shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 text-slate-700 border-b border-surface-border font-semibold uppercase text-[11px] tracking-wider">
              <tr>
                <th className="px-5 py-3">NISN</th>
                <th className="px-5 py-3">Nama Lengkap Siswa</th>
                <th className="px-5 py-3">Kelas & Jurusan</th>
                <th className="px-5 py-3">Kontak / Email</th>
                <th className="px-5 py-3 text-center">Total Pengajuan</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-surface-border">
              {loading ? (
                <tr>
                  <td colSpan={5} className="px-5 py-8 text-center text-slate-400">
                    Memuat data siswa...
                  </td>
                </tr>
              ) : list.length === 0 ? (
                <tr>
                  <td colSpan={5} className="px-5 py-8 text-center text-slate-400">
                    Tidak ditemukan data siswa.
                  </td>
                </tr>
              ) : (
                list.map((item) => (
                  <tr key={item.id} className="hover:bg-slate-50 transition-colors">
                    <td className="px-5 py-3.5 font-mono font-bold text-slate-800">
                      {item.nisn || '-'}
                    </td>
                    <td className="px-5 py-3.5 font-semibold text-slate-800">
                      {item.nama}
                    </td>
                    <td className="px-5 py-3.5">
                      <span className="font-medium text-slate-700">{item.kelas || '-'}</span>
                      {item.jurusan && (
                        <p className="text-[11px] text-slate-400">{item.jurusan}</p>
                      )}
                    </td>
                    <td className="px-5 py-3.5 text-slate-600">
                      <p>{item.noTelepon || '-'}</p>
                      <p className="text-[11px] text-slate-400">{item.email || '-'}</p>
                    </td>
                    <td className="px-5 py-3.5 text-center font-bold text-brand-600">
                      {item._count?.pengajuan || 0}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal Tambah Siswa */}
      <Modal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title="Pendaftaran Data Siswa Baru"
        maxWidth="lg"
      >
        <form onSubmit={handleAddSiswa} className="space-y-4">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                NISN (Nomor Induk)
              </label>
              <input
                type="text"
                required
                value={nisn}
                onChange={(e) => setNisn(e.target.value)}
                placeholder="Contoh: 0081234567"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800 font-mono"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                Nama Lengkap
              </label>
              <input
                type="text"
                required
                value={nama}
                onChange={(e) => setNama(e.target.value)}
                placeholder="Nama lengkap siswa"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
              />
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                Kelas
              </label>
              <input
                type="text"
                required
                value={kelas}
                onChange={(e) => setKelas(e.target.value)}
                placeholder="Contoh: XII RPL 1"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                Kompetensi Keahlian / Jurusan
              </label>
              <input
                type="text"
                value={jurusan}
                onChange={(e) => setJurusan(e.target.value)}
                placeholder="Contoh: Rekayasa Perangkat Lunak"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
              />
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                No. Telepon / WhatsApp
              </label>
              <input
                type="text"
                value={noTelepon}
                onChange={(e) => setNoTelepon(e.target.value)}
                placeholder="Contoh: 08123456789"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1 uppercase tracking-wider">
                Kata Sandi Default
              </label>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Kata sandi login"
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/20 text-slate-800"
              />
            </div>
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
              {submitting ? 'Menyimpan...' : 'Daftarkan Siswa'}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
}
