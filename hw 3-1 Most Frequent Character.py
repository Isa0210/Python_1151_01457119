n=int(input())
for i in range(n):
    s=input()
    count={}
    for c in s:
        if c in count:
            count[c]+=1
        else:
            count[c]=1
    max_count=max(count.values())
    most_frequent_char = max(count, key=count.get)
    print(most_frequent_char)
    '''most_frequent_char=next(c for c in count if count[c]==max_count)
    print(most_frequent_char)'''#WA
    #print(type(c))
    #print(type(most_frequent_char))
    '''most_frequent_chars=[c for c in count if count[c]==max_count]
    print(''.join(sorted(most_frequent_chars)))'''#WA