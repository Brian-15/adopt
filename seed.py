
from pet_model import Pet, db, connect_db
from app import app

connect_db(app)

db.drop_all()
db.create_all()

Pet.query.delete()

cat1 = Pet(name="Scrunchy",
           species="cat",
           age=15,
           notes="""A wonderful and friendly tabby cat.
                    Scrunchy loves to receive lots of love, pets, and playtime!
                    She's an active old lady""",
           photo_url="https://images.unsplash.com/photo-1612779068752-c6a563a34994?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80")
cat2 = Pet(name="Reglisse",
           species="cat",
           age=15,
           notes="""Shy, regal, and curious.""",
           photo_url="https://images.unsplash.com/photo-1610129079034-7db0e1627753?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80")

dog1 = Pet(name="Chompers",
           species="dog",
           age=4,
           photo_url="https://images.unsplash.com/photo-1605044085790-1f48630b58e6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=925&q=80")
           
dog2 = Pet(name="Sprocket",
           species="dog",
           age=7,
           photo_url="https://images.unsplash.com/photo-1599961403707-7d6ba8ec817c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1050&q=80",
           available=False)

db.session.add_all([cat1, cat2, dog1, dog2])
db.session.commit()