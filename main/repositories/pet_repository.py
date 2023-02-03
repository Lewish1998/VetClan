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
        pdb.set_trace()
        owner = owner_repository.select(results[owner]) # To Fix
        vet = vet_repository.select(result[id]) # To Fix
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

def owners(pet):
    owners = []
    # sql = 'SELECT owners.* FROM owners INNER JOIN pets ON pets.owner_id = owners.id WHERE pet_id = %s' # Not working. Need to understand the connection
    pass