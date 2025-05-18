# 🔧 User Installation & Testing Guide (OS-Agnostic)

This guide helps you set up, install, and test the **Ethical Chinese Dialect NLP Translator** project on **any OS**, including Linux (e.g., Alpine), macOS, and Windows.

---

## 📁 Step 1: Clone the Repository

```bash
git clone https://github.com/thegeekybeng/ethical_chinese_dialect_nlp_translator.git
cd ethical_chinese_dialect_nlp_translator
```

---

## 🧪 Step 2: Create and Activate a Virtual Environment

### On Linux/macOS:

```bash
python3 -m venv venlp
source venlp/bin/activate
```

### On Windows:

```bash
python -m venv venlp
venlp\Scripts\activate
```

---

## 📦 Step 3: Install Required Dependencies

Use the `requirements.txt` file provided:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> On Alpine Linux, you may need to install system packages first:

```bash
sudo apk add build-base python3-dev libffi-dev ffmpeg
```

---

## 📂 Step 4: Dataset & File Setup

Ensure the following files are present in your root directory:
- `sample_dialect_dataset.csv`
- `sample_dialect_dataset.jsonl`

(Optional) If using speech:
- Store actual audio files at the paths specified in `audio_file_path`

---

## 🧪 Step 5: Run Initial Tests (Example)

### Translation Pipeline (Dialect → Mandarin → English)
```bash
python run_translation_test.py
```

### Text-to-Speech Test
```bash
python run_tts.py
```

### Audio File Read Test
```bash
python run_asr.py
```

---

## 🧼 Step 6: Deactivate the Virtual Environment (When Done)

```bash
deactivate
```

---

## 📌 Notes

- On Alpine Linux, make sure Python, pip, and necessary compilers are installed.
- For speech synthesis, `ffmpeg` must be available in your environment.
- For GPU support, ensure PyTorch is installed with the correct CUDA version.

---

## 🚀 You're Ready!

You can now:
- Test translation between dialects, Mandarin, and English
- Add real audio files
- Expand with new domains and dialect phrases