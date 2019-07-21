import random
import string 
def weak(size = 6, chars = string.ascii_uppercase + string.ascii_lowercase):
   return ''.join(random.choice(chars) for _ in range (size))

def medium(size = 10, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits):
   return ''.join(random.choice(chars) for _ in range (size))

def strong(size = 14, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
   return ''.join(random.choice(chars) for _ in range (size))

a = str(input("Password strength ( weak, medium or strong)?: "))
if a == 'weak':
   print (weak())
elif a == 'medium': 
   print (medium())
elif a == 'strong': 
   print (strong())
else:
   print ("Password level: weak, medium or strong.")


