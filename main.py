import requests
from flask import Flask, render_template

all_posts = requests.get("https://api.npoint.io/e42b353ee387383898c7").json()

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def connect():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post['id'] == index:
            return render_template("post.html", requested_post=post)


if __name__ == "__main__":
    app.run(debug=True)
