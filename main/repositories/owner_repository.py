from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = 'INSERT INTO owners (first_name, last_name, address, contact) VALUES (%s, %s, %s, %s) RETURNING id'
    values = [owner.first_name, owner.last_name, owner.address, owner.contact]
    results = run_sql(sql, values)
    owner.id = results[0]['id']
    return owner

def select_all():
    owners = []
    sql = 'SELECT * FROM owners'
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['address'], row['contact'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = []
    sql = 'SELECT * FROM owners WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        owner = Owner(result['first_name'], result['last_name'], result['address'], result['contact'], result['id'])
    return owner


def delete_all():
    sql = 'DELETE FROM owners'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM owners WHERE id = %s'
    values = [id]
    run_sql(sql, values)

