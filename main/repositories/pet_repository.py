import pdb
from db.run_sql import run_sql
from models.pet import Pet
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save(pet):
    sql = 'INSERT INTO pets (owner_id, vet_id, pet_name, age, pet_type, issues, notes) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id'
    values = [pet.owner.id, pet.vet.id, pet.name, pet.age, pet.type, pet.issues, pet.notes]
    pdb.set_trace()
    results = run_sql(sql, values)
    pet.id = results[0]['id']
    return pet

def select_all():
    pets = []
    sql = 'SELECT * FROM pets'
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet.id'])
        pet = Pet(owner, vet, row['name'], row['age'], row['type'], row['issues'], row['notes'], row['id'])
        pets.append(pet)
    return pets