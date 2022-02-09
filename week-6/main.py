from collections import UserString
from email import message
from flask import Flask, flash, render_template, redirect, url_for, request, session
from flaskext.mysql import MySQL
import pymysql
pymysql.install_as_MySQLdb()
import pymysql.cursors
import re
import mysql.connector
import datetime
import os

app = Flask(__name__,template_folder="templates")

# for extra protection
app.secret_key = os.urandom(24)

# connect to the local DB
conn = pymysql.connect(host = "localhost", user = "root", password="12345678", database='website')
cursor = conn.cursor(pymysql.cursors.DictCursor)

# http://127.0.0.1:3000/signin
@app.route('/signin', methods=['GET', 'POST'])
def signin():   
    # Create variables for easy access
    username = request.form['username']
    password = request.form['password']
        
    # Check if user exists using MySQL 
    sql = "SELECT * FROM member WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    # Fetch one record and return result
    user = cursor.fetchone()
        
    # If user doesn't exist in member table 
    if user is None:
        # make sure session is empty
        session.clear()
        flash('帳號或密碼輸入錯誤')
        #Redirect to error page
        return redirect(url_for('error',message= "帳號或密碼輸入錯誤"))
    # user exists in member table 
    elif len(user) > 0:
        # set the session variable
        cursor.execute("SELECT name FROM member WHERE username = %s and password = %s", (username, password))
        user = cursor.fetchone()
        session['name'] = user['name']
        #Redirect to member page
        return redirect(url_for('member'))
        
        

# http://127.0.0.1:3000/member/
@app.route('/member/')
def member():
    # check if the users exist or not
    if 'name' not in session:
        # if not there in the session then redirect to the login page
        return redirect(url_for("login"))
    return render_template("home.html")

# http://127.0.0.1:3000/error/
@app.route('/error/', methods=['GET', 'POST'])
def error():
    return render_template("error.html")

# http://127.0.0.1:3000/signout
@app.route('/signout')
def signout():
    if request.method == "GET":
     # remove the username from the session if it is there
        session.pop('name', None)
        return redirect(url_for('login'))

# http://127.0.0.1:3000/  
@app.route('/', methods=['GET', 'POST'])
def login():
    # signup process
    if request.method == 'POST' and 'name' in request.form and 'username' in request.form and 'password' in request.form:   
        return redirect(url_for("signup"))

    # signin process
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:   
        return redirect(url_for("signin")) 
         
    return render_template('index.html') 

# http://127.0.0.1:3000/signup 
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Create variables for easy access
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
        
    # Check if username exists using MySQL 
    sql = "SELECT * FROM member WHERE username = %s"
    cursor.execute(sql, (username))
    # Fetch one record and return result
    user = cursor.fetchone()
        
    # If user doesn't exist in member table 
    if user is None:
        sql = "INSERT INTO member(name,username, password) VALUES (%s,%s,%s)"
        cursor.execute(sql, (name, username, password))
        flash('會員註冊成功')
        # make sure session is empty
        session.clear()

    # user exists in member table 
    elif len(user) > 0:
        # make sure session is empty
        session.clear()
        flash('帳號已經被註冊')
        #Redirect to error page
        return redirect(url_for('error',message= "帳號已經被註冊"))
    
    return redirect(url_for("login")) 


# http://127.0.0.1:3000/
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True, debug=True)