class Middleware(object):
    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):
        for lists in self.app(environ, start_response):
            text = lists
            if text.find('<body') != -1:
                yield text.encode()
                yield "<div class='top'>Middleware TOP</div>".encode()
            elif text.find('</body>') != -1:
                yield "<div class='botton'>Middleware BOTTOM</div>".encode()
                yield text.encode()
            else:
                yield text.encode()

def Application(environ, start_response):
    filepath = environ['PATH_INFO']
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

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    app = Middleware(Application)
    _server = make_server('localhost', 8000, app)
    print ("Serving localhost on port 8000...")
    _server.serve_forever()
