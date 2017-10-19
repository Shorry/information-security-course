# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import math
import random


def miller_rabin(n, k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


k = 10
while k > 0:
  tmpn = random.randrange(int(1e6), int(1e8))
  if miller_rabin(tmpn, 5):
    print('Proceed number {0}'.format(tmpn))
    k -= 1
  if not k:
    break
    
