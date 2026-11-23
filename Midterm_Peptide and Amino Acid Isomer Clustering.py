N=int(input())
L=[input()for s in range(N)]
sor=[''.join(sorted(s)) for s in L]
S=list(set(sor))
#print (sor)
#print (S)
#S=dict.fromkeys(''.join(sorted(s)) for s in L)
out=list()
for k in S:
    out.append(sorted([ L[i] for i, val in enumerate(sor) if val == k]))
out = sorted(out, key= lambda x: (0-len(x),x[0]))
for o in out:
    print(*o)
