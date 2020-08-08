from app import app,db
from flask import redirect,render_template,url_for,session
from app.models import *
from twilio.rest import Client
from pytube import YouTube

@app.route('/notif', methods=["GET"])
def notif():
    resources = Resource.query.all()
    return render_template("notif.html")    


@app.route('/download', methods=["GET", "POST"])
def download():
    
    print("pls work")
    yturl = 'https://www.youtube.com/watch?v=C99rqP-lMjM'
    yt = YouTube(yturl)
    if yt.age_restricted == False:
        filters = yt.streams.filter(progressive=True, file_extension='mp4').first()
        filters.download()
    else:
        flash("Age restricted video")
    

@app.route('/download_res', methods=["GET", "POST"])
def download_res():
    #video
    youtube_api = "##"
    return render_template('download_res.html', youtube_api=youtube_api)

@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route('/search')
def search():
    resources = Resource.query.all()
    return render_template('search.html',resources=resources)


@app.route('/logout<usertype>',methods=["GET","POST"])
def logout(usertype):
    session.pop(usertype,None)
    return redirect(url_for('home'))

@app.route('/teacher',methods=["POST"])
def teacher():
    if 'teacher' in session:
        teach=session['teacher']
        return render_template('teacher.html',teach=teach)
    else :
        username = request.form["username"]
        password = request.form["password"]
        teach = Teacher.query.filter_by(username = username)
        if not teach is None:
            session['teacher']=teach
            return render_template('teacher.html',teach=teach)
        else :
            return redirect(url_for('login'))        

@app.route('/student',methods=["POST"])
def student():
    if 'student' in session:
        stud=session['student']
        return render_template('student.html',stud=stud)
    else :
        username = request.form["username"]
        password = request.form["password"]
        stud = student.query.filter_by(username = username)
        if not stud is None:
            session['student']=stud
            return render_template('student.html',stud=stud)
        else :
            return redirect(url_for('login'))  

@app.route('/admin',methods=["POST"])
def admin():
    if 'admin' in session:
        adm=session['admin']
        return render_template('admin.html',adm=adm)
    else :
        username = request.form["username"]
        password = request.form["password"]
        adm = Admin.query.filter_by(username = username)
        if not adm is None:
            session['student']=stud
            return render_template('admin.html',adm=adm)
        else :
            return redirect(url_for('login'))    

