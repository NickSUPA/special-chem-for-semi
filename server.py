import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run_server():
    port = PORT
    for attempt in range(10):
        try:
            with socketserver.ThreadingTCPServer(("", port), Handler) as httpd:
                url = f"http://localhost:{port}/index.html"
                print("=" * 70)
                print("   SEMICONDUCTOR SPECIALTY CHEMICALS - FINAL EXAM PORTAL")
                print("=" * 70)
                print(f"[*] Local server started successfully at: {url}")
                print(f"[*] Serving files from: {DIRECTORY}")
                print("[*] Press Ctrl+C in this terminal to stop the server.")
                print("=" * 70)
                webbrowser.open(url)
                httpd.serve_forever()
                break
        except OSError as e:
            if "Address already in use" in str(e) or e.errno == 98 or e.errno == 10048:
                port += 1
                continue
            else:
                print(f"[!] Server error: {e}")
                sys.exit(1)

if __name__ == "__main__":
    run_server()
