def sum_num(x):
    res = 0
    for i in range(x + 1):
        res += i
        print('i = ', i, 'res = ',res)
        yield res

ob = sum_num(10)
for i in range(11):
    print(next(ob))
