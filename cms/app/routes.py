from app import app,db
from flask import redirect,render_template,url_for
from flask_login import login_user,LoginManagercurrent_user, LoginManager,login_user, logout_user,login_required
from models import *

loginmanager=LoginManager()
loginmanager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return 

@app.route('/'.methods=["GET"])

def home():
    return render_template("home.html")

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route('/logout',methods=["GET","POST"])
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/teacher',methods=["POST"])
def teacher():
     
     if :
         #query
         login_user()
         return render_template('teacher.html',args=args)
     else:

         return redirect(url_for('login'))

@app.route('/student',methods=["POST"])
def student():
    #query
     if :
         #query
         return render_template('student.html',args=args)
     else:

         return redirect(url_for('login'))   

@app.route('/admin',methods=["POST"])
def admin():
    #query
     if :
         #query
         return render_template('admin.html',args=args)
     else:

         return redirect(url_for('login'))             

