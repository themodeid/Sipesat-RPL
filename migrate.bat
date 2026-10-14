@echo off
title Migrasi & Seeding Database SIPESAT
echo ========================================================
echo   Migrasi Schema & Seeding Database PostgreSQL (be/)
echo ========================================================
cd /d %~dp0be
echo 1. Generate Prisma Client...
call npx.cmd prisma generate
echo.
echo 2. Sinkronisasi Skema Database...
call npx.cmd prisma db push
echo.
echo 3. Menjalankan Seeder Data Awal...
call node prisma/seed.mjs
echo.
echo Selesai! Database siap digunakan.
pause
