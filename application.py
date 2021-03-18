# fontsize issues en html la linea de meta = name...

from flask import Flask, render_template, request

application = Flask(__name__)
app = application
REGISTRANTS = {}

SPORTS = [
    "Dogeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports = SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport=request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    REGISTRANTS[name] = sport
    return render_template("registrants.html", registrants = REGISTRANTS)