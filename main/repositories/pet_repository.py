import pdb
from db.run_sql import run_sql
from models.pet import Pet
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save(pet):
    sql = 'INSERT INTO pets (owner_id, vet_id, name, age, type, issues, notes) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id'
    values = [pet.owner.id, pet.vet.id, pet.name, pet.age, pet.type, pet.issues, pet.notes]
    results = run_sql(sql, values)
    pet.id = results[0]['id']
    return pet

def select_all():
    pets = []
    sql = 'SELECT * FROM pets'
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(owner, vet, row['name'], row['age'], row['type'], row['issues'], row['notes'], row['id'])
        pets.append(pet)
    return pets



# unable to access owne and vet based on the pet id.
def select(id):
    pet = None
    sql = 'SELECT * FROM pets WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        result = results[0]
        pet = Pet(owner, vet, result['name'], result['age'], result['type'], result['issues'], result['notes'], result['id'])
    return pet


def delete_all():
    sql = 'DELETE FROM pets'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM pets WHERE id = %s'
    values = [id]
    run_sql(sql, values)


def update(pet):
    sql = 'UPDATE pets SET (name, age, type, issues, notes, vet_id, owner_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [pet.name, pet.age, pet.type, pet.issues, pet.notes, pet.vet_id, pet.owner_id, pet.id]
    run_sql(sql, values)
