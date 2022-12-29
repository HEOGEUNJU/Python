from flask import Flask, render_template
from flask.globals import request
import psycopg2
from flask.json import jsonify
from day14.dao_teacher import Daoteacher
import time

app = Flask(__name__)

@app.route('/')
@app.route('/three')
def teacher():
    return render_template('three.html')



if __name__ == '__main__':
    app.run(debug=True)