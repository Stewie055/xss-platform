from rabit import app,db
from flask import session, redirect, url_for, escape, request, render_template, send_from_directory
import pymongo
from datetime import datetime

USERNAME = 'rabitxss'
PASSWORD = 'rabitpass'


@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('signin'))
    record_col = db.records
    records = []
    records = record_col.find().sort('time',pymongo.DESCENDING)
    return render_template('index.html',records=records)


@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username',None,type=str)
        password = request.form.get('password',None,type=str)
        print(username,password)
        if username == USERNAME and password == PASSWORD:
            print('ok')
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('signin.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))

@app.route('/log',methods=['GET'])
def log():
    record = {'time':datetime.now(),
            'host':request.remote_addr,
            'request':request.args,
            'data':request.form}
    db.records.insert(record)
    return ''


