from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Pitch,Cate
from .forms import ReviewForm,UpdateProfile
from flask_login import login_required,current_user

@main.route('/')
def index():
    pitches = Pitch.pitches.query.all()
    InterviewPitch = Pitch.query.filter_by(category_id="InterviewPitch")
    title = "Pitches - A MInute Pitch One liner"

    return render_template('index.html',title = title,InterviewPitch = InterviewPitch )


