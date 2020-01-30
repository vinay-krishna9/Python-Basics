# basic 1
class Dog():
    # CLASS OBJECT ATTRIBUTE
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    # OPERATIONS/Actions -----------> Methods
    def bark(self):
        print (f'WOOF! My name is {self.name}')


my_dog = Dog(breed='pug', name="sammy", spots=False)

print (my_dog.breed, my_dog.name, my_dog.bark(), my_dog.species)
