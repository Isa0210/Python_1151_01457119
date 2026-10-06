mirror = {"A": "A", "E": "3", "H": "H", "I": "I", "J": "L", "L": "J", "M": "M", "O": "O", "S": "2", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "5", "1": "1", "2": "S", "3": "E", "5": "Z", "8": "8"}
try:
    while True:
        s=input().strip()
        s.replace("0", "O")
        p=1
        m=1
        for i in range(len(s)//2+1):
            rs=s[-i-1]
            if s[i]!=rs:
                p=0;
            if s[i]!=mirror.get(rs):
                m=0;
        if p==1 and m==1:
            print(f"{s} -- is a mirrored palindrome.")
        elif m==1:
            print(f"{s} -- is a mirrored string.")
        elif p==1:
            print(f"{s} -- is a regular palindrome.")
        else:
            print(f"{s} -- is not a palindrome.")
        print("")
except EOFError:
    pass