@echo off
title SIPESAT - Sistem Pengajuan Surat Siswa
echo ===================================================
echo [SIPESAT] Memulai Server Lokal (BE & FE)...
echo ===================================================

start "SIPESAT-Backend-Express (Port 5000)" cmd /k "cd /d %~dp0be && npm run dev"
start "SIPESAT-Frontend-NextJS (Port 3000)" cmd /k "cd /d %~dp0fe && npm run dev"

echo.
echo Backend Express API : http://localhost:5000
echo Frontend Next.js    : http://localhost:3000
echo ===================================================
pause
