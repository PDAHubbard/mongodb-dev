from bottle import route, run, template, debug

@route('/')
def home_page():
    return "Hello Wordl."

@route('/test')
def test_page():
    return "This is a test page."

@route('/bye/<name>')
def index(name):
    return template("Bye <b>{{name}}</b>!", name=name)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

debug(True)
run(host='localhost', port=8080)
