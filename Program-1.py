def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

choice="yes"

while choice=="yes":
    num1=int(input("Enter your first number:"))
    num2=int(input("Enter your second number:"))
    operation=input("Type the operation you want to perform:\nAddition\nSubtraction\nMultiplication\nDivision\n")
    operation=operation.lower()
    if operation=="addition":
        print("\nOutput is:",add(num1,num2))
    elif operation=="subtraction":
        print("\nOutput is:",sub(num1,num2))
    elif operation=="multiplication":
        print("\nOutput is:",mul(num1,num2))
    elif operation=="division":
        print("\nOutput is:",div(num1,num2))
    else:
        print("\nType the operation correctly")
    print("Want to perform some operations? (yes/no)\n")
    ch=input()
    choice=ch.lower()
print("Thank you")
        
