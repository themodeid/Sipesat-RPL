'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { UserSession } from '@/lib/types';
import {
  LayoutDashboard,
  FileText,
  PlusCircle,
  Clock,
  BookOpen,
  Users,
  FileSpreadsheet,
  LogOut,
  GraduationCap,
} from 'lucide-react';

interface SidebarProps {
  user: UserSession | null;
  onLogout: () => void;
}

export default function Sidebar({ user, onLogout }: SidebarProps) {
  const pathname = usePathname();
  const isSiswa = user?.role === 'SISWA';

  const menuItems = isSiswa
    ? [
        {
          label: 'Dashboard',
          href: '/dashboard',
          icon: LayoutDashboard,
        },
        {
          label: 'Ajukan Surat Baru',
          href: '/dashboard/pengajuan/baru',
          icon: PlusCircle,
        },
        {
          label: 'Riwayat Surat Saya',
          href: '/dashboard/riwayat',
          icon: Clock,
        },
      ]
    : [
        {
          label: 'Dashboard',
          href: '/dashboard',
          icon: LayoutDashboard,
        },
        {
          label: 'Data Pengajuan Surat',
          href: '/dashboard/pengajuan',
          icon: FileText,
        },
        {
          label: 'Master Jenis Surat',
          href: '/dashboard/jenis-surat',
          icon: BookOpen,
        },
        {
          label: 'Master Data Siswa',
          href: '/dashboard/siswa',
          icon: Users,
        },
        {
          label: 'Laporan Rekapitulasi',
          href: '/dashboard/laporan',
          icon: FileSpreadsheet,
        },
      ];

  return (
    <aside className="w-64 bg-navy-900 text-slate-200 flex flex-col shrink-0 min-h-screen border-r border-slate-800 select-none">
      {/* Brand Header */}
      <div className="p-5 border-b border-slate-800 flex items-center gap-3">
        <div className="w-10 h-10 rounded-lg bg-brand-500 flex items-center justify-center text-white shadow-sm">
          <GraduationCap className="w-6 h-6" />
        </div>
        <div>
          <h1 className="font-bold text-base tracking-wide text-white">SIPESAT WEB</h1>
          <p className="text-xs text-slate-400">Pengajuan Surat Siswa</p>
        </div>
      </div>

      {/* Role Profile Info Card */}
      <div className="px-4 py-3 m-3 bg-[#242e42] rounded-md border border-slate-700/60">
        <p className="text-[11px] uppercase tracking-wider font-semibold text-slate-400">Pengguna Aktif</p>
        <p className="text-sm font-semibold text-white truncate">{user?.nama || 'Pengguna'}</p>
        <div className="flex items-center gap-1.5 mt-1">
          <span className="inline-block w-2 h-2 rounded-full bg-emerald-400"></span>
          <span className="text-xs text-slate-300">
            {user?.role === 'ADMIN' ? 'Administrator TU' : user?.role === 'PETUGAS' ? 'Petugas Administrasi' : `Siswa (${user?.kelas || 'Siswa'})`}
          </span>
        </div>
      </div>

      {/* Navigation Menu */}
      <div className="px-3 py-2 flex-1">
        <p className="px-3 py-1 text-[11px] font-semibold uppercase tracking-wider text-slate-400">
          Menu Utama
        </p>
        <nav className="mt-1 space-y-1">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive =
              item.href === '/dashboard'
                ? pathname === '/dashboard'
                : pathname.startsWith(item.href);

            return (
              <Link
                key={item.href}
                href={item.href}
                className={`flex items-center gap-3 px-3.5 py-2.5 rounded-md text-sm transition-colors ${
                  isActive
                    ? 'bg-[#2D3A55] text-white font-medium border-l-4 border-brand-500'
                    : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                }`}
              >
                <Icon className={`w-4 h-4 ${isActive ? 'text-brand-200' : 'text-slate-400'}`} />
                <span>{item.label}</span>
              </Link>
            );
          })}
        </nav>
      </div>

      {/* Footer / Logout */}
      <div className="p-3 border-t border-slate-800">
        <button
          onClick={onLogout}
          className="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-md text-sm text-rose-300 hover:bg-rose-950/40 hover:text-rose-200 transition-colors"
        >
          <LogOut className="w-4 h-4 text-rose-400" />
          <span>Keluar (Logout)</span>
        </button>
      </div>
    </aside>
  );
}
