# Импорт необходимых библиотек
from jinja2 import Environment, FileSystemLoader, Template
from wsgiref.simple_server import make_server


# Наш интерфейс
e_nv = Environment(loader=FileSystemLoader('.'))

def Application(environ, start_response):
    start_response = '200 OK'
    start_response = [('Content-type', 'text/html')]
    filepath = environ['PATH_INFO']

    return Application(path) \
    .encode('utf-8')
            
    if  (filepath == '/' or filepath == '/index.html' or filepath == '/about/aboutme.html'):
        file = open('.' + filepath, 'r')
        result = []
        for line in file:
            result.append(line)
        file.close()
        start_response('200 OK', [('Content-type', 'text/HTML')])
        return result
    else:
        start_response('404 Not Found', [("Content-Type", "text/html")])
        return ''.encode()

# Вызов скрипта
if __name__ == '__main__':    
    make_server(Middleware(Application), host='localhost', port=8000).serve_forever()   
