from bottle import Bottle, run

from myform import setup_form_routes
from routes import setup_routes


app = Bottle()
setup_routes(app)
setup_form_routes(app)


if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True, reloader=True)
