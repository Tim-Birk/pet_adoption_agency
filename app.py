"""Pet adoption application."""

from flask import Flask, render_template, flash, redirect
from models import Pet, db, connect_db
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def index_page():
    """List top 25 pets"""

    pets = Pet.query.limit(25).all()
    return render_template("pet-list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if not form.photo_url.data == "" else None
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        flash(f"Added {name} the {species}!","success")

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template(
            "add-pet-form.html", form=form)

@app.route("/<int:id>")
def show_pet_details(id):
    """Show pet details page"""

    pet = Pet.query.get_or_404(id)
    return render_template("pet-details.html", pet=pet)

@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_user(id):
    """Show pet edit form and handle edit."""

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data if not form.photo_url.data == "" else None
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Updated {pet.name} the {pet.species}!","success")
        return redirect(f"/{id}")

    else:
        return render_template("edit-pet-form.html", form=form)

@app.route("/<int:id>/delete", methods=["POST"])
def delete_user(id):
    """Delete pet from database"""

    pet = Pet.query.get_or_404(id)
    try:
        pet = Pet.query.filter_by(id=id).first()
        db.session.delete(pet)
        db.session.commit()

        flash("Pet deleted", "success")
    except Exception as e:
        flash(f"There was an error deleting the user: {e}", "error")
        return redirect(f"/{id}")

    return redirect(f"/")