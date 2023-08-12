# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# ?? - class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # ?? - self.name has-a name
        self.name = name


# ??- Class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # ?? - self.name has-a name
        self.name = name


# ?? - Person is-a object
class Person(object):

    def __init__(self, name):
        # ?? - self name has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# ?? - Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # ?? - Employee has-a name - run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        # ?? - Employee has-a salary
        self.salary = salary


# ?? - Fish is-a object
class Fish(object):
    pass


# ?? - Salmon is-a fish
class Salmon(Fish):
    pass


# ?? - Halibut is-a fish
class Halibut(Fish):
    pass


# ?? - rover is-a Dog
rover = Dog("Rover")

# ?? - satan is-a Cat
satan = Cat("Satan")

# ?? - Mary is-a Person
mary = Person("Mary")

# ?? - mary has-a pet
mary.pet = satan

# ? - Frank is-a Employee
frank = Employee("Frank", 120000)

# ?? - frank has-a pet
frank.pet = rover

# ?? - flipper is-a fish
flipper = Fish()

# ?? - crouse is-a salmon
crouse = Salmon()

# ?? - harry is-a halibut
harry = Halibut()
