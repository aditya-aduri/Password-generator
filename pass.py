import random

upper_alphabets = "ABCDEFGHIJKLMNOPGRSTUVWXYZ"
lower_alphabets = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
syms = "(){}[],./;:-_\\?+*&#!"

upper, lower, numbers, symbols = True, True, True, True

ALL = ""

if upper:
    ALL += upper_alphabets
if lower:
    ALL += lower_alphabets
if numbers:
    ALL += nums
if symbols:
    ALL += syms

len = 15
amount = 20


for x in range(amount):
    password = "".join(random.sample(ALL,len))
    print (password)