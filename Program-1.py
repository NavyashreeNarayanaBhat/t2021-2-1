class calcy:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
    def operations(self,op):
        if op == '+': return self.val1+self.val2
        elif op == '-': return self.val1-self.val2
        elif op == '*': return self.val1*self.val2
        elif op == '/':
            try:
                return self.val1/self.val2
            except ZeroDivisionError:
                print("Cannot divide By zero .")
                exit(0)

while(True):
    val1 = float(input("Enter your first number:"))
    val2 = float(input("Enter your second number:"))
    obj1 = calcy(val1,val2)
    print("enter operations to perform :")
    print("Addition :  +\nSubtraction : - \nMultiplication : * \nDivision : /  \nExit : Any Key \n")
    op = input()
    if op in ['+','-','*','/']:
        print(val1 , op , val2 , ' = ',obj1.operations(op))
        print('------------------------------------------')
    else : break
