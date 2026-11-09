N,K= input().split()
N= int(N)
K= int(K)
A= [int(x) for x in input().split()]
window =list()
maxlen=0
sum=0
for i in range(0,N):
    window.append(A[i])
    sum+=A[i]
    while sum>K:
        sum-=window[0]
        window.pop(0)
    if len(window)>maxlen:
        maxlen=len(window)
print(maxlen)

