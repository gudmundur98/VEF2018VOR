from bottle import route, run

@route("/")
def index():
    return "<a href = 'about'> About</a>" \
           "<a href = 'bio'> Biography</a>" \
           "<a href = 'pictures'> Pictures</a>"

@route("/about")
def about():
    return "jasdjad"

@route("/bio")
def bio():
    return "kashdjhajds"

@route("/pictures")
def pictures():
    return "ksjhadjahsjd"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

