#!/usr/bin/env python3
from flask import *
from flask_socketio import SocketIO, emit
from dashboard import dashboard
import util

app = Flask(__name__, template_folder="./views/")
socketio = SocketIO(app)

dash = dashboard.DashBoard("first Dashboard", "Testing first dashboard")

# store links for the dashboard
# could look at redis for persistence
context = {
    "display_url": "http://ip-api.com/"
}

@app.route("/")
def index():
    return render_template("base.html", url=context["display_url"])

@app.route("/update", methods=["POST"])
def update_link():
    if not "url" in request.form:
        return Response("error", 400)

    try:
        context["display_url"] = request.form["url"]

        # emit socket event to tell client to reload dashboard
        emit('reload', namespace="/", broadcast=True)

        return jsonify("updated display to {}".format(request.form["url"]))

    except ValueError as err:
        return jsonify("{}".format(err))


@app.route("/addModule", methods=["POST"])
def add_Module():
    dash.addModule(request)
    print(dash.Modules[0].url)
    return jsonify("Added Module")

if __name__ == "__main__":
    socketio.run(app, debug=True)
