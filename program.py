
def fun(num1):
    if num1>5:
        return 0
    return num1+ fun(num1+1)
    
num1=int(input())
print(fun(1))