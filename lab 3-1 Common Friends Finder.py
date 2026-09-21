n, m = input().split()
set_a = set([int(x) for x in input().split()])
set_b = set([int(x) for x in input().split()])
intersection = set_a & set_b
print(len(intersection))
if intersection:
    print(*sorted(intersection))