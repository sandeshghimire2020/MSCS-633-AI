#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d ".venv" ]]; then
  echo "Virtual environment not found. Create it first with: python3 -m venv .venv"
  exit 1
fi

source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel >/dev/null
pip install -r requirements.txt
python -m spacy download en_core_web_sm >/dev/null
python manage.py migrate
python manage.py runserver 127.0.0.1:8000