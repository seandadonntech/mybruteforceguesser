from asyncio import current_task
from random import*
from colorama import Fore, Back, Style
from time import *

print(Fore.GREEN + 'brute force program made by seandadonntech , technio#7716, ')

user_pass = input('Enter your password:')
password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"1","2","3","4","5","6","7","8","9","0","!","@","#","%"]
guess = ""
while(guess != user_pass):
 guess = ""
 for letter in range(len(user_pass)):
  guess_letter = password[randint(0,25)]
  guess = str(guess_letter) + str(guess)
  print("Your password is", guess)

import time

# get the start time
st = time.time()

# main program
# find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i

# wait for 3 seconds
time.sleep(3)
print('Sum of first 1 million numbers is:', sum_x)

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
print("Made by seandadonntech/lilcryptotech/technio#7716")
sleep(150)
