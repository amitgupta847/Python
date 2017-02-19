import random

def integrate(a, b, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        pinSum += f(random.uniform(a, b))
    average = pinSum/numPins
    return average*(b - a)

def one(x):
    return 1.0

print integrate(0, 8, one, 100000)

import math
print integrate(0, 8, math.sin, 1000000)

def doubleIntegrate(a, b, c, d, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        pinSum += f(x, y)
    average = pinSum/numPins
    return average*(b - a)*(d - c)

def f(x, y):
    return 4 - x**2 - y**2

print doubleIntegrate(0, 1.25, 0, 1.25, f, 100000)
