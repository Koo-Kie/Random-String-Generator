import random, pyperclip
from termcolor import colored 

charset = input(colored('\nSpecify charset (separated by spaces): ', 'red', attrs=['bold']))
list = charset.split(' ')
length = int(input(colored('Length of the number: ', 'red', attrs=['bold'])))
number= ''
for i in range(length):
    number += str(random.choice(list))
clipboard = input(colored('Hide and save to clipboard? y/n: ', 'red', attrs=['bold']))
if clipboard.lower() == 'y':
    pyperclip.copy(number)
else:
    print(colored(number, 'green', attrs=['bold']))