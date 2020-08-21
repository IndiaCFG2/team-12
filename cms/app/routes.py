from app import app,db
from flask import redirect,render_template,url_for,session
from app.models import *
from twilio.rest import Client
from pytube import YouTube
from flask import request, flash
from app.helpers import whatsapp, sms, mail

@app.route('/course', methods=["GET"])
def course():
    resources = Resource.query.all()
    return render_template("course.html")    

@app.route('/notif', methods=["GET", "POST"])
def notif():
    whatsapp()    
    sms()
    mail()
    resources = Resource.query.all()
    sessions = Session.query.all()    
    return render_template('teacher-dashborad.html',resources=resources, sessions = sessions)    
   
@app.route('/signup', methods=["GET", "POST"])
def signup():
    flash("For notifications add twilio_number to your contacts and start your conversation in whatsapp as twilio_code ")
    return render_template('register.html')


@app.route('/download', methods=["GET", "POST"])
def download():
        
    yturl = ''
    yt = YouTube(yturl)
    if yt.age_restricted == False:
        filters = yt.streams.filter(progressive=True, file_extension='mp4').first()
        filters.download()
    else:
        flash("Age restricted video")

    return render_template('student.html')

    

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



@app.route('/logout',methods=["GET","POST"])
def logout():    
    return redirect(url_for('login'))

@app.route('/teacher',methods=["GET", "POST"])
def teacher():
    resources = Resource.query.all()
    sessions = Session.query.all()    
    return render_template('teacher-dashborad.html',resources=resources, sessions = sessions)    


@app.route('/student',methods=["POST","GET"])
def student():
    
    
    return render_template('student.html')
     

@app.route('/admin',methods=["POST", "GET"])
def admin():
    
    return render_template('admin.html')
      

