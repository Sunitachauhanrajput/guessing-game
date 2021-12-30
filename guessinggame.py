i=0
while i<=5:
    n=int(input("enter guess no."))
    if n<5:
        print("no. is small from scret no.")
    elif n>5:
        print("no. is big from secret  no.")
    elif n==5:
        print("congratulation your guess is right")
        break
    i=i+1
else:
    print("your guess is not right ")
