def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"<h1>Hello! I'm proxy!</h1>"]
