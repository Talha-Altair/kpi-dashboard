from flask import Flask, render_template, request
from settings import HOST, PORT, BACKEND_URL
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/teachers", methods=["GET", "POST"])
def teachers():
    if request.method == "POST":

        payload = dict(request.form)

        payload['subject_codes'] = []

        res = requests.post(BACKEND_URL + "/teaching/add", json=payload)

        if res.status_code != 200:

            return render_template("teachers.html", alert_msg="Something went wrong!")

        return render_template("teachers.html", alert_msg="Teacher added successfully!")

    return render_template("teachers.html")

@app.route("/subjects/add", methods=["GET", "POST"])
def subjectsadd():

    if request.method == "POST":

        payload = dict(request.form)

        res = requests.post(BACKEND_URL + "/teaching/addsubjects", json=payload)

        if res.status_code != 200:

            return render_template("addsubjects.html", alert_msg="Something went wrong!")

        return render_template("addsubjects.html", alert_msg="Subject added successfully!")

    return render_template("addsubjects.html")


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
