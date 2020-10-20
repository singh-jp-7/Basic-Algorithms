lis = []
n = int(input("no of elements : "))
print("elements : ")
def bubbleSort(lis,n):
    for i in range(n):
        temp = int(input())
        lis.append(temp)
    print(lis)
    for i in range(n):
        for j in range(n-i-1):
            if (lis[j]>lis[j+1]):
                c = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = c
    print(lis)

bubbleSort(lis,n)