'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { JenisSuratItem } from '@/lib/types';
import { api } from '@/lib/api';
import {
  FilePlus,
  ArrowLeft,
  Upload,
  CheckCircle,
  AlertCircle,
  FileCheck,
  Send,
} from 'lucide-react';

export default function BuatPengajuanBaruPage() {
  const router = useRouter();
  const [jenisSuratList, setJenisSuratList] = useState<JenisSuratItem[]>([]);
  const [selectedJenisId, setSelectedJenisId] = useState('');
  const [keperluan, setKeperluan] = useState('');
  const [keterangan, setKeterangan] = useState('');
  const [lampiranUrl, setLampiranUrl] = useState('');
  const [lampiranName, setLampiranName] = useState('');
  const [uploading, setUploading] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    async function loadJenisSurat() {
      try {
        const res = await api.get('/jenis-surat');
        const activeOnly = (res?.data || []).filter((j: JenisSuratItem) => j.isActive);
        setJenisSuratList(activeOnly);
        if (activeOnly.length > 0) {
          setSelectedJenisId(activeOnly[0].id);
        }
      } catch (err) {
        console.error('Gagal memuat jenis surat:', err);
      }
    }
    loadJenisSurat();
  }, []);

  const selectedJenis = jenisSuratList.find((j) => j.id === selectedJenisId);

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (file.size > 5 * 1024 * 1024) {
      alert('Ukuran berkas maksimal 5MB');
      return;
    }

    setUploading(true);
    try {
      const data = await api.upload(file);
      setLampiranUrl(data.url);
      setLampiranName(file.name);
    } catch (err: any) {
      alert(err.message || 'Gagal mengunggah berkas');
    } finally {
      setUploading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedJenisId || !keperluan.trim()) {
      setError('Pilih jenis surat dan isi tujuan/keperluan pengajuan!');
      return;
    }

    setLoading(true);
    setError('');

    try {
      await api.post('/pengajuan', {
        jenisSuratId: selectedJenisId,
        keperluan: keperluan.trim(),
        keterangan: keterangan.trim() || null,
        lampiran: lampiranUrl || null,
      });

      setSuccess(true);
      setTimeout(() => {
        router.push('/dashboard/riwayat');
      }, 1500);
    } catch (err: any) {
      setError(err.message || 'Terjadi kesalahan saat mengirim pengajuan');
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {/* Header Bar */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <Link
            href="/dashboard"
            className="p-2 bg-white rounded-lg border border-surface-border text-slate-600 hover:text-slate-900 transition-colors shadow-sm"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <h1 className="text-xl font-bold text-slate-800">
              Formulir Pengajuan Surat Siswa
            </h1>
            <p className="text-xs text-slate-500">
              Isi data permohonan surat administrasi dengan benar dan lengkap
            </p>
          </div>
        </div>
      </div>

      {success && (
        <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-lg flex items-center gap-3 text-emerald-800 animate-fadeIn">
          <CheckCircle className="w-5 h-5 text-emerald-600 shrink-0" />
          <div>
            <p className="text-sm font-bold">Pengajuan Berhasil Dikirim!</p>
            <p className="text-xs text-emerald-700">
              Mengalihkan Anda ke halaman riwayat status permohonan surat...
            </p>
          </div>
        </div>
      )}

      {error && (
        <div className="p-4 bg-rose-50 border border-rose-200 rounded-lg flex items-center gap-3 text-rose-800">
          <AlertCircle className="w-5 h-5 text-rose-600 shrink-0" />
          <p className="text-xs font-semibold">{error}</p>
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-5">
        {/* Card Pilihan Jenis Surat */}
        <div className="bg-white rounded-xl border border-surface-border p-6 shadow-sm space-y-4">
          <h2 className="text-sm font-bold text-slate-800 border-b border-surface-border pb-3 flex items-center gap-2">
            <FilePlus className="w-4 h-4 text-brand-500" />
            <span>1. Pilih Jenis Surat Yang Diajukan</span>
          </h2>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1.5 uppercase tracking-wider">
              Kategori / Jenis Surat
            </label>
            <select
              value={selectedJenisId}
              onChange={(e) => setSelectedJenisId(e.target.value)}
              className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/30 focus:border-brand-500 text-slate-800 transition-colors"
            >
              {jenisSuratList.map((item) => (
                <option key={item.id} value={item.id}>
                  {item.namaSurat} ({item.kodeSurat})
                </option>
              ))}
            </select>
          </div>

          {selectedJenis && (
            <div className="p-4 bg-slate-50 border border-slate-200 rounded-lg space-y-2 text-xs">
              <div>
                <span className="font-semibold text-slate-700">Deskripsi Surat:</span>
                <p className="text-slate-600 mt-0.5">{selectedJenis.deskripsi}</p>
              </div>
              {selectedJenis.persyaratan && (
                <div className="pt-2 border-t border-slate-200">
                  <span className="font-semibold text-slate-700">Persyaratan Pengajuan:</span>
                  <p className="text-slate-600 whitespace-pre-line mt-0.5">
                    {selectedJenis.persyaratan}
                  </p>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Card Detail Keperluan */}
        <div className="bg-white rounded-xl border border-surface-border p-6 shadow-sm space-y-4">
          <h2 className="text-sm font-bold text-slate-800 border-b border-surface-border pb-3 flex items-center gap-2">
            <FileCheck className="w-4 h-4 text-brand-500" />
            <span>2. Maksud & Keperluan Pengajuan</span>
          </h2>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1.5 uppercase tracking-wider">
              Keperluan / Alasan Utama <span className="text-rose-500">*</span>
            </label>
            <textarea
              required
              rows={3}
              value={keperluan}
              onChange={(e) => setKeperluan(e.target.value)}
              placeholder="Contoh: Pengurusan persyaratan beasiswa perguruan tinggi / Tunjangan instansi orang tua / Izin mengikuti kejuaraan karate..."
              className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/30 focus:border-brand-500 text-slate-800 transition-colors"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1.5 uppercase tracking-wider">
              Keterangan Tambahan (Opsional)
            </label>
            <textarea
              rows={2}
              value={keterangan}
              onChange={(e) => setKeterangan(e.target.value)}
              placeholder="Catatan tambahan untuk petugas tata usaha bila ada..."
              className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/30 focus:border-brand-500 text-slate-800 transition-colors"
            />
          </div>
        </div>

        {/* Card Lampiran Berkas Pendukung */}
        <div className="bg-white rounded-xl border border-surface-border p-6 shadow-sm space-y-4">
          <h2 className="text-sm font-bold text-slate-800 border-b border-surface-border pb-3 flex items-center gap-2">
            <Upload className="w-4 h-4 text-brand-500" />
            <span>3. Lampiran Berkas Pendukung (Opsional)</span>
          </h2>

          <p className="text-xs text-slate-500">
            Unggah foto atau dokumen PDF pendukung jika dipersyaratkan. Maksimal 5MB.
          </p>

          <div className="flex items-center gap-3">
            <label className="inline-flex items-center gap-2 px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-lg border border-slate-200 cursor-pointer transition-colors">
              <Upload className="w-3.5 h-3.5" />
              <span>Pilih Berkas</span>
              <input
                type="file"
                className="hidden"
                accept="image/*,.pdf"
                onChange={handleFileUpload}
                disabled={uploading}
              />
            </label>

            {uploading && (
              <span className="text-xs text-brand-600 font-medium animate-pulse">
                Mengunggah berkas ke server...
              </span>
            )}

            {lampiranName && !uploading && (
              <div className="flex items-center gap-2 px-3 py-1.5 bg-emerald-50 border border-emerald-200 rounded-md text-emerald-800 text-xs font-medium">
                <FileCheck className="w-4 h-4 text-emerald-600" />
                <span className="truncate max-w-[200px]">{lampiranName}</span>
                <button
                  type="button"
                  onClick={() => {
                    setLampiranUrl('');
                    setLampiranName('');
                  }}
                  className="text-rose-500 hover:text-rose-700 font-bold ml-1 text-xs"
                >
                  &times;
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Tombol Aksi */}
        <div className="flex items-center justify-end gap-3 pt-2">
          <Link
            href="/dashboard"
            className="px-4 py-2.5 text-xs font-semibold text-slate-600 hover:bg-slate-100 rounded-lg transition-colors border border-slate-200"
          >
            Batal
          </Link>
          <button
            type="submit"
            disabled={loading || uploading}
            className="inline-flex items-center gap-2 px-5 py-2.5 bg-brand-500 hover:bg-brand-600 disabled:opacity-60 text-white text-sm font-semibold rounded-lg shadow-sm transition-colors"
          >
            {loading ? (
              <span>Mengirim Permohonan...</span>
            ) : (
              <>
                <Send className="w-4 h-4" />
                <span>Kirim Pengajuan Surat</span>
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
}
