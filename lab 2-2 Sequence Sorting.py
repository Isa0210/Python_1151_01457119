n=int(input())
a=[int(x) for x in input().split()]
b = a.copy()
if not 1<=n<=100:
    print("Invalid input")
for i in range(n-1):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
for i in range(n):
    print(b[i],end=" ")
print("")
for i in range(n):
    print(a[i],end=" ")
