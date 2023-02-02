class Pet:
    def __init__(self, owner, vet, name, age, type, issues, notes, id=None):
        self.owner = owner
        self.vet = vet
        self.name = name
        self.age = age
        self.type = type
        self.issues = issues
        self.notes = notes
        self.id = id