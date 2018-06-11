from ctypes import *
import os.path
import sys

def test(a):
    print("test before ")
    print(id(a))
    a+=2
    print("test after +,a=",a)
    print(id(a))
    return a

def printIt(t):
    for i in range(len(t)):
        print(t[i])

if __name__=="__main__":
    a=2
    print("main before invoke test")
    print(id(a))
    n=test(a)
    print("main afterf invoke test")
    print('a=',a)
    print(id(a))