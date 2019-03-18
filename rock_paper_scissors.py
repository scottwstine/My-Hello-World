import random

rps = ['rock', 'paper', 'scissors'] # order matters - see below

answer = 'yes'
if answer != 'no':
    while True:
        user_choice = input('rock, paper, or scissors? ').lower()
        if user_choice in rps:
            break

    print('user choice: ' + user_choice)

    comp_choice = random.choice(rps)
    print('computer choice: ' + comp_choice)

    user_choice = rps.index(user_choice)
    comp_choice = rps.index(comp_choice)

    #  0       1       2
    # rock, paper, scissors

    if user_choice == comp_choice:
        answer = input('It\'s a tie. Would you like to try again? y/n\n')
    elif (user_choice + 1)%3 == comp_choice:
        answer = input('Computer wins. Would you like to play again? y/n\n')
    else:
        answer = input('You win! Would you like to play again? y/n\n')
print('Thanks for playing.')
