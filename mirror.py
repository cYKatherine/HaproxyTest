from flask import Flask, url_for, jsonify
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def index():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return f'index: {out}'

@app.route('/test')
def login():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return f'test: {out}'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))