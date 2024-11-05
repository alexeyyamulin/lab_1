from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

# Настройка Jinja2
template_dir = 'templates'
env = Environment(loader=FileSystemLoader(template_dir))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?', 1)[0]  # Получаем путь без параметров

        if path == '/':
            self.render_template('index.html', {'title': 'Главная - Автомагазин'})
        elif path == '/about/':
            self.render_template('about.html', {'title': 'О нас - Автомагазин'})
        elif path == '/catalog/':
            cars = {
                'BMW X5': {'price': 7000000, 'image': 'bmw_x5.jpg'},
                'Mercedes-Benz S-Class': {'price': 8500000, 'image': 'mercedes_s_class.jpg'},
                'Audi A8': {'price': 7800000, 'image': 'audi_a8.jpg'},
                'Tesla Model S': {'price': 9500000, 'image': 'tesla_model_s.jpg'},
                'Volkswagen Golf': {'price': 3200000, 'image': 'vw_golf.jpg'},
            }
            self.render_template('catalog.html', {'title': 'Каталог - Автомагазин', 'cars': cars})
        else:
            self.send_error(404)

    def render_template(self, template_name, data):
        try:
            template = env.get_template(template_name)
            html = template.render(**data)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        except FileNotFoundError:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущен на порту {8000}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
