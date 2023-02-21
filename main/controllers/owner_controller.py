import pdb
from flask import Flask, render_template, redirect, request, Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository

owners_blueprint = Blueprint('owners', __name__)

@owners_blueprint.route('/owners')
def owners():
    owners = owner_repository.select_all()
    return render_template('owners/index.html', owners=owners)

@owners_blueprint.route('/owners/<id>')
def view_owner(id):
    pets = pet_repository.select_all()
    owner = owner_repository.select(id)
    return render_template('owners/show.html', owner=owner, pets=pets)

@owners_blueprint.route('/owners/add', methods=['GET'])
def add_owner():
    return render_template('/owners/add.html')

@owners_blueprint.route('/owners', methods=['POST'])
def create_owner():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    contact = request.form['contact']
    owner = Owner(first_name, last_name, address, contact)
    owner_repository.save(owner)
    return redirect('/owners')

@owners_blueprint.route('/owners/<id>/delete', methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')

@owners_blueprint.route('/owners/<id>/edit', methods=['GET'])
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('/owners/edit.html', owner=owner)

@owners_blueprint.route('/owners/<id>/update', methods=['POST'])
def update_owner(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    contact = request.form['contact']
    active = request.form['active']
    owner = Owner(first_name, last_name, address, contact, active, id)
    owner_repository.update(owner)
    return redirect('/owners')
