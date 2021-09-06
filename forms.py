from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.fields.core import SelectField
from wtforms.validators import InputRequired, URL, NumberRange, Optional

class AddPetForm(FlaskForm):
    """Form class for adding a pet"""

    name        = StringField("Name", validators=[InputRequired()])
    species     = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")], validators=[InputRequired()])
    photo_url   = StringField("Photo URL", validators=[Optional(), URL()])
    age         = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes       = StringField("Notes", validators=[Optional()])
    available   = BooleanField("Available?", default=True)

class EditPetForm(FlaskForm):
    """Form class for editing pet"""

    photo_url   = StringField("Photo URL", validators=[Optional(), URL()])
    notes       = StringField("Notes", validators=[Optional()])
    toggle_available   = BooleanField("Toggle Availablility (leave unchecked for no change)", validators=[Optional()])