class A:
    def first_method(self):
        print('Method of class A...')

class B(A):
    def first_method(self):
        print('Method of class B...')

class C(B):
    def first_method(self):
        print('Method of class C1...')

    def third_method(self):
        print('Method of class C2...')
        super().first_method()

if __name__ == '__main__':
    ob = C()
    ob.third_method()
    
