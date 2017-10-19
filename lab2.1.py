# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import math
from random import randint


def Leman(p, m):
    tmp = True
    for i in range(m):
        a = randint(1, p)
        # // in p3.6
        k = ((a % p) ** ((p - 1) // 2)) % p
        
        if k != 1 and k != p - 1:
            return False
        if k == p - 1:
            tmp = False
    if tmp:
        return False
    else:
        return True


result = []

k = 10

while k > 0:
  tmpn = randint(int(1e6), int(1e8))
  if tmpn % 2 == 0 or tmpn % 3 == 0 or tmpn % 5 == 0 or tmpn % 7 == 0:
    continue
  
  if Leman(tmpn, 10):
    print('Proceed number {0}'.format(tmpn))
    k -= 1
  if not k:
    break
