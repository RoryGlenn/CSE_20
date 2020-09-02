# Q1
x, y = 10, 0
z = x / y

# Q2
try:
    z = x / y
except ZeroDivisionError:
    print("Division by zero is prohibited!")

# Q3
z = x + y + a

# Q4
try:
    z = x + y + a
except NameError:
    print("Some variables are not defined.")

# Q5
a = "A"
try:
    z = x + y + a
except NameError:
    print("Some variables are not defined.")

# Q6
try:
    z = x + y + a
except NameError:
    print("Some variables are not defined.")
except TypeError:
    print("Some values are of incompatible types.")

# Q7
num = int(input("Enter an integer: "))

# Q8
try:
    num = int(input("Enter an integer: "))
    print(f"You entered {num}.")
except ValueError:
    print("It is not an integer!")


# Q9
def get_data():
    try:
        n = float(input("Enter a floating point number:"))
        print(f"You entered {n}.")
    except ValueError:
        print("It is not a float number!")


# Q10
get_data()

# Q11
get_data()


# Q12
def get_data():
    done = False
    while not done:
        try:
            n = float(input("Enter a floating point number:"))
            print(f"You entered {n}")
            done = True
        except ValueError:
            print("It is not a float number!")


# Q13
# dont worry about this one

# Q14
f1 = open("mytest.txt", "w+")
f1.write("hello\n")
for i in range(5):
    f1.write(str(i) + "\n")
f1.readlines()
f1.close()

# Q15
f1 = open("mytest.txt", "r")
for line in f1:
    print(line.strip(), end=";")
f1.close()

# Q16
f1 = open("mytest.txt", "r+")
f1.readlines()

# Q17
f1.write("hello again\n")
f1.readlines()

# Q18
f1.seek(0, 0)
f1.readlines()

# Q19
f1.seek(0, 0)
for line in f1:
    print(line.strip(), end=";")
f1.close()

# Q20
f1 = open("mytest.txt", "r")
f2 = open("mycopy.txt", "w")

count = 1
for line in f1:
    f2.write(str(count) + "." + line)
    count += 1
f1.close()
f2.close()

f2 = open("mycopy.txt", "r")
for line in f2:
    print(line.strip(), end=";")

f2.close()

# Q21
f1 = open("mynew.txt", "r")

# Q22
filename1 = "mynew.txt"

try:
    f1 = open(filename1, "r")
except IOError:
    print(f"File {filename1} cannot be opened.")
else:
    print(f"File {filename1} is opened successfully.")
finally:
    f1.close()


# Q23
def open_file(filename, mode):
    try:
        f = open(filename, mode)
    except IOError:
        print(f"File {filename} cannot be opened.")
    else:
        print(f"File {filename} is opened successfully.")
        return f


f1 = open_file("mynew.txt", "r")
f1.close()

# Q24
f2 = open_file("mytest.txt", "r")
f2.close()

# Q25
with open("mytest.txt", "r") as f1:
    f1.read()

# Q26
with open("mytest.txt", "r") as f1, open("mynew.txt", "w") as f2:
    s = ""
    for line in f1:
        f2.write(line)
        s += line.strip() + ";"
print(s)


# Q27
animals = ["cat", "dog", "rat"]
with open("mynew.txt", "w+") as f1, open("mycopy.txt", "w+") as f2:
    for word in animals:
        f1.write(word + " ")
    f1.seek(0, 0)

    for line in f1:
        f2.write(line[::-1])
    f2.seek(0, 0)

    for line in f2:
        print(line, end=" ")


# Q28
def copy(filename1, filename2):
    try:
        with open(filename1, "r") as f1, open(filename2, "w+") as f2:
            # reads one file line by line
            list1 = list()
            for line in f1.readlines():
                list1.append(line)

            # copy each line to another file
            list1_str = "".join(list1)
            f2.write(list1_str)
    except IOError:
        print("File does not exist")

# Q29
copy("mynew.txt", "mycopy.txt")

with open("mynew.txt", "r") as f1, open("mycopy.txt", "r") as f2:
    count = 1
    for line in f2:
        if line == f1.readline():
            print(line.strip(), end=";")
    else:
        print(f"{count} lines are different.")

    count += 1
