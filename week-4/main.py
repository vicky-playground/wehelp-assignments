from collections import UserString
from email import message
from flask import Flask, render_template, redirect, url_for, request, session
from flaskext.mysql import MySQL
import pymysql
pymysql.install_as_MySQLdb()
import pymysql.cursors
import re
import mysql.connector
import datetime

app = Flask(__name__,template_folder="templates")

# for extra protection
app.secret_key = '12345678'


"""
# connect to the local DB
conn = pymysql.connect(host = "localhost", user = "root", password="12345678", database='pythonlogin')
cursor = conn.cursor(pymysql.cursors.DictCursor)
"""

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username}>'
        
users = []
users.append(User(id=1, username="test", password = "test"))

# http://127.0.0.1:3000/signin
@app.route('/signin')
def signin():
    return redirect(url_for("member"))

# http://127.0.0.1:3000/member/
@app.route('/member/')
def member():
    if 'username' not in session:
        return redirect(url_for("login"))
    return render_template("home.html")

# http://127.0.0.1:3000/error/
@app.route('/error/')
def error():
    return render_template("error.html")

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('login'))
        
@app.route('/', methods=['GET', 'POST'])
def login():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        session.pop('username', None)

        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        """
        # Check if user exists using MySQL 
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        # Fetch one record and return result
        user = cursor.fetchone()
        
        # If user doesn't exist in users table 
        if user is None:
            #Redirect to error page
            return redirect(url_for('error',message= "登入失敗唷！"))
        # user exists in users table 
        elif len(user) > 0:
            # set the session variable
            session['username'] = username
            #Redirect to signin page
            return redirect(url_for('signin'))
        """

        user = [x for x in users][0]
        if user.username == username and user.password == password:
            session["username"] = username
            return redirect(url_for('signin'))
        elif user.username != username or user.password != password:
            return redirect(url_for('error',message= "登入失敗唷！"))
        return redirect(url_for("login"))
    return render_template('index.html') 


# http://127.0.0.1:3000/
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True, debug=True)