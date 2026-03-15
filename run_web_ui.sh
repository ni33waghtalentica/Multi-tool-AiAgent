#!/bin/bash
# Start ADK API (port 8000), then serve the custom UI with API proxy (port 3000).
# Open http://localhost:3000 — all API calls are proxied, so no CORS issues.
set -e
cd "$(dirname "$0")"

# Free ports so this script can bind (e.g. after a previous run)
for port in 8000 3000; do
  pid=$(lsof -ti:$port 2>/dev/null) || true
  if [ -n "$pid" ]; then
    echo "Stopping process on port $port (PID $pid)..."
    kill -9 $pid 2>/dev/null || true
    sleep 2
  fi
done

echo "Starting ADK API on port 8000..."
.venv/bin/adk web --port 8000 &
ADK_PID=$!
sleep 6
echo "Starting custom UI + API proxy on port 3000..."
python3 web_ui/proxy_server.py &
UI_PID=$!
echo ""
echo "  API:       http://localhost:8000"
echo "  Custom UI: http://localhost:3000  (use this; API is proxied)"
echo ""
echo "Press Ctrl+C to stop both."
trap "kill $ADK_PID $UI_PID 2>/dev/null; exit" INT TERM
wait
