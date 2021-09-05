from flask import Flask, request, render_template, redirect
from pet_model import Pet, db, connect_db
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

