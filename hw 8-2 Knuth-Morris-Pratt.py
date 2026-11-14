def build_lps(p):
    lps = [0] * len(p)
    length = 0 # current border length
    i = 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1] # fall back
        else:
            lps[i] = 0
            i += 1
    return lps
def kmp_search(text, pattern):
    lps = build_lps(pattern)
    m = len(pattern)
    found = []
    j = 0 # chars matched so far
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1] # i never moves back
        if ch == pattern[j]:
            j += 1
        if j == m:
            found.append(i - m + 1)
            j = lps[j - 1] # allow overlaps
    return found

text=input()
pattern=input()
print(*kmp_search(text, pattern))
