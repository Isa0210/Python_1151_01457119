n=int(input())
b = [int(x) for x in input().split()]
while b[0]!=0:
    a = [x for x in range(1, n+1)]
    c = []
    #print(a)
    #print(b)

    while len(b)>0:
        if len(c)>0 and b[0] == c[-1]:#往c找目標
            c.pop()
            b.pop(0)
        elif len(a) == 0: #a是否為空/是否c找不到目標a也空了
            print("NO")
            break
        elif b[0] == a[0]:#往a找目標
            a.pop(0)
            b.pop(0)
        else:#a的頭不是目標就往c放
            c.append(a.pop(0))

    if len(b) == 0:
        print("YES")

    b = [int(x) for x in input().split()]