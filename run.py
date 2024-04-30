class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def creation():
        return []

class Woman(Human):
    def __init__(self, name, age, has_breasts):
        super().__init__(name, age)
        self.has_breasts = has_breasts
        self.sex = "Female"

class Man(Human):
    def __init__(self, name, age, has_breasts):
        super().__init__(name, age)
        self.has_breasts = has_breasts
        self.sex = "Male"

