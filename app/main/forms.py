from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField("Pitch Title")
    category = SelectField(u"Pitch Category",choices=[("Social Welfare Pitch", "Social Welfare Pitch"),("Business","Business"),("General","General"),("Something hilarious","Something hilarious")])
    pitch = TextAreaField('Pitch')
    submit = SubmitField("Submit")

# add comment

class CommentForm(FlaskForm):
    
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

# update profile

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')