"""Answer every request as Cloudflare's challenge page does: 403, HTML, no `request-id`.
For trying NexKit's handling of a block in front of the API (nexkit#290)."""

import http.server

PAGE = (
    b"<!DOCTYPE html><html><head><title>Attention Required! | Cloudflare</title></head>"
    b"<body><h1>Sorry, you have been blocked</h1></body></html>"
)


class Handler(http.server.BaseHTTPRequestHandler):
    def answer(self):
        self.rfile.read(int(self.headers.get("content-length") or 0))
        self.send_response(403)
        for key, value in (
            ("content-type", "text/html; charset=UTF-8"),
            ("server", "cloudflare"),
            ("cf-mitigated", "challenge"),
            ("content-length", str(len(PAGE))),
        ):
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(PAGE)

    do_GET = do_POST = do_HEAD = answer

    def log_message(self, *args):
        pass


http.server.ThreadingHTTPServer(("127.0.0.1", 18443), Handler).serve_forever()
