N,Q=input().split()
N=int(N)
Q=int(Q)
M=[int(e) for e in input().split()]
avaT=[0]*N

for i in range(Q):
    arrival, duration, max_wait=(int(e) for e in input().split())

    for j in range(N): #whether any WM finishes washing before customer's arrival
        if arrival>avaT[j]:
            avaT[j]=arrival
    #print(f"customer: {arrival, duration, max_wait}")
    #print(f"cleared avaT: {avaT}")

    minfinishtime=float('inf')
    minfinishtimeWMindex=-1
    b=1
    for j in range(N):
        if avaT[j] <= arrival+max_wait:
            b=0
            if avaT[j]+duration*M[j] < minfinishtime:
                minfinishtime=avaT[j]+ duration*M[j]
                minfinishtimeWMindex=j

    #print(f"minfinishtime= {minfinishtime} minfinishtimeWMindex= {minfinishtimeWMindex}")

    if b:
        print("REJECTED")
    else:
        print(f"{minfinishtimeWMindex+1} {avaT[minfinishtimeWMindex]} {minfinishtime}")
        avaT[minfinishtimeWMindex] = minfinishtime
    #print(f"assigned avaT: {avaT}")