def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

while True:
        N = int(input())
        if N == 0:
            break
        G=0
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                G += GCD(i, j)
        print(G)
