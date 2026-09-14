n=int(input())
if n<=1:
    print("Invalid input")
else:
    for i in range(n):
        for j in range(n+i):
            if j==n-1-i or j==n+i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    for i in range(n-1):
        for j in range(2*n-2-i):
            if j==i+1 or j==2*n-3-i:
                print("*",end="")
            else:
                print(" ",end="")
        print("")