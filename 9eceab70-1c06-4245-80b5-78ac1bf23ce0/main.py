a = 'Hello! My name is Sagnik'

print(a)  #print the text a;
print(len(a)) #print the length of the text;

if "name" in a:
  print("Yes, It's There in the text")
else:
  print("No, It's not there in the text") 


for x in "name": #Loop Through a String
  print(x)

print(a.upper())
print(a.replace("S","N")) #replacing S by N

#-------------------------------------------------------
#String Concatenation

x = "Sagnik"
y = "Chanda"
z = x + " "+ y
print(z)

#Booleans

#If-Else-Statements-----
a = 100
b = 90

if a > b:
  print("A is greater than B")
else:
  print("A is smaller than B");

#------Little-Advance-If-else-Statements--------

m = "Sagnik"
n = "Chanda"

o = len(m)
p = len(n)

if o == p:
  print(m + " " + n)
else:
  print("Invalid Username")

def myFunction():
  return True

if myFunction():
  print("Yes!");
else:
  print("No!")

#------------------------------

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
car.update({"year": 2020})
print(car["year"]) #It will print 2020 after the update
car.pop("model")

print(x) #before the change

car["color"] = "white"

print(x) #after the change

for x in car:
  print(car[x])

#---------------------------------
#While-Loop-
##while i < 6:
  #print(i)
 # i += 1


j = 'Sagnik'

a = len(j)
print(a)

while a < 2:
  print(a)
  a += 3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(2, 6):
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
football = ["Baseball", "FootBall", "Cricket"]

for x in adj:
  for y in fruits:
    for z in football:
      print(x,y,z)


#Function-----

def my_function():
  print("Hello from a function")

my_function()




def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")





def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
  print("The Oldest son is : " + child1)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def my_function(student1, student2, student3):
  print("The first Student is : " + student1)
  print("The first Student is : " + student2)
  print("The first Student is : " + student3)


my_function(student1 = "Sagnik", student2 = "Rechal", student3 = "Arya")



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)




def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


x = lambda a : a + 10
print(x(5))




class myClass():
  x = "Sagnik";
  y = "Chanda";

  z = x + " " + y;

  print(z)
p1 = myClass() #Object
print(p1.x)
print(p1.z)




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Student:
  def __init__(name,roll,age):
    name.name = name
    name.roll = roll

p1 = Student("Sagnik", 38)

print(p1.name)
print(p1.roll)




class Person():
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self,fname,lname):
    super().__init__(fname,lname)
    self.graduationyear = 2024

x = Student("Sagnik" , "Chanda")
x.printname()
print(x.graduationyear)




class Student():
  def __init__(my_self,lname,fname):
    my_self.firstname = fname
    my_self.lastname = lname

  def print_name(my_self):
    print(my_self.firstname,my_self.lastname)

x = Student("Sagnik" , "Panda")
x.print_name()




class Employees():
  def __init__(my_self,name,age):     #init take the initilisation 
    my_self.name = name
    my_self.age = age

  def print_details(my_self):
    print("The name of employee is: " + my_self.name)
    print("The Age of the employee is : " + my_self.age)

x = Employees("Sagnik" ,"Mon")
x.print_details()


#---------------Procedure---------------------
#1. Make a Class
#2. Make a function which intilise a set of characters,procedures
#3. Make another function which will be shown at the time of execution with bunch of other variables; which the programmer set or maybe input.
#4. Make a variable and puth the values of the characters or procedures from the Programmer or the User and then print the function which was created to execute the results.



class Person():
  def __init__(my_person,behaviour,honesty,happiness,sadness):
    my_person.behaviour = behaviour
    my_person.honesty = honesty
    my_person.happiness = happiness
    my_person.sadness = sadness

  def human(my_person):
    print(
    "My Behaviour is: " + my_person.behaviour + "\n",
    "My Honesty is: " + my_person.honesty + "\n",
    "My Happiness is: " + my_person.happiness +  "\n",
    "My Sadness is: " + my_person.sadness +  "\n"
    )

x = Person("Good","Yes","Yes","No")
x.human()



class History():
  def __init__(kings,king_1,king_2,king_3,king_4):
    kings.king_1 = king_1
    kings.king_2 = king_2
    kings.king_3 = king_3
    kings.king_4 = king_4

  def print_kings(kings):
    print("The first Mughal Ruler was: " + kings.king_1)
    print("The second Mughal Ruler was: " + kings.king_2)
    print("The third Mughal Ruler was: " + kings.king_3)
    print("The fourth Mughal Ruler was: " + kings.king_4)

a = History("Babur", "Humayun","Akbar","Jahangir")
a.print_kings()





#A variable inside a unction is called a scope and cannot be acccessed in other places except inside the function

import datetime

x = datetime.datetime.now()
print(x)
  

