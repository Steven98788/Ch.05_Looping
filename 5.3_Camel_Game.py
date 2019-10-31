'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''
#Variables
miles = 0
energyshots = 3
shot = 4
energy = 10
cops = 0
gas = 100
gasstation=0
#Intro
print("You robbed a bank and the cops are following you.")
print("The cars gas you stole is full.")
print("You have 5 energy shots for the long road ahead.")
print("Manage your energy, gas, and distance between the cops, if any of the variable hit 0 then game over.")
print("GOOD LUCK.")
print()
start = int(input("Click 0 to start and q to quit "))  # Starts the game by conditioning 0 to make done = False
print()
if start == 0:
   done = False  # When done=False the game starts. when done=True the game will stop
import random

while not done:
   #Makes amount of miles traveled in one turn random
   moderatespeed = random.randrange(30, 40)
   fullspeed = random.randrange(55, 65)
   #Options
   print("A. Take an energy shot")
   print("B. Ahead moderate speed")
   print("C. Ahead Full speed")
   print("D. Stop for the night")
   print("E. Status check")
   print("Q. quit")
   user = input()
   if user.upper() == "A": #Take energy shot
       energy+=shot
       energyshots -= 1
       gasstation = random.randrange(1, 10000) #Oaisis
   elif user.upper() == "B": #Move moderate speed
       miles += moderatespeed
       gas -= 25
       energy -= 3
       gasstation = random.randrdrugstore= (1, 7) #Oaisis
       cops += random.randrange(30, 45)
   elif user.upper() == "C": #Move full speed
       miles += fullspeed
       gas -= 37
       energy -= 3
       gasstation = random.randrange(1, 7)
       cops += random.randrange(40, 45)
   elif user.upper() == "D": #Stop for the night
       gas = 100
       energy += 5
       cops += random.randrange(40, 45)
       gasstation = random.randrange(1, 10000)
   elif user.upper() == "E": #Status check
       print("Miles traveled:", miles)
       print("Energy:", energy)
       print("Energy shots left:",energyshots)
       print("Gas out of 100:", gas)
       print("The cops are this many miles behind you:", miles - cops)
       gasstation = random.randrange(1, 10000)
       print()
   elif user.upper() == "Q": #Stop game/quit
       done = True
   #Conditionals
   if gas <= 0:
       done = True
       print("Your car sputters and stops in the middle of the road. You try to run on foot but are eventually caught.")
       print("You Lose")
   if miles < cops:
       done = True
       print("The cops catch you in the midst of your escape. You Lose.")
   if energy <= 0:
       print("Sleep deprived you fall asleep on the road and crash into a lake. You LOSE.")
       done = True
   if energyshots <= 0: #If energy shots = 0 then this condition makes the energy you get from shots 0 so it can't be abused
       shot = 0
   if energyshots==0:
       print("OUT OF SHOTS LOOK OUT FOR DRUG STORE")
   if gasstation==6:
       energyshots+=3
       gas=100
       print("YOU STOPPED BY A ABANDONED GAS STATION AND FOUND 3 ENERGY SHOTS ALONG WITH GAS")
   if miles>= 800: #Game winner
       done=True
       print("Your a master escapist and make it to the canadian border. YOU WIN.")
   if energyshots<0: #keeps energy shot out of negative so it won't be possible to spam A and go negative in energy shots
       energyshots=0




