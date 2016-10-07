import os
import smtplib
from email.mime.text import MIMEText

from flask import Flask
from flask import render_template
from flask import request

PORT = 5000
app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    server = smtplib.SMTP('mail.adrielklein.com')

    text = """From:
To:
Subject: New Message from {0}

Congrats me! I just got a new message from a potential client!
name: {0}
email: {1}
phone: {2}
message: {3}
""".format(request.form['name'], request.form['email'], request.form['phone'], request.form['message'])
    msg = MIMEText(text)

    server.send_message(msg)
    msg['Subject'] = 'subject'
    msg['From'] = 'from'
    msg['To'] = 'to'
    server.quit()
    return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', PORT)))
