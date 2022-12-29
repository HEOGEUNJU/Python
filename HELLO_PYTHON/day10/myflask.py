from flask import Flask, render_template
from flask.globals import request
import psycopg2
from day10.dao_emp import DaoEmp
from day10 import dao_emp

app = Flask(__name__)

@app.route('/')
@app.route('/emp_list')
def emp_list():
    ds = DaoEmp()
    list = ds.selects()
    return render_template('emp_list.html', list=list)


@app.route('/emp_detail')
def emp_detail():
    e_id = request.args.get('e_id','')
    ds = DaoEmp()
    emp = ds.select(e_id)
    return render_template('emp_detail.html', emp=emp)


@app.route('/emp_edit')
def emp_edit():
    e_id = request.args.get('e_id','')
    ds = DaoEmp()
    emp = ds.select(e_id)
    return render_template('emp_edit.html', emp=emp)


@app.route('/emp_edit_act', methods=['POST'])
def emp_edit_act():
    e_id= request.form['e_id']
    e_name= request.form['e_name']
    sex= request.form['sex']
    addr= request.form['addr']
    ds = DaoEmp()
    cnt = ds.update(e_id, e_name, sex, addr)
    return render_template('emp_edit_act.html', cnt=cnt)

@app.route('/emp_add')
def emp_add():
    return render_template('emp_add.html')


@app.route('/emp_add_act',  methods=['POST'])
def emp_add_act():
    e_id= request.form['e_id']
    e_name= request.form['e_name']
    sex= request.form['sex']
    addr= request.form['addr']
    ds = DaoEmp()
    cnt = ds.insert(e_id, e_name, sex, addr)
    return render_template('emp_add_act.html', cnt=cnt)


@app.route('/emp_del_act', methods=['POST'] )
def emp_del_act():
    e_id= request.form['e_id']
    ds = DaoEmp()
    cnt = ds.delete(e_id)
    return render_template('emp_del_act.html', cnt=cnt)
    
    
if __name__ == '__main__':
    app.run(debug=True)
   