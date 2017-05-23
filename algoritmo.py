import sys
import random
from random import shuffle

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1
    lista.append(random.randint(0, 100000000))
    shuffle(lista)
    shortBubbleSort(alist)

lista  = []
lista.append(random.randint(0, 100000000))
shuffle(lista)
shortBubbleSort(lista)




