class Pet:
    PET_TYPES = [
        "dog", 
        "cat", 
        "rodent", 
        "bird", 
        "reptile", 
        "exotic"
    ]

    all = []

    def __init__(self, name, pet_type, owner = None) -> None:
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise ValueError('Pet type not found on your system, the pet must include: {}'.format(" ,".join(Pet.PET_TYPES)))
        else:
            self._pet_type = value
    

class Owner:
    def __init__(self, name) -> None:
        self.name = name


    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self ]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("")

    def get_sorted_pets(self):
         return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda pet: pet.name)
