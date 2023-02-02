DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS pets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    description VARCHAR(255),
    favourite_animal VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address VARCHAR(255),
    contact VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    type VARCHAR(255),
    issues VARCHAR(255),
    notes VARCHAR(255)

);