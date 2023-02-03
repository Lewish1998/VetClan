from flask import Flask, render_template, redirect, request, Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint('owners', __name__)

@owners_blueprint.route('/owners')
def owners():
    owners = owner_repository.select_all()
    return render_template('owners/index.html', owners=owners)

@owners_blueprint.route('/owners/<id>')
def view_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/show.html', owner=owner)