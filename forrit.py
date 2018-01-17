from bottle import route, run

@route("/")
def index():
    return "<a href = '/about'>About</a>" \
           "<a href = '/bio'>Biography</a>" \
           "<a href = '/pictures'>Pictures</a>"

@route("/about")
def about():
    return "jasdjad"

@route("/bio")
def bio():
    return "kashdjhajds"

@route("/pictures")
def pictures():
    return "ksjhadjahsjd"

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)

