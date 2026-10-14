'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { api } from '@/lib/api';
import { GraduationCap, Lock, User as UserIcon, ShieldAlert, ArrowRight, School } from 'lucide-react';

export default function LoginPage() {
  const router = useRouter();
  const [roleType, setRoleType] = useState<'SISWA' | 'PETUGAS'>('SISWA');
  const [identifier, setIdentifier] = useState('0061234567');
  const [password, setPassword] = useState('siswa123');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleTabChange = (type: 'SISWA' | 'PETUGAS') => {
    setRoleType(type);
    setError('');
    if (type === 'SISWA') {
      setIdentifier('0061234567');
      setPassword('siswa123');
    } else {
      setIdentifier('admin');
      setPassword('admin123');
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await api.login(roleType, identifier, password);
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message || 'Terjadi kesalahan saat login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-surface-light p-4">
      <div className="w-full max-w-md">
        {/* Card Header & Brand */}
        <div className="text-center mb-6">
          <div className="inline-flex items-center justify-center w-14 h-14 rounded-xl bg-navy-900 text-white shadow-md mb-3">
            <GraduationCap className="w-8 h-8 text-brand-500" />
          </div>
          <h1 className="text-2xl font-bold text-slate-800 tracking-tight">
            SIPESAT WEB
          </h1>
          <p className="text-sm font-medium text-slate-500 mt-1">
            Sistem Informasi Pengajuan Surat Siswa
          </p>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 mt-2 rounded-full bg-slate-200 text-slate-700 text-xs font-semibold">
            <School className="w-3.5 h-3.5" />
            <span>SMK NEGERI 1 CONTOH KOTA</span>
          </div>
        </div>

        {/* Login Card */}
        <div className="bg-white rounded-xl border border-surface-border shadow-sm p-6 sm:p-8">
          {/* Role Tabs */}
          <div className="grid grid-cols-2 gap-1 p-1 bg-slate-100 rounded-lg mb-6 border border-slate-200">
            <button
              type="button"
              onClick={() => handleTabChange('SISWA')}
              className={`py-2 text-xs font-semibold rounded-md transition-all ${
                roleType === 'SISWA'
                  ? 'bg-white text-brand-600 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Siswa (NISN)
            </button>
            <button
              type="button"
              onClick={() => handleTabChange('PETUGAS')}
              className={`py-2 text-xs font-semibold rounded-md transition-all ${
                roleType === 'PETUGAS'
                  ? 'bg-white text-navy-900 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Petugas / Admin TU
            </button>
          </div>

          {error && (
            <div className="mb-4 p-3 bg-rose-50 border border-rose-200 rounded-lg flex items-start gap-2.5 text-xs text-rose-700">
              <ShieldAlert className="w-4 h-4 shrink-0 mt-0.5" />
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5 uppercase tracking-wider">
                {roleType === 'SISWA' ? 'Nomor Induk Siswa Nasional (NISN)' : 'Nama Pengguna (Username)'}
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                  <UserIcon className="w-4 h-4" />
                </div>
                <input
                  type="text"
                  required
                  value={identifier}
                  onChange={(e) => setIdentifier(e.target.value)}
                  placeholder={roleType === 'SISWA' ? 'Contoh: 0061234567' : 'admin / petugas'}
                  className="w-full pl-10 pr-3.5 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/30 focus:border-brand-500 text-slate-800 transition-colors"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5 uppercase tracking-wider">
                Kata Sandi
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                  <Lock className="w-4 h-4" />
                </div>
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Masukkan kata sandi"
                  className="w-full pl-10 pr-3.5 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-brand-500/30 focus:border-brand-500 text-slate-800 transition-colors"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full mt-2 py-2.5 px-4 bg-brand-500 hover:bg-brand-600 disabled:opacity-70 text-white font-semibold text-sm rounded-lg shadow-sm transition-all flex items-center justify-center gap-2"
            >
              {loading ? (
                <span>Menghubungi Server Express...</span>
              ) : (
                <>
                  <span>Masuk ke Sistem</span>
                  <ArrowRight className="w-4 h-4" />
                </>
              )}
            </button>
          </form>

          {/* Quick Demo Credentials helper */}
          <div className="mt-6 pt-4 border-t border-slate-100 text-center">
            <p className="text-xs font-semibold text-slate-500 mb-2">
              Akun Contoh untuk Pengujian:
            </p>
            {roleType === 'SISWA' ? (
              <div className="flex flex-wrap gap-1.5 justify-center">
                <button
                  type="button"
                  onClick={() => {
                    setIdentifier('0061234567');
                    setPassword('siswa123');
                  }}
                  className="text-[11px] px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded border border-slate-200"
                >
                  Siswa 1 (Ahmad Fauzi)
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setIdentifier('0067654321');
                    setPassword('siswa123');
                  }}
                  className="text-[11px] px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded border border-slate-200"
                >
                  Siswa 2 (Siti Nurhaliza)
                </button>
              </div>
            ) : (
              <div className="flex flex-wrap gap-1.5 justify-center">
                <button
                  type="button"
                  onClick={() => {
                    setIdentifier('admin');
                    setPassword('admin123');
                  }}
                  className="text-[11px] px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded border border-slate-200"
                >
                  Admin TU (admin / admin123)
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setIdentifier('petugas');
                    setPassword('petugas123');
                  }}
                  className="text-[11px] px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded border border-slate-200"
                >
                  Petugas (petugas / petugas123)
                </button>
              </div>
            )}
          </div>
        </div>

        <p className="text-center text-xs text-slate-400 mt-5">
          &copy; {new Date().getFullYear()} Tata Usaha & Bagian Kesiswaan Sekolah
        </p>
      </div>
    </div>
  );
}
