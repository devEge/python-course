class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increaseAge(self):
        self.age += 1

    def decreaseAge(self):
        if self.age > 0:
            self.age -= 1

    def __str__(self):
        return f'{self.name} is {self.age} years old!'


mehmet = Person("Mehmet", 5)
mehmet.decreaseAge()
mehmet.decreaseAge()
mehmet.decreaseAge()
mehmet.decreaseAge()
mehmet.decreaseAge()
mehmet.decreaseAge()
mehmet.decreaseAge()
mehmet.decreaseAge()
print(mehmet)