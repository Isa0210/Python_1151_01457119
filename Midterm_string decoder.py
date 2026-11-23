S=input().strip()
n=[]
tmpn=""
op=[]
for c in S:
    if c.isdigit():
        tmpn+=c
    else:
        if c==']':
            s=""
            while(op[-1]!='['):
                s=op[-1]+s
                op.pop()
            op.pop()#pop'['
            op.append(n[-1]*s)
            n.pop()
        else: #abcde...
            if c=='[':
                n.append(int(tmpn))
                tmpn=""
            op.append(c)
print(*op,sep="")
SforCount=""
for a in op:
    SforCount+=a
print(len(SforCount))