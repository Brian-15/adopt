from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet model class"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    species = db.Column(db.String(), nullable=False)
    photo_url = db.Column(db.String())
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

    def __repr__(self):
        """Display pet instance information"""

        return f"<Pet {self.species} {self.id} {self.name} {self.available}>"
    