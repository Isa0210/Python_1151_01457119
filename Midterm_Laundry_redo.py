class WM:
    def __init__(self, id, mult):
        self.id = id
        self.mult = mult
        self.avaT = 0
    def __repr__(self):
        return f"(id={self.id}, mult={self.mult}, avaT={self.avaT})"
    def __str__(self):
        return f"({self.id}, {self.mult}, {self.avaT})"
    
N,Q=input().split()
N=int(N)
Q=int(Q)
WMlist=[WM(id,int(mult)) for id,mult in zip(range(N),input().split())]

for i in range(Q):

    arrival, duration, max_wait=(int(e) for e in input().split())
    #print(f"customer: arrival={arrival}, duration={duration}, max_wait={max_wait}")

    #print(f"WMlist={WMlist}")

    #找avaT < arrival+max_wait 的 WM 有哪些
    possibleWMlist = [wm for wm in WMlist if wm.avaT<=arrival+max_wait]
    #print(f"possibleWMlist={possibleWMlist}")

    if possibleWMlist:
        #找其中 avaT+duration*mult 最小，再看誰 id 最小
        assignWM = min(possibleWMlist, key=lambda x: (max(arrival, x.avaT)+duration*x.mult , x.id)) 

        start=max(arrival,assignWM.avaT)
        finish=start + duration*assignWM.mult
        print(f"{assignWM.id+1} {start} {finish}")
        assignWM.avaT=finish
    else:
        print("REJECTED")



        
    '''whether any WM finishes washing before customer's arrival
    for wm in WMlist:
        if wm.avaT <= arrival:
            wm.avaT = 0
    print(f"cleared WMlist={WMlist}")'''