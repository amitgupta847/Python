import random, pylab

def clear(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))
    pylab.plot(numRemaining, label = 'Exponential Decay')

##clear(1000, 0.01, 500)
#pylab.semilogy()
##pylab.show()
        
def clearSim(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random() <= clearProb: 
                numLeft -= 1
        if t != 0 and t%100 == 0:
            numLeft += numLeft
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'r', label = 'Simulation')

clear(1000, 0.01, 500)
clearSim(1000, 0.01, 500)
pylab.show()
