from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def connect():
	return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    pass


if __name__ == "__main__":
    app.run(debug=True)
