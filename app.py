import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Pet
from models import Owner

@app.route("/")
def hello():
    return "Hello World!"

# Post pet route will add pet to the database.
@app.route("/addpets", methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.args.get('name')
        owner_id = request.args.get('owner_id')
        breed = request.args.get('breed')
        color = request.args.get('color')
        checked_in = request.args.get('checked_in')
        owner_name = request.args.get('owner_name')
        try:
            pet = Pet(
                name=name,
                owner_id=owner_id,
                breed=breed,
                color=color,
                checked_in=checked_in,
                owner_name=owner_name,
            )
            db.session.add(pet)
            db.session.commit()
            return "pet added. pet id={}".format(pet.id)
        except Exception as e:
	        return(str(e))

# Post owners route will add owner to database
@app.route("/addowner", methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        name = request.args.get('name')
        try:
            owner = Owner(
                name=name,
            )
            db.session.add(owner)
            db.session.commit()
            return "owner added. owner id={}".format(owner.id)
        except Exception as e:
            return(str(e)) 

# gets all the pets from the database
@app.route("/getpets")
def get_allPets():
    try:
        pets = Pet.query.all()
        # return jsonify([e.serialize() for e in pets])
        resp = jsonify([e.serialize() for e in pets])
        resp.status_code = 200
        return resp
    except Exception as e:
	    return(str(e))

# get owners route from database
@app.route("/getowners")
def get_allOwners():
    try:
        owners = Owner.query.all()
        return jsonify([e.serialize() for e in owners])
    except Exception as e:
	    return(str(e))

#  Delete Owner Route
@app.route("/deleteowner/<int:id>", methods=['DELETE'])
def delete_owner_id(id):
    if request.method == 'DELETE':
        qry = db.session.query(Owner).filter(
                Owner.id==id)
        name = qry.first()
        try:
            # owner = Owner(
            #     id=id,
            #     name=name,
            # )
            db.session.delete(name)
            db.session.commit()
            resp = jsonify([e.serialize() for e in owner])
            resp.status_code = 200
            return resp
        except Exception as e:
            return(str(e))

#  Delete Pet Route
@app.route("/deletepet/<int:id>", methods=['DELETE'])
def delete_pet_id(id):
    if request.method == 'DELETE':
        qry = db.session.query(Pet).filter(
                Pet.id==id)
        name = qry.first()
        try:
            # owner = Owner(
            #     id=id,
            #     name=name,
            # )
            db.session.delete(name)
            db.session.commit()
            resp = jsonify([e.serialize() for e in pet])
            resp.status_code = 200
            return resp
        except Exception as e:
            return(str(e))        
    # try:
        # .delete should allow us to delete the owner or pet by id.
    #     pets = Pet.query.filter_by(id=id_).delete()
    #     return jsonify(book.serialize())
    # except Exception as e:
	    # return(str(e))

# @app.route("/add/form", methods=['GET', 'POST'])
# def add_book_form():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         author = request.form.get('author')
#         published = request.form.get('published')
#         try:
#             book = Book(
#                 name=name,
#                 author=author,
#                 published=published
#             )
#             db.session.add(book)
#             db.session.commit()
#             return "Book added. book id={}".format(book.id)
#         except Exception as e:
#             return(str(e))
#     return render_template("getdata.html")


if __name__ == '__main__':
    app.run()
