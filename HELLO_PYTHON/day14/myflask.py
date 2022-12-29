from flask import Flask, render_template
from flask.globals import request
import psycopg2
from flask.json import jsonify
from day14.dao_teacher import Daoteacher

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('teacher.html')

@app.route('/teacher_list_ajax', methods=['POST'])
def ajax():
    # data = request.get_json()
    # print(data)
    de = Daoteacher()
    list = de.selects()
    print(list)
    return jsonify(list = list)

@app.route('/ajax_teacher_one', methods=['POST'])
def ajax_teacher_one():
    dict = request.get_json()
    t_id = dict['t_id']
    de = Daoteacher()
    teacher = de.select(t_id)
    print(teacher)
    return jsonify(teacher = teacher)

@app.route('/ajax_teacher_add', methods=['POST'])
def ajax_teacher_add():
    dict    = request.get_json()
    print(dict)
    t_name  = dict['t_name']
    mobile  = dict['mobile']
    addr    = dict['addr']
    de = Daoteacher()
    cnt = de.insert(t_name, mobile, addr)
    print(cnt)
    return jsonify(cnt = cnt)

@app.route('/ajax_teacher_delete', methods=['POST'])
def ajax_teacher_delete():
    dict = request.get_json()
    # print(dict['t_id'])
    t_id = dict['t_id']
    de = Daoteacher()
    cnt = de.delete(t_id)
    print(cnt)
    return jsonify(cnt = cnt)

@app.route('/ajax_teacher_update', methods=['POST'])
def ajax_teacher_update():
    dict = request.get_json()
    t_id    = dict['t_id']
    t_name  = dict['t_name']
    mobile  = dict['mobile']
    addr    = dict['addr']
    # print(dict['t_id'])
    de = Daoteacher()
    cnt = de.update(t_id, t_name, mobile, addr)
    print(cnt)
    return jsonify(cnt = cnt)
    
if __name__ == '__main__':
    app.run(debug=True)