from flask import Flask, render_template, redirect, flash
from pet_model import Pet, db, connect_db
from forms import AddPetForm, EditPetForm
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
def list_pets():
    """List all pets"""

    pets = Pet.query.all()
    return render_template("pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """
        GET:  displays form for adding new pet.
        POST: sends new pet data to database
    """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url,
                  age=age, notes=notes, available=available)
        
        db.session.add(pet)
        db.session.commit()

        flash(f"{name} has been added.")
        return redirect("/")
    
    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:id>", methods=["GET", "POST"])
def handle_pet(id):
    """
        GET: Displays pet details and edit form.
        POST: updates pet model.
    """
    pet = Pet.query.get_or_404(id)
    form = EditPetForm()

    if form.validate_on_submit():
        
        if form.photo_url.data is not "":
            pet.photo_url = form.photo_url.data
            flash(f"{pet.name} photo URL updated.")

        if form.notes.data is not "":
            pet.notes = form.notes.data
            flash(f"{pet.name} notes updated.")
        
        if form.toggle_available.data:
            pet.available = not pet.available
            flash(f"{pet.name} is now " + ("un" if not pet.available else "") + "available")
        
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("pet.html", form=form, pet=pet)
    
@app.errorhandler(Exception)
def error_page(error):

    if isinstance(error, HTTPException):
        return render_template("error.html", error=error)
    else:
        return render_template("error.html", error=error), 500