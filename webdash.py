#!/usr/bin/env python3
from flask import *
import util

app = Flask(__name__, template_folder="./views/")

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
    context["display_url"] = request.form["url"]
    return jsonify("updated display to {}".format(request.form["url"]))


if __name__ == "__main__":
    app.run(debug=True)
