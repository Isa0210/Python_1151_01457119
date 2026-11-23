N,Q=input().split()
N=int(N)
Q=int(Q)
M=[int(e) for e in input().split()]
avaT=[0]*N

for i in range(Q):
    arrival, duration, max_wait=(int(e) for e in input().split())

    for j in range(N): #whether any WM finishes washing before customer's arrival
        if arrival>avaT[j]:
            avaT[j]=0
    #print(f"customer: {arrival, duration, max_wait}")
    print(f"cleared avaT: {avaT}")
    #先找在avaT[i] < arrival+max_wait的WM有哪些，再找其中avaT[i]+duration*M[i]最小的assign給客人
    CompletionT = [t[0]+(t[1]*t[2]) for t in zip(avaT,[duration]*N,M)]
    EarliestCompletionT = avaT[0]+ duration*M[0]
    NoPossibleWM = True
    possibleWMCompletionT=list()
    for j in range(N):
        if avaT[j] <= arrival+max_wait:
            NoPossibleWM = False
            possibleWMCompletionT.append(avaT[j]+duration*M[j])
            if avaT[j]+duration*M[j] < EarliestCompletionT:
                EarliestCompletionT = avaT[j]+duration*M[j]
    ECTi = possibleWMCompletionT.index(EarliestCompletionT)
    '''CompletionT = [t[0]+(t[1]*t[2]) for t in zip(avaT,[duration]*N,M)]
    EarlistCompletionT = min(CompletionT)
    EarlistCompletionT_index = -1
    if EarlistCompletionT <= arrival+max_wait:
        EarlistCompletionT_index = CompletionT.index(EarlistCompletionT)'''
    
    print(f"CompletionT= {CompletionT}")
    print(f"possibleWMCompletionT= {possibleWMCompletionT}")
    print(f"EarliestCompletionT= {EarliestCompletionT} ECTi= {ECTi}")

    if NoPossibleWM:
        print("REJECTED")
    else:
        print(f"*****ANS = {ECTi+1} {avaT[ECTi]} {EarliestCompletionT}")
        avaT[ECTi] = EarliestCompletionT
    #print(f"assigned avaT: {avaT}")



        
    
  
