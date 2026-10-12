ans=0
def cola(n):
    global ans
    if n <=1 :#跟朋友借會還不了
        return 0
    elif n < 3: #剩兩空瓶，跟朋友借可以還
        ans+= 1
        return 0
    else: #三瓶以上空瓶
        ans+=n//3
        return cola( n%3+n//3 ) #回傳空瓶數
try:
    while True:
        n=int(input())
        ans=n
        cola(n)
        print(ans)
except EOFError:
    pass