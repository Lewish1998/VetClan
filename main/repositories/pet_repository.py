from db.run_sql import run_sql
from models.pet import Pet
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save(pet):
    sql = 'INSERT INTO pets (owner, vet, name, age, type, issues, notes) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id'
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