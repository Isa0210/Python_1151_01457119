S=input().lower().split()
word_freq = dict.fromkeys(S, 0)
for word in S:
    word_freq[word] += 1
for i in word_freq:
    print(f"{i} {word_freq[i]}")