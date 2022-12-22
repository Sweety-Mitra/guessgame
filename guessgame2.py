import random
def function (d,c):
    h=random.randint(1, 10)
    f=random.randint(5, 10)
    if(d==1):
        print("hint-1:if we divide the number by %d we get reminder as%d"%(h,c%h))
    elif(d==2):
        print("hint-2:the last digit of the number is%d"%(c%10))
    elif (d==3):
        print("hint-3:when we divide the number by %d we get%f"%(f,c/f))
    if(d<=4):
     
         e=int(input(" you missed your %d chance  again please enter the guess number:"%(d)))
         randomguess(e,c, d)
    else:
         print ("you lost! ")
def randomguess (num,c,d):
    
    if(num==c):
         print ("wow! you won the match")
    else:
         print ("please try again ")
         d=d+1
         function (d, c)


print("welcome to the game")
d=0
c=random.randint(1, 100)
e=int(input ("please enter the any number in the range (1, 100):"))
randomguess(e, c,d)