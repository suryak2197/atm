import random
RandNo = random.randint(0,5)
guess = input("enter the number")
while int(guess) != RandNo:
    print ("Please make a guess for the random number.")
    guess = input("enter the number")
print('Ding! Ding! Ding! The random number was ', RandNo)
             