#!/usr/bin/env bash
set -euo pipefail
echo "Setting up RAG Project environment..."
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Setup complete! Activate your venv with 'source .venv/bin/activate'."
