#!/bin/bash
# Start ADK Web UI (cricket + football agents). Run from project root.
# Usage: ./run_web.sh   or:  ./run_web.sh 8080
set -e
cd "$(dirname "$0")"
PORT="${1:-8000}"
echo "Starting ADK web server on port $PORT..."
echo "Open http://localhost:$PORT and select cricket_stats_agent or football_stats_agent"
exec .venv/bin/python3 -m google.adk.cli web --port "$PORT"
