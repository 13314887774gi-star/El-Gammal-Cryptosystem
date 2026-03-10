# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:07:44 2026

@author: wangyunong
"""

#public key:(p,r) = (309677,2), private key k = 254621, B = 14, j = 221003.

import string

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
#The signature consists of two numbers (c,d). We first calculate c.
j = 221003
b = 14
c = pow(r,j,p)
print("")
print("c:" + str(c))


#Next, we calculate d.
s = (b-(k*c))%(p-1)
i = p-1
x,y, u,v = 0,1, 1,0
while j != 0:
    q, z = i//j, i%j
    m, n = x-u*q, y-v*q
    i,j, x,y, u,v = j,z, u,v, m,n
    gcd = i
d1 = x*int(s/gcd)
d = d1%(p-1)
print("d:" + str(d))
print("Signature: (" + str(c) + "," + str(d) + ")")

#Confirm the validity of this signature
va = pow(a,c)
vb = pow(c,d)
v1 = (va*vb)%p
print("V1:" + str(v1))
v2 = pow(r,b,p)
print("V2:" + str(v2))
if v1==v2:
    print("This signature is valid.")
else:
    print("Invalid Signature.")