"""# String indexing and slicing
word = "movie"
print(word[0])
print(word[0:3])  # prints "mov"
print(word[::3])  # prints "mi"
print(word[::-1])  # prints "eivom"

# Data Collections: Lists

cars = ["Toyota", "Honda", "Ford", "Volvo", "Ferrari"]
newlist = []
for item in cars:
    newlist.append(item)
    print(newlist)

if cars[0] == "Toyota":
    newlist.remove("Ford")
    newlist.insert(0, "Ford")
    print(newlist)

cars = ["Toyota", "Honda", "Ford", "Volvo", "Ferrari"]
print(cars[0])
print(cars[0:3])

try:
    f1 = open(filename1, "r")  # open a file for reading
    f2 = open(filename2, "w")  # open a file for writing
    for line in f1:  # read a file line by line
        f2.write(line)  # write a line to a file
except IOError:
    print("The file cannot be opened.")
else:
    f1.close()  # close the file
    f2.close()"""


######################################################################################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


# main program
TA = Person("Bob", 23)
friend = Person("Pete", 18)
professor = Person("Brian", 45)
friend.set_age(19)

neighbors = [TA, friend, professor]

for person in neighbors:
    print(person.get_name())
    print(person.get_age())
