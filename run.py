import os

from flask import Flask
from flask import render_template
from flask import request
from postmark import PMMail

PORT = 5000
app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    msg = """Congrats me! I just got a new message from a potential client!
    name: {0}
    email: {1}
    phone: {2}
    message: {3}
    """.format(request.form['name'], request.form['email'], request.form['phone'], request.form['message'])

    message = PMMail(api_key=os.environ.get('POSTMARK_API_TOKEN'),
                     subject="New message from {0}".format(request.form['name']),
                     sender="adriel@adrielklein.com",
                     to="adrielmklein@gmail.com",
                     text_body=msg)

    message.send()
    return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', PORT)))
