from flask import Flask, render_template
from requests import *
import datetime
import random
app = Flask(__name__)

AGIFY_API = "https://api.agify.io?"
GENDERIZE_API = "https://api.genderize.io?"
NATIONALIZE_API = "https://api.nationalize.io/?"
NPOINT_API = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route("/")
def home():
    random_integer = random.randint(1, 9)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num = random_integer, this_year = current_year)

@app.route("/guess/<user_name>")
def guess(user_name):
    parameters = {
        "name": user_name
    }
    agify = get(url = AGIFY_API, params = parameters).json()
    genderize = get(url = GENDERIZE_API, params = parameters).json()
    nationalize = get(url = NATIONALIZE_API, params = parameters).json()
    return render_template("guess.html", age = agify["age"], gender = genderize["gender"], nation = nationalize["country"][0]["country_id"], name = user_name.title())

@app.route("/blog/<num>")
def get_blog(num):
    npoint = get(url = NPOINT_API).json()
    return render_template("blog.html", blogs = npoint)

if __name__ == "__main__":
    app.run(debug = True)