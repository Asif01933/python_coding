from operator import truediv


def func(x):
    if x%2==0:
        return True
    return False

for i in range(0,10):
    if func(i)==True:
        print(i," is even")
    else:
        print(i," is odd")