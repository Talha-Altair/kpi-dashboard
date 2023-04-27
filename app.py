from flask import Flask, render_template, request
from settings import HOST, PORT, BACKEND_URL
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        payload = dict(request.form)

        _file = request.files['file']

        payload['file'] = _file.read().decode("utf-8")

        res = requests.post(BACKEND_URL + "/upload", json=payload)

        if res.status_code != 200:

            return render_template("upload.html", alert_msg="Something went wrong!")

        return render_template("upload.html", alert_msg="Data uploaded successfully!")

    return render_template("upload.html")

@app.route("/teachers", methods=["GET", "POST"])
def teachers():
    if request.method == "POST":

        payload = dict(request.form)

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

@app.route("/subjects/pass", methods=["GET", "POST"])
def subjectspass():

    if request.method == "POST":

        payload = dict(request.form)

        res = requests.post(BACKEND_URL + "/teaching/add_pass_fail", json=payload)

        if res.status_code != 200:

            return render_template("endsem_pass_fail.html", alert_msg="Something went wrong!")

        return render_template("endsem_pass_fail.html", alert_msg="Pass fail data added successfully!")

    return render_template("endsem_pass_fail.html")


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
