#!/bin/bash
# Recreate the virtual environment on THIS machine so native extensions
# (cryptography, grpc, pydantic_core, etc.) are built for your Mac.
# Fixes: "code signature not valid" / "library load disallowed by system policy"
#
# Run from project root:  ./setup_venv.sh
# Then:  source .venv/bin/activate  &&  adk web --port 8000
# Open:  http://localhost:8000
set -e
cd "$(dirname "$0")"
echo "Removing old .venv..."
rm -rf .venv
echo "Creating new venv with $(which python3)..."
python3 -m venv .venv
echo "Upgrading pip..."
.venv/bin/pip install --upgrade pip
echo "Installing requirements (this may take a few minutes)..."
.venv/bin/pip install -r requirements.txt
echo ""
echo "Done. Run:"
echo "  source .venv/bin/activate"
echo "  adk web --port 8000"
echo "Then open http://localhost:8000 in your browser."
