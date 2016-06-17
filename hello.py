def wsgi_application(environ, start_response):
# бизнес-логика
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
        ]
    
    args = environ.QUERY_STRING.split("&")
    body = '\n'.join(args)
    
    start_response(status, headers )
    return [ body ]