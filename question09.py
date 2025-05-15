"""A"""

#class Customer(Person):
#This creates a Customer class that gets all the methods from the Person class.


"""B"""
#def__init__(self,name):
#    self.name = name
#This is the constructor for the class and sets self.name as equal to the parameter name

"""C"""
#class Person:
#    def __init__(self, name):
#        self.name = name  #Name is the attribute

#    def speak(self):
#        print(f"{self.name} makes a sound.")  # This is the method

"""D"""

class Customer:
    def __init__(self, name):
        self.name = name  #Name is the attribute


class Person(Customer):
    def speak(self):
        print(f"{self.name} says hello.")
# Create an instance of Cat and call the method
my_person = Person("John")
my_person.speak()
