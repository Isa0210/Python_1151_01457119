def search(id):
    if id in dict:
            print(f"{dict[id][0]} {dict[id][1]}")
    else:
        print("Not found")
n=int(input())
dict={}
for i in range(n):
    id, name, score = input().split()
    dict[id] = name, int(score)
#print(dict)
I=int(input())
for i in range(I):
    sid = input().strip()#之前錯在沒加strip
    search(sid)
