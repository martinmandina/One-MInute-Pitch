from flask import render_template,request,redirect,url_for
from . import main
from .. import db,photos
from ..models import User,Pitch
from .forms import PitchForm,CommentForm,UpdateProfile
from flask_login import login_required,current_user

@main.route('/')
def index():
    pitches = Pitch.query.all()
    pickuplines= Pitch.query.filter_by(category = 'Pickuplines').all() 
    interview = Pitch.query.filter_by(category = 'Interview').all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    title = "Pitches - A Minute Pitch Website One liner"

    return render_template('index.html',title = title, pitches = pitches,pickuplines = pickuplines,promotion = promotion,interview = interview)


@main.route('/pitches', methods =  ["POST","GET"])
@login_required
def new_pitch(): 
    
    form = PitchForm()

    if form.validate_on_submit():
        description = form.description.data
        category = form.category.data
        title = form.title.data
        user_id = current_user

        print(current_user._get_current_object().id)
        new_pitch = Pitch(user_id =current_user._get_current_object().id, title = title,description=description,category=category)
        
        return redirect(url_for('main.index'))
         
    return render_template('new_pitch.html', form = form)

@main.route('/comments/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()

    post = Pitch.query.get(pitch_id)
    user = User.query.all()
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(
            comment=comment,
            pitch_id=pitch_id,
            user_id=user_id
        )
        new_comment.save()
        new_comments = [new_comment]
        print(new_comments)
        return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, post=post, comments=comments, user=user)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)  

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    form = UpdateProfile()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        error = "User does not exist"
        
        form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))  
