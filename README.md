# Ethical Chinese Dialect NLP Translator

This project builds a prototype two-way NLP translator for major Chinese dialects — Cantonese, Teochew, Hokkien, and Hakka — used by native Singaporean and Malaysian Chinese communities. The goal is to support speech and text input/output translation via a standardized pipeline.

---

## 📦 Project Setup (OS-Agnostic)

### 1. Clone or Download the Project Folder

```bash
cd your/desired/folder
```

### 2. Create a Virtual Environment

#### On Linux/macOS:
```bash
python3 -m venv venlp
source venlp/bin/activate
```

#### On Windows:
```bash
python -m venv venlp
venlp\Scripts\activate
```

You should now see the virtual environment prefix like `(venlp)` in your terminal.

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Load Sample Dataset

Place the `sample_dialect_dataset.csv` and `sample_dialect_dataset.jsonl` files into the root project folder.

---

### 5. Run Test Scripts (Optional)

You can create and run the following scripts to validate each part of the pipeline:
- `run_tts.py` – Text-to-Speech synthesis
- `run_asr.py` – Speech-to-Text audio processing
- `run_translation_test.py` – Dialect → Mandarin → English pipeline simulation

---

### 6. Deactivate the Virtual Environment

When done, deactivate with:

```bash
deactivate
```

---

## 📁 Project Structure

```
ethical_chinese_dialect_nlp_translator/
├── venlp/                       # Virtual environment
├── sample_dialect_dataset.csv
├── sample_dialect_dataset.jsonl
├── requirements.txt
├── README.md
└── (Optional scripts: run_tts.py, run_asr.py, etc.)
```

---

## 🔗 Notes

- Dataset includes placeholder IPA/romanized phonetics.
- Audio file paths are pre-filled; you may replace them with real recordings later.
- Future improvements may include real speaker voices, contextual translation modeling, and feedback-driven refinements.

---

## ✨ Goals

- Accept speech input in any major dialect
- Translate dialect → Mandarin → English (and back)
- Output user-facing response via text or synthesized speech