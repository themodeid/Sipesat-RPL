import { Router } from 'express';
import multer from 'multer';
import path from 'path';
import fs from 'fs';
import { authMiddleware } from '../middlewares/auth.middleware';

const router = Router();

// Pastikan folder uploads ada
const uploadDir = path.join(process.cwd(), 'uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    const cleanName = file.originalname.replace(/[^a-zA-Z0-9.-]/g, '_');
    cb(null, `${Date.now()}_${cleanName}`);
  },
});

const upload = multer({
  storage,
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB
});

router.post('/', authMiddleware, upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'Tidak ada berkas yang diunggah.' });
    }

    const fileUrl = `http://localhost:5000/uploads/${req.file.filename}`;
    return res.json({
      success: true,
      url: fileUrl,
      fileName: req.file.originalname,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal mengunggah berkas.' });
  }
});

export default router;
