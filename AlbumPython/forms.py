from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    image_url = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Guardar Foto')
