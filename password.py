import random
import string

print("This is to generate password")

length = int(input("Enter the length of the password:"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols = string.punctuation

alll = lower + upper + num + symbols 

temp = random.sample(alll,length)

password = "".join(temp)

print("This is your password:",password)