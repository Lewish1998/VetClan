from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = 'INSERT INTO vets (first_name, last_name, description, fav_animal) VALUES (%s, %s, %s, %s) RETURNING id'
    values = [vet.first_name, vet.last_name, vet.description, vet.fav_animal]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet

def select_all():
    vets = []
    sql = 'SELECT * FROM vets'
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['description'], row['fav_animal'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = []
    sql = 'SELECT * FROM vets WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        vet = Vet(result['first_name'], result['last_name'], result['description'], result['fav_animal'], result['id'])
    return vet

def delete_all():
    sql = 'DELETE FROM vets'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM vets WHERE id = %s'
    values = [id]
    run_sql(sql, values)

