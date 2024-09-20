def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return  a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "cannot divide by 0"

print("Select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice =  input("enter your choice 1/2/3/4: ")

num1 = float(input("enter first no.: "))
num2 = float(input("enter second no.: "))


if choice == "1":
    print(add(num1,num2))

elif choice == "2":
    print(sub(num1,num2))

elif choice == "3":
    print(multiply(num1,num2))

elif choice == "4":
    print(divide(num1,num2))

else:
    print("invalid input")
