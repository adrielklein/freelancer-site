import smtplib

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("adrielmklein2@gmail.com", "Dogsareawesome")

    msg = """From:
To:
Subject: New Message from {0}

Congrats me! I just got a new message from a potential client!
name: {0}
email: {1}
phone: {2}
message: {3}
""".format(request.form['name'], request.form['email'], request.form['phone'], request.form['message'])

    server.sendmail("", "adrielmklein@gmail.com", msg)
    server.quit()
    return 'OK'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
