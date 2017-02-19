def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print result

import pylab

##pylab.plot([1,2,3,4], [1,2,3,4])
##pylab.plot([1,4,2,3], [5,6,7,8])
##pylab.show()

pylab.figure(1)
pylab.plot([1,2,3,4], [1,2,3,4])

pylab.figure(2)
pylab.plot([1,4,2,3], [5,6,7,8])

pylab.savefig('firstSaved')

pylab.figure(1)
pylab.plot([5,6,7,10])
pylab.savefig('secondSaved')

pylab.show()
