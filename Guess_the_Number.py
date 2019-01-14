import random

x = random.randint(1, 20)
count = 0
last_guess = None
while True:
    current_guess = input("Guess a number between 1 and 20.")
    current_guess = int(current_guess)
    count += 1
    if current_guess == x:
        print(f'Good guess. {x} is correct. That took you {count} attempts!')
        break

    if last_guess is not None:
        last_proximity = abs(last_guess - x)
        new_proximity = abs(current_guess - x)
        if new_proximity < last_proximity:
            print('You are getting warmer.')
        elif new_proximity > last_proximity:
            print('Uh oh, you are getting colder.')
        else:
            print('You\'re the same distance')
    last_guess = current_guess
