class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def __str__(self):
        return self.color + ', ' + str(self.legs)

if __name__ == "__main__":
    pet1 = Cat('Ginger', 4)
    print(pet1.legs)
    print(pet1.color)
    print(pet1)

    pet2 = Cat('Brown', 3)
    print(pet2.legs)
    print(pet2.color)
    print(pet2)
