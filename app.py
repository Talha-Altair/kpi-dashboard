from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/teachers', methods=['GET', 'POST'])
def teachers():

    if request.method == 'POST':

        payload = dict(request.form)

        

        return render_template('teachers.html', alert_msg='Teacher added successfully!')

    return render_template('teachers.html')

if __name__ == '__main__':
    app.run(debug=True)