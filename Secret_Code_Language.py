import string
import random

random_letters1 = ''.join(random.choices(string.ascii_letters, k=3)) 
random_letters2 = ''.join(random.choices(string.ascii_letters, k=3))
#  ''.join : it joins all the random strings together
# The join in Python takes all the elements of an iterable and joins them into a single string.

# print(random_letters)
rt1 = str(random_letters1)              
rt2 = str(random_letters2)

Code_or_Decode = bool(input("Type True to Encrypt: \nType False  to Decrypt:"))

# OR
# Code_or_Decode =input("1 for Coding or 0 for Decoding : ")
# Code_or_Decode = True if Code_or_Decode =="1" else False

st = input("Enter Your Messege : ")

coding = Code_or_Decode      #if Value of Coding is True it would Encrypt and if Value is false it would Decrypt

# Coding Variable / Encrypting
if (coding):
    if (len(st) >= 3):
        st = rt1 + st[1:] + st[0] + rt2 #Adds Three Random Characters to the Front as well as to the End , Also Removes the first letter of the Message and adds it to the End
        st = str(st)
    else:
        st = st[1:] + st[0]
    print("This is Your Encryptd Messege \nCopy and pasteinto Your DeEncrypter : ", st)


# DeCoding/DeEncrypting
else:
    if (len(st) >= 3):
        st = st[3:-3]               #Removes First and Last Three Random Characters
        st =  st[-1] + st[:-1]      #Removes last Character and adds it to the front
    else:
        st =  st[0] + st[1:]
    print("This is Your Decryptd Messege : ", st)
