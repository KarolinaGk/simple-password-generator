# This program creates randomized password which contains 10 signs 
# Including: lowercase letter, uppercase letters, digits and punctuations
# Returns a string

import string
import random

abc = string.ascii_lowercase
ABC = string.ascii_uppercase
nums = string.digits
puncs = string.punctuation

x = [*abc,*ABC,*nums,*puncs]

p = []

num = random.randint(8,12)

for i in range(num):
	p.append(random.choice(x))

password = ''.join(p)

print(password)