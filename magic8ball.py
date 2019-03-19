#magic 8 ball

import random


response_list = ['It is certain', 'It is decidedly so','Without a doubt','Yes - definitely', 'As I see it, yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Don\'t count on it.','My reply is no','My sources say no.','Outlook not so good.','Very doubtful.','Yes! Wait, check that. No.']


user_name = input("Please enter your name:\n")
question = input(f'Hello {user_name}, what "yes-or-no" question would you like to ask 8-ball?\n')
answer = random.choice(response_list)
print(answer)
next_question = 'done'
# next_question = input('press any key + Enter to ask another question, or if you are finished, type "done"\n')
while True:
    next_question = input('Feel free to ask another question. Or type "done" if you are finished.\n')
    if next_question == 'done':
        print(f'Thanks for playing {user_name}. Bye')
        break
    next_answer = random.choice(response_list)
    print(next_answer)