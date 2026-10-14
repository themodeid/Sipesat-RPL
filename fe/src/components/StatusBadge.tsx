import React from 'react';
import { StatusPengajuan } from '@/lib/types';
import { Clock, RefreshCw, CheckCircle2, XCircle } from 'lucide-react';

interface StatusBadgeProps {
  status: StatusPengajuan;
  showIcon?: boolean;
}

export default function StatusBadge({ status, showIcon = true }: StatusBadgeProps) {
  switch (status) {
    case 'MENUNGGU':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-50 text-amber-800 border border-amber-200">
          {showIcon && <Clock className="w-3.5 h-3.5" />}
          Menunggu Verifikasi
        </span>
      );
    case 'DIPROSES':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-blue-50 text-brand-600 border border-blue-200">
          {showIcon && <RefreshCw className="w-3.5 h-3.5 animate-spin" />}
          Sedang Diproses
        </span>
      );
    case 'DISETUJUI':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200">
          {showIcon && <CheckCircle2 className="w-3.5 h-3.5" />}
          Disetujui
        </span>
      );
    case 'DITOLAK':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-rose-50 text-rose-800 border border-rose-200">
          {showIcon && <XCircle className="w-3.5 h-3.5" />}
          Ditolak
        </span>
      );
    default:
      return null;
  }
}
