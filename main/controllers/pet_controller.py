from flask import Flask, render_template, redirect, request, Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import random

pets_blueprint = Blueprint('pets', __name__)

@pets_blueprint.route('/pets')
def pets():
    pets = pet_repository.select_all()
    return render_template('pets/index.html', pets=pets)

@pets_blueprint.route('/pets/<id>')
def view_pet(id):
    pet = pet_repository.select(id)
    return render_template('/pets/show.html', pet=pet)

@pets_blueprint.route('/pets/add', methods=['GET'])
def add_pet():
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template('pets/add.html', vets=vets, owners=owners)

@pets_blueprint.route('/pets', methods=['POST'])
def create_pet():
    name = request.form['name']
    age = request.form['age']
    type = request.form['type']
    issues = request.form['issues']
    notes = request.form['notes']
    owner = owner_repository.select(request.form['owner_id'])
    vets = vet_repository.select_all()
    vet = random.choice(vets)
    pet = Pet(owner, vet, name, age, type, issues, notes)
    pet_repository.save(pet)
    return redirect('/pets')