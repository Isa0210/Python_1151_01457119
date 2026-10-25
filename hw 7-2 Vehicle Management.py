class Vehicle:
    
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def __repr__(self):
        return f"Vehicle: {self.brand}, Year: {self.year}"

class Car(Vehicle):

    def __init__(self, brand, year, seat):
        super().__init__(brand, year)
        self.seat = seat

    def __repr__(self):
        return f"Car: {self.brand}, Year: {self.year}, Seat: {self.seat}"
    
class Motorcycle(Vehicle):

    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = cc

    def __repr__(self):
        return f"Motorcycle: {self.brand}, Year: {self.year}, cc: {self.cc}"
    
class Bicycle(Vehicle):

    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def __repr__(self):
        return f"Bicycle: {self.brand}, Year: {self.year}, Model: {self.model}"
l=[]
while True:
    op=input().split()
    if not op: continue
    if op[0]=='stop':break

    if op[0]=='Car':
        tmp=Car(op[1],op[2],op[3])
        l.append(tmp)
    if op[0]=='Motorcycle':
        tmp=Motorcycle(op[1],op[2],op[3])
        l.append(tmp)

    if op[0]=='Bicycle':
        tmp=Bicycle(op[1],op[2],op[3])
        l.append(tmp)

    if op[0]=='print':
        for V in l:
            print(V)

'''Car 品牌 年份 座位數

Motorcycle 品牌 年份 排氣量

Bicycle 品牌 年份 型號

print:輸出所有交通工具的資訊

stop:結束程式'''