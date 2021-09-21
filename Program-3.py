def display(a):
    if a%2!=0:
        for  i in range(1,a+1):
            print(2*i-1,end=" ")
    else:
        for i in range(1,a):
            print(2*i-1,end=" ")
        

a=int(input("How many digits you want to display?\n"))
display(a)
