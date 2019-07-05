print('{0}, {1}, {2}'.format('apple', 'banana', 'carrot', 'pen'))
print('{}, {}, {}'.format('apple', 'banana', 'carrot'))
print('{2}, {1}, {0}'.format('apple', 'banana', 'carrot'))
print('{2}, {1}, {1}, {0}'.format('apple', 'banana', 'carrot'))
print('{2}, {1}, {0}'.format(*'abcd'))
print('{0}, {1}, {0}'.format('apple', 'banana', 'carrot'))
print('Coordinates: {latitude}, {longtitude}'.format(latitude = '37.24N', longtitude = '-115.81W'))
print('Welcome: {name}, your college is: {college}'.format(name = 'Harsh', college = 'IMS UC'))

coord = {'latitude': '37.24N', 'longtitude' : '-115.81W'}
print('Coordinates: {latitude}, {longtitude}'.format(**coord))
c = 3 - 5j
print('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}:'.format(c))
coord = (3, 5)
abc = (2, 9)
print('X: {0[0]}; Y: {0[1]}; abc : {1[0]},{1[1]}'.format(coord, abc))
coord = [(3, 9), (2, 4)]
print('First tuple: {0[0]}, {0[1]}, second tuple: {1[0]}, {1[1]}'.format(*coord))
print('{:#<30}'.format('Apple'))
print('{:*>30}'.format('Apple'))
print('{:^30}'.format('Apple'))
print('{:*^30}'.format('Apple'))
print('int:{0:d}; hex: {0:x}; oct:{0:o}; bin: {0:b}'.format(42, 55))
print('int:{1:d}; hex: {1:x}; oct:{1:o}; bin: {1:b}'.format(42, 55))
print('{:}'.format(1234567890))
points = 19.0
total = 22
print('Correct answers: {:4%}'.format(points / total)) 
