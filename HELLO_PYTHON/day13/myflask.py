from flask import Flask, render_template
from flask.globals import request
import psycopg2
from flask.json import jsonify
from day13.dao_student import Daostudent

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    # data = request.get_json()
    # print(data)
    de = Daostudent()
    list = de.selects()
    print(list)
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    s_id = dict['s_id']
    de = Daostudent()
    Student = de.select(s_id)
    print(Student)
    return jsonify(Student = Student)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    # print(dict['s_id'])
    de = Daostudent()
    cnt = de.insert(dict['s_id'], dict['s_name'], dict['mobile'], dict['addr'])
    print(cnt)
    return jsonify(cnt = cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    dict = request.get_json()
    # print(dict['s_id'])
    s_id = dict['s_id']
    de = Daostudent()
    cnt = de.delete(s_id)
    print(cnt)
    return jsonify(cnt = cnt)

@app.route('/ajax_update', methods=['POST'])
def ajax_update():
    dict = request.get_json()
    print(dict)
    de = Daostudent()
    cnt = de.update(dict['s_id'], dict['s_name'], dict['mobile'], dict['addr'])
    print(cnt)
    return jsonify(cnt = cnt)
    
if __name__ == '__main__':
    app.run(debug=True)