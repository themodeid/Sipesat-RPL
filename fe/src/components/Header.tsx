'use client';

import React from 'react';
import { UserSession } from '@/lib/types';
import { School, Calendar } from 'lucide-react';
import { formatDate } from '@/lib/utils';

interface HeaderProps {
  user: UserSession | null;
}

export default function Header({ user }: HeaderProps) {
  const today = formatDate(new Date());

  return (
    <header className="h-16 bg-white border-b border-surface-border px-6 flex items-center justify-between shrink-0">
      <div className="flex items-center gap-3">
        <div className="p-2 bg-brand-50 text-brand-500 rounded-md">
          <School className="w-5 h-5" />
        </div>
        <div>
          <h2 className="text-sm font-bold text-slate-800">
            {process.env.NEXT_PUBLIC_SCHOOL_NAME || 'SMK NEGERI 1 CONTOH KOTA'}
          </h2>
          <p className="text-xs text-slate-500">
            Layanan Administrasi & Pengajuan Surat Siswa
          </p>
        </div>
      </div>

      <div className="flex items-center gap-4 text-xs text-slate-600">
        <div className="hidden sm:flex items-center gap-1.5 bg-slate-100 px-3 py-1.5 rounded-md border border-slate-200">
          <Calendar className="w-3.5 h-3.5 text-slate-500" />
          <span>{today}</span>
        </div>

        <div className="flex items-center gap-2 pl-3 border-l border-slate-200">
          <div className="w-8 h-8 rounded-full bg-brand-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
            {user?.nama ? user.nama.charAt(0).toUpperCase() : 'U'}
          </div>
          <div className="hidden md:block text-left">
            <p className="text-xs font-semibold text-slate-800 leading-tight truncate max-w-[140px]">
              {user?.nama}
            </p>
            <p className="text-[11px] text-slate-500 font-medium capitalize">
              {user?.role?.toLowerCase()}
            </p>
          </div>
        </div>
      </div>
    </header>
  );
}
