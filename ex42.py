## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##Dog is a class of Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a object name
        self.name = name

## Cat is a Class of Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has an object name
        self.name = name

##
class Person(object):

    def __init__(self, name):
        ## Self has a name
        self.name = name

        ##Person has a pet of some kind
        self.pet = None

## Person has a class called Employee
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## Employee has a object salary
        self.salary = salary

## Fish is a class
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = cat("Satan")

## mary is a Person
mary = Person("Mary")

## Mary has a pet called satan
mary.pet = satan

## Frank is a employee has a name Frank and salary 120000
frank = Employee("Frank", 120000)

## Frank has a pet called rover
frank.pet = rover

## Flipper is a Fish
flipper = Fish()

## Crouse is a Salmon
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()
