from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Pitch,Category
# from .forms import ReviewForm,UpdateProfile
from flask_login import login_required,current_user

@main.route('/')
def index():
    pitches = Pitch.query.all()
    pickuplines= Pitch.query.filter_by(category = 'Pickuplines').all() 
    interview = Pitch.query.filter_by(category = 'Interview').all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    
    title = "Pitches - A Minute Pitch Website One liner"

    return render_template('index.html',title = title, pitches = pitches,pickuplines = pickuplines,promotion = promotion,interview = interview)


