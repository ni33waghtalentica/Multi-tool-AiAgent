#!/usr/bin/env python3
"""
Serve the custom UI and proxy API requests to the ADK server (port 8000).
This avoids CORS: the browser talks only to this server (port 3000).
"""
import http.server
import json
import os
import urllib.request
import urllib.error

UI_DIR = os.path.dirname(os.path.abspath(__file__))
API_BASE = "http://127.0.0.1:8000"
PORT = 3000


class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=UI_DIR, **kwargs)

    def do_GET(self):
        if self.path.startswith("/list-apps") or self.path.startswith("/apps/") or self.path == "/health":
            self._proxy("GET", body=None)
            return
        super().do_GET()

    def do_POST(self):
        if self.path.startswith("/apps/") or self.path == "/run":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length) if length else None
            self._proxy("POST", body=body)
            return
        self.send_error(404)

    def _proxy(self, method, body=None):
        url = API_BASE + self.path
        req = urllib.request.Request(url, data=body, method=method)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                self.send_response(resp.status)
                for k, v in resp.headers.items():
                    if k.lower() != "transfer-encoding":
                        self.send_header(k, v)
                self.end_headers()
                self.wfile.write(resp.read())
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(e.read())
        except urllib.error.URLError as e:
            self.send_response(503)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            msg = json.dumps({"error": "API unreachable", "detail": str(e.reason)}).encode()
            self.wfile.write(msg)
        except Exception as e:
            self.send_response(503)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        print("[%s] %s" % (self.log_date_time_string(), format % args))


def main():
    os.chdir(UI_DIR)
    server = http.server.HTTPServer(("", PORT), ProxyHandler)
    print("Custom UI + API proxy: http://localhost:%s" % PORT)
    print("Proxying API to %s" % API_BASE)
    server.serve_forever()


if __name__ == "__main__":
    main()
