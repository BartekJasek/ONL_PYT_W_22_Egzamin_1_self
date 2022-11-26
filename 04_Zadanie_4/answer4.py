from flask import Flask, request
import re
from psycopg2 import connect

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return """<html>
                <form method="post">
                    <p>Name:</p>
                    <p><input type="text" name="name"/></p>
                    <p>E-mail:</p>
                    <p><input type="text" name="mail"/></p>
                    <p><input type="submit" value="submit"/></p>
                </html>"""
    else:
        if re.match(r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'", request.form["mail"]):
            cnx = connect(user="postgres", password="coderslab", host="127.0.0.1")
            cnx.autocommit = True
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO Orders (name, email) VALUES (request.form['name'], request.form['mail'])"
            return "Done!"
        else:
            return "Something went wrong! Check your e-mail"


if __name__ == "__main__":
    app.run(debug=True)
