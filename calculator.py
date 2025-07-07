""""Simple Calculator"""
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
print("select an Operator")
choice= input("Enter Choice (1/2/3/4)")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

a=float(input("Enter Your first value "))
b= float(input("Enter the second value "))

# now use condition
if choice == "1":
    print("Your Total sum is:",add(a,b))
elif choice=="2":
    print("Your Output Value is: ",subtract(a,b))
elif choice=="3":
    print("Your Result is:",division(a,b))
elif choice =="4":
    print("Your Taotal is : ",multiply(a,b))
else:
    print("please input vailed value ")



