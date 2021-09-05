from logging import PercentStyle
from flask import Flask, request, render_template, redirect, flash
from flask.templating import render_template_string
from pet_model import Pet, db, connect_db
from forms import AddPetForm
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "SECRET_KITTY_CATS (^_^)"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/", methods=["GET"])
def home():

    pets = Pet.query.filter_by(available=True).all()
    return render_template("pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        flash(f"{name} has been added.")
        return redirect("/")
    
    else:
        return render_template("add_pet.html", form=form)