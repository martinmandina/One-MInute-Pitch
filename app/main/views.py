from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    pitches = Pitch.query.all()
    interview =  Pitch.query.filter_by(category = 'interview').all() 
    product =  Pitch.query.filter_by(category = 'product').all() 
    promotion =  Pitch.query.filter_by(category = 'promotion').all() 
    advertisement =  Pitch.query.filter_by(category = 'advertisement').all()
      return render_template('index.html', interview = interview,product = product,promotion = promotion,advertisement = advertisement)



