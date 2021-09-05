from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField

class AddPetForm(FlaskForm):

    name        = StringField("Name")
    species     = StringField("Species")
    photo_url   = StringField("Photo URL")
    age         = IntegerField("Age")
    notes       = StringField("Notes")
    available   = BooleanField("Available?")