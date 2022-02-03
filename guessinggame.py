import random
n=random.randint(0,9)
i=1
while i<=5:
    guess=int(input("enter guess no."))
    if guess<n:
        print("no. is small from scret no.")
    elif guess>n:
        print("no. is big from secret  no.")
    elif guess==n:
        print("congratulation your guess is right")
        break
    i=i+1
else:
    print("your guess is not right ")

