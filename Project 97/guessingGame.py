import random

def randint ():

    chances = 1
    number = random.randint (1,5)

#While loop to count the number of chances
    while chances < 5:

            guess = int(input("Enter your number: "))

    if guess == number:
        print ("Congratulations. You won!!!")
        break

    elif chances == 4:
         print("You lose. The number was", number)
    
    chances += 1 randint ()

randint ()