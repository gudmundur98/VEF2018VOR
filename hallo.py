from bottle import route, run

@route("/")
def index():
    return "<h2>Hallo Heimur</h2>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

