from random import randint
def random():
    while True:
        n=str(randint(100,999))
        if not (n[0]==n[1] or n[1]==n[2] or n[2]==n[0]):
            return n
player=input("Welcome to the COWS and BULLS GAME \U0001F917\nPlease Enter your Name:")
print("HI",player,"Let's Start the game \U0001F600")
chances=5
COWS=0
BULLS=0
num=str(random())
while chances>0:
    print("You Have",chances,"Chances Left \U0001F625")
    n=str(input("Guess The Number"))
    if(num==n):
        print(player,"WOHOOH Great! You Cracked It CONGRATS \U0001F389")
        break
    else:
        for i in range(0,3):
            if n[i]==num[i]:
                BULLS=BULLS+1
            elif n[i] in num:
                COWS=COWS+1
        print("Keep Going You Have",BULLS,"BULLS and",COWS,"COWS")
        BULLS=0
        COWS=0
        chances=chances-1
print(num," is The Correct Number")

