'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { UserSession, PengajuanItem } from '@/lib/types';
import StatCard from '@/components/StatCard';
import StatusBadge from '@/components/StatusBadge';
import { formatDate } from '@/lib/utils';
import { api } from '@/lib/api';
import {
  FileText,
  Clock,
  RefreshCw,
  CheckCircle2,
  PlusCircle,
  Printer,
  ArrowUpRight,
  GraduationCap,
  Layers,
  AlertCircle,
} from 'lucide-react';

export default function DashboardPage() {
  const [user, setUser] = useState<UserSession | null>(null);
  const [stats, setStats] = useState<any>({
    total: 0,
    pending: 0,
    diproses: 0,
    disetujui: 0,
    ditolak: 0,
    totalSiswa: 0,
    totalJenis: 0,
  });
  const [recent, setRecent] = useState<PengajuanItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const [userData, statsData] = await Promise.all([
          api.getMe(),
          api.get('/stats'),
        ]);

        if (userData?.user) {
          setUser(userData.user);
        }
        if (statsData?.stats) {
          setStats(statsData.stats);
          setRecent(statsData.recent || []);
        }
      } catch (err) {
        console.error('Error memuat data dashboard:', err);
      } finally {
        setLoading(false);
      }
    }
    loadDashboard();
  }, []);

  const isSiswa = user?.role === 'SISWA';

  if (loading) {
    return (
      <div className="flex items-center justify-center p-12">
        <div className="flex flex-col items-center gap-2">
          <div className="w-8 h-8 border-3 border-brand-500 border-t-transparent rounded-full animate-spin"></div>
          <p className="text-xs text-slate-500 font-medium">Memuat ringkasan data...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Welcome Banner */}
      <div className="bg-white rounded-xl border border-surface-border p-6 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <span className="text-xs font-semibold px-2.5 py-1 bg-brand-50 text-brand-600 rounded-md">
            {isSiswa ? 'Portal Layanan Siswa' : 'Panel Administrasi Sekolah'}
          </span>
          <h1 className="text-xl font-bold text-slate-800 mt-2">
            Selamat Datang, {user?.nama}!
          </h1>
          <p className="text-sm text-slate-500 mt-0.5">
            {isSiswa
              ? 'Ajukan permohonan surat keterangan, izin dispensasi, dan pantau statusnya secara online.'
              : 'Kelola verifikasi pengajuan surat, pencetakan nomor registrasi, dan master persuratan.'}
          </p>
        </div>

        {isSiswa ? (
          <Link
            href="/dashboard/pengajuan/baru"
            className="inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-brand-500 hover:bg-brand-600 text-white text-sm font-semibold rounded-lg shadow-sm transition-colors shrink-0"
          >
            <PlusCircle className="w-4 h-4" />
            <span>Ajukan Surat Baru</span>
          </Link>
        ) : (
          <Link
            href="/dashboard/pengajuan"
            className="inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-navy-900 hover:bg-slate-800 text-white text-sm font-semibold rounded-lg shadow-sm transition-colors shrink-0"
          >
            <FileText className="w-4 h-4" />
            <span>Verifikasi Pengajuan</span>
          </Link>
        )}
      </div>

      {/* Notice Banner if there are pending applications for Staff */}
      {!isSiswa && stats.pending > 0 && (
        <div className="p-4 bg-amber-50 border border-amber-200 rounded-lg flex items-center justify-between gap-3 text-amber-800">
          <div className="flex items-center gap-3">
            <AlertCircle className="w-5 h-5 text-amber-600 shrink-0" />
            <div>
              <p className="text-sm font-semibold">
                Perhatian: Terdapat {stats.pending} permohonan surat baru yang menunggu tindakan Anda.
              </p>
              <p className="text-xs text-amber-700">
                Segera periksa berkas dan tentukan status pengajuan untuk mempercepat pelayanan siswa.
              </p>
            </div>
          </div>
          <Link
            href="/dashboard/pengajuan?status=MENUNGGU"
            className="px-3 py-1.5 bg-amber-600 hover:bg-amber-700 text-white rounded-md text-xs font-semibold shrink-0 transition-colors"
          >
            Tinjau Sekarang
          </Link>
        </div>
      )}

      {/* Stat Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Total Pengajuan"
          value={stats.total}
          icon={FileText}
          variant="slate"
          description={isSiswa ? 'Semua permohonan Anda' : 'Total seluruh pengajuan'}
        />
        <StatCard
          title="Menunggu Tindakan"
          value={stats.pending}
          icon={Clock}
          variant="amber"
          description="Belum ditelaah petugas"
        />
        <StatCard
          title="Sedang Diproses"
          value={stats.diproses}
          icon={RefreshCw}
          variant="blue"
          description="Dalam telaah / tanda tangan"
        />
        <StatCard
          title="Disetujui / Selesai"
          value={stats.disetujui}
          icon={CheckCircle2}
          variant="emerald"
          description="Nomor surat diterbitkan"
        />
      </div>

      {/* Master Data Metrics for Staff */}
      {!isSiswa && (
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="bg-white rounded-lg border border-surface-border p-4 flex items-center gap-4">
            <div className="w-12 h-12 rounded-lg bg-blue-50 text-brand-600 flex items-center justify-center">
              <GraduationCap className="w-6 h-6" />
            </div>
            <div>
              <p className="text-xs font-semibold uppercase text-slate-400">Total Siswa Terdaftar</p>
              <p className="text-xl font-bold text-slate-800">{stats.totalSiswa} Siswa</p>
            </div>
          </div>
          <div className="bg-white rounded-lg border border-surface-border p-4 flex items-center gap-4">
            <div className="w-12 h-12 rounded-lg bg-slate-100 text-slate-700 flex items-center justify-center">
              <Layers className="w-6 h-6" />
            </div>
            <div>
              <p className="text-xs font-semibold uppercase text-slate-400">Jenis Surat Tersedia</p>
              <p className="text-xl font-bold text-slate-800">{stats.totalJenis} Jenis Dokumen</p>
            </div>
          </div>
        </div>
      )}

      {/* Recent Submissions Table */}
      <div className="bg-white rounded-xl border border-surface-border shadow-sm overflow-hidden">
        <div className="p-5 border-b border-surface-border flex items-center justify-between">
          <div>
            <h3 className="text-sm font-bold text-slate-800">
              {isSiswa ? 'Pengajuan Surat Terkini' : 'Permohonan Masuk Terkini'}
            </h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Daftar transaksi permohonan surat administrasi terbaru
            </p>
          </div>
          <Link
            href={isSiswa ? '/dashboard/riwayat' : '/dashboard/pengajuan'}
            className="text-xs font-semibold text-brand-600 hover:text-brand-700 flex items-center gap-1"
          >
            <span>Lihat Semua</span>
            <ArrowUpRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 text-slate-700 border-b border-surface-border font-semibold uppercase text-[11px] tracking-wider">
              <tr>
                <th className="px-5 py-3">No. Pengajuan</th>
                {!isSiswa && <th className="px-5 py-3">Pemohon</th>}
                <th className="px-5 py-3">Jenis Surat</th>
                <th className="px-5 py-3">Keperluan</th>
                <th className="px-5 py-3">Tanggal</th>
                <th className="px-5 py-3">Status</th>
                <th className="px-5 py-3 text-right">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-surface-border">
              {recent.length === 0 ? (
                <tr>
                  <td colSpan={isSiswa ? 6 : 7} className="px-5 py-8 text-center text-slate-400">
                    Belum ada data pengajuan surat saat ini.
                  </td>
                </tr>
              ) : (
                recent.map((item) => (
                  <tr key={item.id} className="hover:bg-slate-50 transition-colors">
                    <td className="px-5 py-3.5 font-mono font-medium text-slate-800">
                      {item.nomorPengajuan}
                    </td>
                    {!isSiswa && (
                      <td className="px-5 py-3.5">
                        <p className="font-semibold text-slate-800">{item.siswa?.nama}</p>
                        <p className="text-[11px] text-slate-400">
                          {item.siswa?.nisn} &bull; {item.siswa?.kelas}
                        </p>
                      </td>
                    )}
                    <td className="px-5 py-3.5">
                      <span className="font-medium text-slate-800">
                        {item.jenisSurat?.namaSurat}
                      </span>
                    </td>
                    <td className="px-5 py-3.5 max-w-[200px] truncate text-slate-600" title={item.keperluan}>
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
                        {item.status === 'DISETUJUI' && (
                          <Link
                            href={`/cetak/${item.id}`}
                            target="_blank"
                            className="p-1.5 text-slate-600 hover:text-brand-600 hover:bg-slate-100 rounded transition-colors"
                            title="Cetak Surat Resmi"
                          >
                            <Printer className="w-4 h-4" />
                          </Link>
                        )}
                        <Link
                          href={`/dashboard/pengajuan/${item.id}`}
                          className="px-2.5 py-1 text-xs font-semibold text-brand-600 hover:bg-brand-50 rounded border border-brand-200 transition-colors"
                        >
                          Detail
                        </Link>
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
