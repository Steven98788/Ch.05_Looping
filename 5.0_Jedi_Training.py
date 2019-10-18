  #Sign your name:________________

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter 3 numbers: "))
    total = total + x
print("The total is:",total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
    print(i)





'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=11
while i >0:
    i-=1
    print(i)
print("Blast off!")






# done = False
# while not done:





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
i= random.randrange(1,11)
print(i)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total=0
for i in range(7):
   num=int(input("Please give me a number!"))
   total+=num
print("Your total comes to:",total)
