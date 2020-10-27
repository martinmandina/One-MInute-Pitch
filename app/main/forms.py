from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("Add Your Pitch Here",validators=[Required()])
	category = RadioField('Label', choices=[ ('pickuplinespitch','Pickuplinespitch'), ('interviewpitch','Interviewpitch'),('promotion','Promotion')],validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
