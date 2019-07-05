#filter() filters an iterable by removing items that don't match a prediction
#predicate is a function that returns a Boolean

def find_odd(x):
    if x%2==1:
        return True
    else:
        return False
nums=[11,22,33,44,55]
result=list(filter(find_odd,nums))
print(nums)
print("Odd:",result)
print('#'*20)
num=[11,22,33,44,55]
result=list(filter(lambda x:x%2 == 1,num))
print("Odd:",result)
print('#'*20)
result=list(filter(lambda x:x%2 == 1,num))
print("Even:",result)
