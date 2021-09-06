from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, URL, NumberRange, Optional

class AddPetForm(FlaskForm):

    name        = StringField("Name", validators=[InputRequired()])
    species     = StringField("Species", validators=[InputRequired()])
    photo_url   = StringField("Photo URL", validators=[Optional(), URL()])
    age         = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes       = StringField("Notes", validators=[Optional()])
    available   = BooleanField("Available?", validators=[InputRequired()], default=True)

class EditPetForm(FlaskForm):

    photo_url   = StringField("Photo URL", validators=[Optional(), URL()])
    notes       = StringField("Notes", validators=[Optional()])
    toggle_available   = BooleanField("Toggle Availablility (leave unchecked for no change)", validators=[Optional()])