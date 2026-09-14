n=int(input())
c=0
if not 1<=n<=100:
    print("Invalid input")
for i in range(n):
    for j in range(i+1):
        c+=1
        print(c,end=" ")
    print("")