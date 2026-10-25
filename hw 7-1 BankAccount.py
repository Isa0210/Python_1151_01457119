'''class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, n):
        self.balance+=n
    def withdraw(self, n):
        self.balance-=n
    def s_balance(self):
        return self.balance'''
l=dict()
while(True):
    op=input().split()
    #print (op)
    if op[0]=='stop':break
    if op[0]=='create':
        l[op[1]]=int(op[2])
        #l.append({op[1]})
    if op[0]=='deposit':
        try:
            l[op[1]]+=int(op[2])
        except KeyError:
            print("Account not found")
        #{op[1]}.deposit(op[2])
    if op[0]=='withdraw':
        try:
            if int(op[2])<=l[op[1]]: l[op[1]]-=int(op[2])
            else: print("Insufficient funds")
        except KeyError:
            print("Account not found")
    if op[0]=='balance':
        try:
            print(l[op[1]])
        except KeyError:
            print("Account not found")
        #{op[1]}.withdraw(op[2])
