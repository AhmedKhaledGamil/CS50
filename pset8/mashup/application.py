import os
import re
from flask import Flask, jsonify, render_template, request

from cs50 import SQL
from helpers import lookup

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Render map"""
    if not os.environ.get("API_KEY"):
        raise RuntimeError("API_KEY not set")
    return render_template("index.html", key=os.environ.get("API_KEY"))


@app.route("/articles")
def articles():
    """Look up articles for geo"""

    # TODO

    # return the geo argument from the HTML Url
    geo = request.args.get("geo")

    # check if there is an argument or not
    if not geo:
        raise RuntimeError("Location is not specified")

    # return the articles in JSON format
    articles = lookup(geo)

    # return 6 articles only
    articles_6 = articles[:6]

    return jsonify(articles_6)


@app.route("/search")
def search():
    """Search for places that match query"""

    # TODO

    # the + "%" is for autocomplete functionalty so it matches any number of characters
    q = request.args.get("q") + "%"

    space = False
    coma = False


    for i in q:
        if i == ' ':
            space = True
            break
        elif i == ',':
            coma = True
            break

    if space:
        inputs = q.split(" ")
        if len(inputs) == 2:
            data = db.execute("SELECT * FROM places WHERE place_name LIKE :a AND admin_code1 LIKE :b OR place_name LIKE :a AND admin_name1 LIKE :b", a=inputs[0], b=inputs[1])
        else:
            data = db.execute("SELECT * FROM places WHERE place_name LIKE :a AND admin_code1 LIKE :c AND admin_name1 LIKE :b OR place_name LIKE :a AND country_code LIKE :c AND admin_name1 LIKE :b", a=inputs[0], b=inputs[1], c=inputs[2])
    elif coma:
        inputs = q.split(',')
        if len(inputs) == 2:
            data = db.execute("SELECT * FROM places WHERE place_name LIKE :a AND admin_code1 LIKE :b OR place_name LIKE :a AND admin_name1 LIKE :b", a=inputs[0], b=inputs[1][1:])
        else:
            data = db.execute("SELECT * FROM places WHERE place_name LIKE :a AND admin_code1 LIKE :c AND admin_name1 LIKE :b OR place_name LIKE :a AND country_code LIKE :c AND admin_name1 LIKE :b", a=inputs[0], b=inputs[1][1:], c=inputs[2][1:])
    else:
        data = db.execute("SELECT * FROM places WHERE postal_code LIKE :q OR place_name LIKE :q", q=q)

    return jsonify(data)


@app.route("/update")
def update():
    """Find up to 10 places within view"""

    # Ensure parameters are present
    if not request.args.get("sw"):
        raise RuntimeError("missing sw")
    if not request.args.get("ne"):
        raise RuntimeError("missing ne")

    # Ensure parameters are in lat,lng format
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("sw")):
        raise RuntimeError("invalid sw")
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("ne")):
        raise RuntimeError("invalid ne")

    # Explode southwest corner into two variables
    sw_lat, sw_lng = map(float, request.args.get("sw").split(","))

    # Explode northeast corner into two variables
    ne_lat, ne_lng = map(float, request.args.get("ne").split(","))

    # Find 10 cities within view, pseudorandomly chosen if more within view
    if sw_lng <= ne_lng:

        # Doesn't cross the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude AND longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    else:

        # Crosses the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude OR longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    # Output places as JSON
    return jsonify(rows)
