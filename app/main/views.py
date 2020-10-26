from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    pitches = Pitch.pitches.query.all()
    InterviewPitch = Pitch.query.filter_by(category_id="InterviewPitch")
    title = "Pitches - A MInute Pitch One liner"

    return render_template('index.html',title = title,InterviewPitch = InterviewPitch )

@
