from flask import Flask, render_template
from requests import *
import random
import datetime
AGIFY_API_URL = "https://api.agify.io?"
GENDERIZE_API_URL = "https://api.genderize.io?"
app = Flask(__name__)
@app.route("/")
def home():
    this_year = datetime.datetime.now().year
    random_number = random.randint(0, 5)
    return render_template("index.html", number = random_number, year = this_year)
@app.route("/guess/<name>")
def agifygenderize(name):
    agify_params = {
        "name": name
    }
    genderize_params = {
        "name": name
    }
    agify = get(url = AGIFY_API_URL, params = agify_params).json()
    genderize = get(url = GENDERIZE_API_URL, params = genderize_params).json()
    return render_template("AgifyGenderize.html", Name = name.title(), Age = agify["age"], Gender = genderize["gender"])
if __name__ == "__main__":
    app.run(debug = True)