"""# Q1
class Animal:
    def __init__(self, species):
        self.species = species

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species


turtle1 = Animal("turtle")
turtle2 = Animal("turtle")
unknown = Animal("")
hare = Animal("hare")
animals = [turtle1, turtle2, unknown, hare]

# for animal in animals:
#     print(animal.get_species(), end="; ")

# Q2
unknown.set_species("beaver")


# for animal in animals:
#     print(animal.get_species(), end="; ")


# Q3
class Pet(Animal):
    def __init__(self, name, age, species):
        super().__init__(species)
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return (self.name)

    def get_age(self):
        return (self.age)

    def isYounger(self, pet):
        if self.age < pet.get_age():
            return True
        else:
            return False


cat = Pet("Fluffy", 3, "cat")
dog = Pet("Tobby", 5, "dog")
# if cat.isYounger(dog):
#     print(cat.get_name() + " is younger than " + dog.get_name())
# else:
#     print(f"{dog.get_name()} is younger than {cat.get_name()}")


# Q4
class ZooAnimal(Pet):
    aged = 7  # global variable of the class


mountainlion = ZooAnimal("Rocky", 5, "leopard")
snowleopard = ZooAnimal("Snowy", 3, "leopard")
tiger = ZooAnimal("Sunny", 8, "tiger")
cats = [mountainlion, snowleopard, tiger]
# for animal in cats:
#     if animal.get_age() < ZooAnimal.aged:  # access a global variable of the class
#
#         print(animal.get_name() + " is a young cat.")
#     else:
#
#         print(animal.get_name() + " is an old cat.")

# Q5
tiger.set_name("Honey")
# print(tiger.get_name())


# Q6
class ZooAnimal(Pet):
    def aged(self):
        species = self.get_species()
        if species == "tiger":
            aged = 7.0
        elif species == "lion":
            aged = 6.0
        else:
            aged = 8.0
        return aged


class Tiger(ZooAnimal):
    def aged(self):
        return 7.5


class Lion(ZooAnimal):
    def aged(self):
        return 6.5


leopard = ZooAnimal("Snowy", 3.0, "leopard")

tiger = Tiger("Sunny", 8.0, "tiger")

lion = Lion("Rocky", 4.0, "lion")
cats = [lion, leopard, tiger]
for animal in cats:
    if animal.get_age() < animal.aged():
        print(f"{animal.get_name()} is a young cat because it is less than {animal.aged()} years old.")
else:
    print(f"{animal.get_name()} is an old cat because it is more than {animal.aged()} years old.")

"""


# Q7 #########################################################################


class Tree:

    # data attribute
    def __init__(self, age, species):
        self.age = age
        self.species = species

    # instance methods
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_species(self):
        return self.species

    def set_species(self, species):
        self.species = species

    def get_info(self):
        return ( ("age", str(self.age)), ("species", self.species) )


class NurseryTree(Tree):

    # inherited data attributes and methods
    def __init__(self, age, species, cultivar, price):
        super().__init__(age, species)

        # new data attributes
        self.cultivar = cultivar
        self.price = price

    # new instance methods
    def get_cultivar(self):
        return self.cultivar

    def set_cultivar(self, cultivar):
        self.cultivar = cultivar

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_info(self):
        return ( ("age", str(self.age)), ("species", self.species), ("cultivar", self.cultivar), ("price", str(self.price)) )


class ProtectedTree(Tree):

    # inherited data attributes and methods
    def __init__(self, age, species, location):
        super().__init__(age, species)

        # new data attribute
        self.location = location

    # new instance methods

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_info(self):
        return (("age", str(self.age)), ("species", self.species), ("location", self.location))

def print_info(info):
    for i in info:
        if "age" == i[0]:
            print(f"This tree is {i[1]} years old.")
        elif "species" == i[0]:
            print(f"This tree belongs to {i[1]} species.")
        elif "location" == i[0]:
            print(f"This tree is located in {i[1]}.")
        elif "cultivar" == i[0]:
            print(f"This is {i[1]}.")
        elif "price" == i[0]:
            print(f"This tree costs {i[1]} dollars.")
    print()


# main program
pine = Tree(80, "Pinus radiata")
sequoia = ProtectedTree(1650, "Sequoiadendron giganteum", "Kings Canyon National Park")
apple = NurseryTree(4, "Malus domestica", "Golden Delicious", 99.95)

for tree in [pine, sequoia, apple]:
    print_info(tree.get_info())
