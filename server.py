from flask import Flask, render_template
import random
import datetime
import requests

AGIFY_APPI = "6070ffa4bc68053296d3249dd23ae3d1"


app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def get_age_and_gender(name):
    params = {"name": name}
    agify_response = requests.get(url="https://api.agify.io", params=params)
    agify_response.raise_for_status()
    agify_data = agify_response.json()["age"]
    genderize_response = requests.get(url="https://api.genderize.io", params=params)
    genderize_response.raise_for_status()
    genderize_data = genderize_response.json()["gender"]
    return render_template("guess.html", name=name.capitalize(), age=agify_data, gender=genderize_data)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url=blog_url)
    blog_posts = blog_response.json()
    return render_template("blog.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)