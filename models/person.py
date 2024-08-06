class Person:
    def set_person(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
