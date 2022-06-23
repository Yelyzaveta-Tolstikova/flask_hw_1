import random
import string
from faker import Faker
import pandas as pd
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'Home Work #2 - Tolstikova Yelyzaveta'


@app.route("/requirements/")
def get_requirements():
    with open('requirements.txt', 'r') as file:
        lines = file.read().replace('\n', '<br>')
        return lines


@app.route('/generate-users/')
def generate_users():
    get_params = request.args.get('count', default=100, type=int)
    users = {
        Faker().first_name(): ''.join(random.choices(string.ascii_lowercase, k=random.randrange(5, 7))) + '@mail.com'
        for _ in range(get_params)
    }
    return render_template('generate_user.html', users_count=get_params, users=users)


@app.route("/mean/")
def average_height_weight():
    data = pd.read_csv(r'hw.csv')
    average_height = round(data['Height(Inches)'].median()*2.54, 2)
    average_weight = round(data['Weight(Pounds)'].median()*2.205, 2)
    return f'<b>Average Height:</b> {str(average_height)} cm<br><b>Average Weight:</b> {str(average_weight)} kg'


@app.route("/space/")
def space():
    number = requests.get('http://api.open-notify.org/astros.json').json()['number']
    return f'<b>Number of astronauts</b>: {number}'
