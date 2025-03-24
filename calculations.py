# basic calculations

def add (x,y):
    result = x+y
    return result

def subtract (x,y):
    result = x-y
    return result

def multiply (x,y):
    result = x*y
    return result

def divide (x,y):
    if y == 0:
        return -1
    result = x/y
    return result

def percentage (x):
    result = x*100
    return result

def square (x):
    result = x*x
    return result

def changeSign (x):
    result = x*(-1)
    return result
