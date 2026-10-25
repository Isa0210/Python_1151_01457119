n=int(input())
TotalScore=0.0
d=[]
for i in range(n):
    try:
        name, score=input().split(",")
        name = name.strip()
    except ValueError: 
        print("Error: invalid data format")
    else:
        try:
            score=int(score)
            assert(0<=score<=100)
        except ValueError:
            if not score:print("Error: invalid data format") #最後差這個檢查是否有逗號但缺後面分數 如John,
            else:print("Error: invalid score")
        except AssertionError:
            print("Error: invalid score")
        else:
            TotalScore+=score
            d.append((name,score))
            print("OK")
if len(d)>0:
    print(f"Average score: {TotalScore/len(d):.2f}")
else:
    print("No valid scores")