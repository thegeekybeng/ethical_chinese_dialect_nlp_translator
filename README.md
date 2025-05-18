# Ethical Chinese Dialect NLP Translator

This project builds a prototype two-way NLP translator for major Chinese dialects — Cantonese, Teochew, Hokkien, and Hakka — used by native Singaporean and Malaysian Chinese communities.

## 🐳 Docker Quick Start

```bash
docker-compose build
docker-compose up
```

Inside the container:
```bash
python scripts/run_tts_test.py
python scripts/run_asr_test.py
```

## Project Structure

- Dockerfile
- docker-compose.yml
- requirements.txt
- sample_dialect_dataset.csv / .jsonl
- scripts/