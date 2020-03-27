# wsgi--python web服务server网关gatewa接口interface

def application(environ, start_response):
    response_boday = "HELLO WORLD"
    header = [('Content-Type', 'text/html')]
    status = "200 OK"
    start_response(status, header)
    print("http request method:" + environ['REQUEST_METHOD'])
    return [response_boday]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server("0.0.0.0",8080,application)
    print("http run on:"+ str(httpd.server_port))
    httpd.serve_forever()
