'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
o=0
x=0
for i in range(50):
    xo= random.randrange(0, 2)
    if xo == 0:
        o+=1
        print("heads")
    else:
        x+=1
        print("tails")
print("number of tails",x)
print("number of heads",o)














