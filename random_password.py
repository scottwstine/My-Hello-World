import random
import string


n_lowercase = int(input('how many lowercase characters? '))
n_uppercase = int(input('how many uppercase characters? '))
n_numbers = int(input('how many numerical characters? '))
n_special = int(input('how many special characters? '))


password = []
for i in range(n_lowercase):
    password.append(random.choice(string.ascii_lowercase))

for i in range(n_uppercase):
    password.append(random.choice(string.ascii_uppercase))

for i in range(n_numbers):
    password.append(random.choice(string.digits))

for i in range(n_special):
    password.append(random.choice('~`!@#$%^&*()-_=+[{]}\\|;:\'"<,>.?/'))

# print(password)
random.shuffle(password)
password = ''.join(password)
print('-'*10 + 'YOUR PASSWORD IS' + '-'*10)
print(password)













