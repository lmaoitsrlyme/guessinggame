import random

randomnum, guess = random.randint(1, 10), 0

while randomnum != guess:
    
    guess = int(input("guess a number between 1 and 10 until you get it right : "))

print('correct!')
