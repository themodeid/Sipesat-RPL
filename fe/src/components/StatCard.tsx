import React from 'react';
import { LucideIcon } from 'lucide-react';

interface StatCardProps {
  title: string;
  value: number | string;
  icon: LucideIcon;
  variant?: 'blue' | 'amber' | 'emerald' | 'rose' | 'slate';
  description?: string;
}

export default function StatCard({
  title,
  value,
  icon: Icon,
  variant = 'blue',
  description,
}: StatCardProps) {
  const colorMap = {
    blue: {
      bg: 'bg-blue-50',
      icon: 'text-brand-500',
      borderLeft: 'border-l-brand-500',
    },
    amber: {
      bg: 'bg-amber-50',
      icon: 'text-amber-600',
      borderLeft: 'border-l-amber-500',
    },
    emerald: {
      bg: 'bg-emerald-50',
      icon: 'text-emerald-600',
      borderLeft: 'border-l-emerald-500',
    },
    rose: {
      bg: 'bg-rose-50',
      icon: 'text-rose-600',
      borderLeft: 'border-l-rose-500',
    },
    slate: {
      bg: 'bg-slate-100',
      icon: 'text-slate-600',
      borderLeft: 'border-l-slate-500',
    },
  };

  const style = colorMap[variant] || colorMap.blue;

  return (
    <div
      className={`bg-white rounded-lg border border-surface-border p-5 shadow-sm border-l-4 ${style.borderLeft} flex items-center justify-between`}
    >
      <div>
        <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
          {title}
        </p>
        <p className="text-2xl font-bold text-slate-800 mt-1">{value}</p>
        {description && (
          <p className="text-xs text-slate-400 mt-0.5">{description}</p>
        )}
      </div>
      <div className={`w-12 h-12 rounded-lg ${style.bg} ${style.icon} flex items-center justify-center shrink-0`}>
        <Icon className="w-6 h-6" />
      </div>
    </div>
  );
}
