import pdb
from models.owner import Owner
from models.pet import Pet
from models.vet import Vet

import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

# functions and stuff
owner_1 = Owner('Lewis', 'Halstead', '32 Glass Street, Glasgow, G428UF', '07823513772')
owner_repository.save(owner_1)
owner_repository.select_all()

vet_1 = Vet('Jeff', 'Bezos', 'Awful vet. Only here to take peoples money.', 'Snake')
vet_repository.save(vet_1)
vet_repository.select_all()

pdb.set_trace()