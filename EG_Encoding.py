# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:58:26 2026

@author: wangyunong
"""
#message:DORAEMON, public key: (211, 2, 164), private key k = 19
#random integer chosen for encryption is j = 11
import string
message = "DORAEMON"
#Assigning the digits 00- 25 to letters A- Z respectively
values = dict()
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index
    values[" "] = 26
k = 19
p = 211
r = 2
a = pow(r,k,p)
j = 11
c1 = pow(r,j,p)
#Finding the ciphertext
print("CIPHER TEXT:",end="")
y = pow(a,j,p)
for i in range(len(message)):
    char = message[i]
    B = values[char]
    c2 = (B*y)%p
    if c2<10:
        print("(" + str(c1) + "," + "{:02d}".format(c2) + ")",end="")
    else:

        print("(" + str(c1) + "," + str(c2) + ")",end="")

OUTPUT:
DECRYPTED MESSAGE: TWO DRIVEN JOCKS HELP FAX MY BIG QUIZ
