import pdb
from models.owner import Owner
from models.pet import Pet
from models.vet import Vet

import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

# # functions and stuff
# owner_1 = Owner('Lewis', 'Halstead', '32 Glass Street, Glasgow, G428UF, 07823513772')
# owner_repository.save(owner_1)
# owner_2 = Owner('Jane', 'Doe', '4 Ye Ol Road, Eh1 7ER', '07893673183')
# owner_repository.save(owner_2)


vet_1 = Vet('Jeff', 'Bezos', 'Awful vet. Only here to take peoples money.', 'Snake')
# vet_repository.save(vet_1)
# vet_2 = Vet('Jesus', 'Christ', 'Literally bring animals back from the dead.', 'Dove')
# vet_repository.save(vet_2)
# # vet_repository.select_all()
# # vet_repository.delete_all()
# # vet_repository.select_all()


# pet_1 = Pet(owner_1, vet_1, 'Test Edit', 600, 'test', 'Low Focus', 'Prescribed Cocaine')
# pet_repository.save(pet_1)
# pet_2 = Pet(owner_1, vet_2, 'John', 3, 'Donkey', '3 legs', 'Prescribed extra leg')
# pet_repository.save(pet_2)
# pet_3 = Pet(owner_2, vet_1, 'Andy', 19, 'Walrus', 'Excessive Plaque', 'Prescribed floss')
# pet_repository.save(pet_3)
# pet_4 = Pet(owner_2, vet_2, 'Fred', 30, 'Dog', 'Old age', 'Take 10 years off with this one trick')
# pet_repository.save(pet_4)

# pet_repository.update(pet_1)
# pet_repository.select(pet_1)
# pdb.set_trace()