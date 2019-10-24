'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
miles=0
energyshots=5
energy=10
cops=0
gas=100
print("You robbed a bank and the cops are following you.")
print("The cars gas you stole is full.")
print("YOu have 5 energy shots for the long road ahead.")
print("Manage your energy and gas. Good luck")
print()
start=int(input("Click 0 to start"))
print()
if start==0:
    done=False #When done=False the game starts when done=True the game will stop

while not done:
    print("A. Take an energy shot")
    print("B. Ahead moderate speed")
    print("C. Ahead Full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. quit")
    user=input()
    if user.upper()=="A":
        energy+=2
        energyshots-=1
    elif user.upper()=="B":
        miles+=40
        gas-=25
        energy-=2
    elif user.upper()=="C":
        miles+=70
        gas-=50
        energy-=4
    elif user.upper()=="D":
        gas=100
        energy+=5
    elif user.upper()=="E":
        print("Miles traveled",miles)
        print("Energy",energy)
        print("Gas",gas)
        print("The cops are this many miles behind you",miles-cops)
    elif user.upper()=="Q":
        done=True
if done==True:
    print("You lose better luck next time :(")




















