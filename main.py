import requests
from flask import Flask, render_template, request
from smtplib import SMTP

MY_EMAIL = 'uzzal.official@yahoo.com'
MY_PASSWORD = 'aifrfksshezjaqos'

all_posts = requests.get("https://api.npoint.io/e42b353ee387383898c7").json()

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')  # , methods=['GET', 'POST']
def connect():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post['id'] == index:
            return render_template("post.html", requested_post=post)


@app.route('/contact', methods=['POST', 'GET'])  #
def contact():
    if request.method == 'POST':
        form_data = request.form
        send_email(
            form_data['name'],
            form_data['email'],
            form_data['phone'],
            form_data['message']
        )
        return render_template('contact.html', msg_send=True)

    return render_template('contact.html', msg_send=False)


def send_email(name, email, phone, msg):
    with SMTP('smtp.mail.yahoo.com') as yahoo:
        email_msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{msg}"
        yahoo.starttls()
        yahoo.login(user=MY_EMAIL, password=MY_PASSWORD)
        yahoo.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_msg)


if __name__ == "__main__":
    app.run(debug=True)
