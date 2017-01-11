# Импорт необходимых библиотек
from jinja2 import Environment, FileSystemLoader, Template
from wsgiref.simple_server import make_server

e_nv = Environment(loader=FileSystemLoader('.'))

def Application(environ, start_resp):
    start_resp = '200 OK'
    start_resp = [('Content-type', 'text/html')]
    filepath = environ['PATH_INFO']

def template(l):
        l = filepath
        return env.template(filepath).render(link=l)
    return [template(filepath).encode('utf-8')]

# Вызов скрипта   
make_server(Middleware(Application), host='localhost', port=8000).serve_forever()   
