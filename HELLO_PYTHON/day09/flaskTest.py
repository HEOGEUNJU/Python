from flask import Flask, render_template
from flask.globals import request
import psycopg2
from day09.dao_sample import DaoSample

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Python'

@app.route('/param')
def param():
    a = request.args.get('a', 'babo')
    return "param:" + a

@app.route('/post', methods=['POST'])
def post():
    a = request.form['a']
    return "post:"+a

@app.route('/sample')
def sample():
    ds = DaoSample()
    list = ds.selects()
    return str(list)
    
    '''
    txt= """
        hello
    """    
    
    conn = psycopg2.connect(host = "127.0.0.1", dbname = "python", user = "postgres", password = "python")

    cur = conn.cursor()
    cur.execute("select col01, col02, col03 from sample")
    rows = cur.fetchall()
   
    txt += str(rows)
    cur.close()
    conn.close()
    
    return txt
    '''
    
@app.route('/view')
def view():
    a = "홍길동"
    b = ["바보", "천재", "미남"]
    c = [
            {'col01':'1','col02':'1','col03':'1'},
            {'col01':'2','col02':'2','col03':'2'}
        ]
    return render_template('view.html', a=a, b=b, c=c)

    
    
if __name__ == '__main__':
    app.run(debug=True)