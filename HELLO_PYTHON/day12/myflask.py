from flask import Flask, render_template
from flask.globals import request
import psycopg2
from day09.dao_sample import DaoSample
from flask.json import jsonify
from day10.dao_emp import DaoEmp

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    # data = request.get_json()
    # print(data)
    de = DaoEmp()
    list = de.selects()
    print(list)
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    e_id = dict['e_id']
    de = DaoEmp()
    emp = de.select(e_id)
    print(emp)
    return jsonify(emp = emp)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    # print(dict['e_id'])
    de = DaoEmp()
    cnt = de.insert(dict['e_id'], dict['e_name'], dict['sex'], dict['e_addr'])
    print(cnt)
    return jsonify(cnt = cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    dict = request.get_json()
    # print(dict['e_id'])
    e_id = dict['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id)
    print(cnt)
    return jsonify(cnt = cnt)

@app.route('/ajax_update', methods=['POST'])
def ajax_update():
    dict = request.get_json()
    print(dict)
    de = DaoEmp()
    cnt = de.update(dict['e_id'], dict['e_name'], dict['sex'], dict['e_addr'])
    print(cnt)
    return jsonify(cnt = cnt)
    
if __name__ == '__main__':
    app.run(debug=True)