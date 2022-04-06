num1=int(input("Enter first number: "))
num2=int(input("Enter first number: "))
op=input("Enter operator: ")
if op=='+':
    print("sum: ",num1+num2)
elif op=='-':
    print("sub: ",num1-num2)
elif op=='*':
    print("mul: ",num1*num2)
elif op=='/':
    print("divide:", num1/num2)
else:
    print("invald operator")