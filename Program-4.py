def counter(array):
    count = {}
    for i in range(1,10):
        count[i] = 0
        for val in array:
            if val%i == 0:
                count[i] += 1
                
    print(count)

n = int(input("enter the number of elements "))
array = []
print()
for i in range(n):
    x = int(input())
    array.append(x)
counter(array)
