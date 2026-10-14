import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import path from 'path';

import authRoutes from './routes/auth.routes';
import pengajuanRoutes from './routes/pengajuan.routes';
import jenisSuratRoutes from './routes/jenis-surat.routes';
import siswaRoutes from './routes/siswa.routes';
import statsRoutes from './routes/stats.routes';
import uploadRoutes from './routes/upload.routes';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middlewares
app.use(cors({
  origin: process.env.CORS_ORIGIN || 'http://localhost:3000',
  credentials: true,
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static uploads
app.use('/uploads', express.static(path.join(process.cwd(), 'uploads')));

// Health check
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', service: 'SIPESAT Backend API', time: new Date() });
});

// Mount Routes
app.use('/api/auth', authRoutes);
app.use('/api/pengajuan', pengajuanRoutes);
app.use('/api/jenis-surat', jenisSuratRoutes);
app.use('/api/siswa', siswaRoutes);
app.use('/api/stats', statsRoutes);
app.use('/api/upload', uploadRoutes);

// Fallback 404
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint API tidak ditemukan.' });
});

app.listen(PORT, () => {
  console.log(`====================================================`);
  console.log(`🚀 SIPESAT Backend Express aktif di http://localhost:${PORT}`);
  console.log(`====================================================`);
});
