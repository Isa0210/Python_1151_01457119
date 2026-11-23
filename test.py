avaT=[1,2,3]
M=[1,2,3]
duration=5
N=3
CompletionT = [t[0]+(t[1]*t[2]) for t in zip(avaT,[duration]*N,M)]
print(CompletionT)