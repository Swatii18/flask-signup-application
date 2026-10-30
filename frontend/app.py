from flask import Flask, request, render_template
from datetime import datetime
import requests
from flask import redirect, url_for, flash

BACKEND_URL = 'http://127.0.0.1:9000'

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def home():
    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)

    try:
        response = requests.post(BACKEND_URL + '/submit', json=form_data)

        if response.ok:
            return redirect(url_for('success'))
        else:
            flash('Failed to submit data.', 'error')
            return render_template('index.html')

    except requests.exceptions.RequestException:
        flash('Failed to submit data.', 'error')
        return render_template('index.html')

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL + '/View')

    return response.json()
    # data = response.json()
    # return render_template('data.html', data=data['data'])
@app.route('/Success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
