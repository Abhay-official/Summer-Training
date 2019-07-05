class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, ob):
        return Complex(self.real + ob.real, self.img + ob.img)

    def __sub__(self, ob):
        return Complex(self.real - ob.real, self.img - ob.img)

    def __str__(self):
        return str(self.real) + '+' + str(self.img) + 'j'

z1 = Complex(5, 7)
z2 = Complex(3, 8)
result = z1 + z2
print(result.real)
print(result.img)
result = z1 - z2
print(result.real)
print(result.img)

print(result)
