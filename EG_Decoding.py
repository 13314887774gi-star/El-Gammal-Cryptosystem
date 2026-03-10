# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:02:47 2026

@author: wangyunong
"""

#public key:(p,r) = (309677,2), private key k = 254621
#Decrypt and obtain the plaintext message for:
#[167525, ['231639', '001364', '195282', '231153', '205170', '005770', '060473', '011372', '257977',
# '179830', '089069', '041799', '218950']]

import string

#Assigning the letters A- Z to digits 00- 25 respectively
nonval = dict()
for index, letter in enumerate(string.ascii_uppercase):
    nonval[index] = letter
    nonval[26] = " "
    
#Keys

print("Private key:")
k = 254621
print("k:" + str(k))
k = int(k)
print("Public key:")
p = 309677
print("p:" + str(p))
p = int(p)
r = 2
print("r:" + str(r))
r = int(r)
a = pow(r,k,p)
print("a:" + str(a))
#Decrypting to obtain the plaintext message
#(c1,c2)
c1 = 167525
#list is exceeding limit of page
c2_list = ['231639', '001364', '195282', '231153', '205170', '005770', '060473', '011372', '257977',
 '179830', '089069', '041799', '218950']

#For each c2 in pairs (c1, c2) in the ciphertext:
s = p- 1- k
c = pow(c1,s,p)
count = 0
print("\n")
print("DECRYPTED MESSAGE: ",end="")
for i in c2_list:
    i = int(i)
    n = (i*c)%p
#printing the sentence
    count = count +1
    n1=n%100
    n2 = int((n-n1)/100)
    n3 = n2%100
    n4 = int((n2-n3)/100)
    print(nonval[n4],end="")
    if count < 13:
        print(nonval[n3],end="")
        print(nonval[n1],end="")


OUTPUT:
CIPHER TEXT:(149,107)(149,07)(149,114)(149,00)(149,02)(149,06)(149,07)(149,112)
        
        
        
        
        
        
        
        
        
        
        









