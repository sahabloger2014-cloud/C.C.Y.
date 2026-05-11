import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
# Указываем Python отдавать файлы строго из папки public
PUBLIC_DIR = os.path.join(os.path.dirname(__file__), 'public')

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

if __name__ == '__main__':
    os.chdir(PUBLIC_DIR)
    server = HTTPServer(('localhost', PORT), MyHandler)
    print(f"Сервер запущен! Откройте в браузере: http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
        server.server_close()