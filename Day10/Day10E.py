def test_fun(stream,course,fee):
    print("arg1:",stream)
    print("arg2:",course)
    print("arg3:",fee*2)
    return

tup1=('Programming','python',20000)
test_fun(*tup1)

dict1={"fee":30000,"course":"ANIMATION","stream":"Multimedia"}
test_fun(**dict1)
