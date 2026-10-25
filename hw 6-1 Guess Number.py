class CustomError(Exception):
    pass
def test(n):
    try:
        n = int(n)
    except ValueError:
        try:
            n = float(n)
            raise CustomError("please enter an integer")
        except ValueError:
            raise CustomError("please enter a number")
    if n<0 or n>50:
            raise CustomError("number out of range")
    return n
t=0
n=input()
try:
    n=test(n)
except CustomError as e:
        print(f"Error: {e}")
else:
    while(True):
        guess=input()
        t+=1
        try:
            guess=test(guess)
        except CustomError as e:
                print(f"Error: {e}")
        else:
            if guess==n: 
                print("You got it!")
                break
            elif guess>n: print("You are too high!")
            else: print("You are too low!")
finally:
     print(f"You guessed {t} times.")