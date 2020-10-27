from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Pitch,Category
# from .forms import ReviewForm,UpdateProfile
from flask_login import login_required,current_user

@main.route('/')
def index():
    # pitches = Pitch.pitches.query.all()
    title = "Pitches - A MInute Pitch One liner"

    return render_template('index.html',title = title)


