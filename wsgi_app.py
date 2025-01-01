
# guincorn

def app(environ, start_response):
    status ="200 OK"
    headers = [("Content_Type","text/plain; charset=utf-8")]
    start_response(status, headers)
    return[b"Hello, WSGI World"]