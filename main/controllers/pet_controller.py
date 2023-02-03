from flask import Flask, render_template, redirect, request, Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository

pets_blueprint = Blueprint('pets', __name__)

@pets_blueprint.route('/pets')
def pets():
    pets = pet_repository.select_all()
    return render_template('pets/index.html', pets=pets)

@pets_blueprint.route('/pets/<id>')
def view_pet(id):
    pet = pet_repository.select(id)
    return render_template('/pets/show.html', pet=pet)