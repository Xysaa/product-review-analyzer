# 🛍️ Product Review Analyzer

Product Review Analyzer adalah aplikasi web yang memungkinkan pengguna untuk:
- Memasukkan ulasan produk (text)
- Menganalisis sentimen (Positive / Negative / Neutral)
- Mengekstraksi poin penting (kelebihan, kekurangan, ringkasan)
- Menyimpan hasil analisis ke database
- Menampilkan riwayat analisis review

Backend dibangun menggunakan **Python Pyramid**, sedangkan frontend menggunakan **React + Vite**.

---

## 🚀 Fitur Utama

### 🔧 Backend (Pyramid)
- REST API
- Analisis sentimen menggunakan **Hugging Face**
- Ekstraksi key points menggunakan **Gemini API**
- Penyimpanan data menggunakan **PostgreSQL + SQLAlchemy**
- Error handling & CORS support

### 🎨 Frontend (React)
- Form input review
- Loading state & error handling
- Menampilkan hasil analisis
- Menampilkan daftar review yang tersimpan

---

## 🗂️ Struktur Folder

```
product-review-analyzer/
├── backend/
│   ├── product_review_analyzer/
│   ├── development.ini
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## ⚙️ Instalasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Xysaa/product-review-analyzer.git
cd product-review-analyzer
```

---

## 🧠 Backend Setup (Pyramid)

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
pserve development.ini --reload
```

Server berjalan di:
```
http://localhost:6543
```

---

## 🎨 Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend berjalan di:
```
http://localhost:5173
```

---

## 🔌 API Endpoint

### POST `/api/analyze-review`
```json
{
  "review_text": "Produknya sangat bagus dan berkualitas"
}
```

### GET `/api/reviews`
Mengambil semua review yang tersimpan.

---

## 📌 Teknologi
- Python Pyramid
- PostgreSQL
- SQLAlchemy
- Hugging Face
- Gemini API
- React
- Vite

---

## 📜 Lisensi
MIT License
