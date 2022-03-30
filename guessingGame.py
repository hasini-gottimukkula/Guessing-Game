import random

guess = int(input("Enter a number from 1 to 9"))

rand = random.randint(1,9)
print(rand)



if (rand==guess):
    print("Congratulations! YOU WON!!")
    
