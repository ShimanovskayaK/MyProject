from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from jinja2 import FileSystemLoader, Environment

e_nv = Environment(loader=FileSystemLoader('temp'))

def index(request):
    return Response(e_nv.get_template('index.html').render())

def AboutMe(request):
    return Response(e_nv.get_template('about/aboutme.html').render())

if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_route('index', '/index.html')
    config.add_route('AboutMe', '/about/aboutme.html')
    app = config.make_wsgi_app()
    server = make_server('localhost', 8000, app)
    print("localhost:8000")
server.serve_forever()
