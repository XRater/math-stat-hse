import math
import random

import matplotlib.pyplot as plt

THETA = 100
TIMES = 1000 # number of experiments
MOMENT_TIMES = 1000 # number of tries to evaluate moment
LIMIT = 100 # max value for k
STEP = 10

distribution_functions = {
    "uniform" : lambda th: random.uniform(0, th),
    "expovariate" : lambda th: random.expovariate(th)
}

estime_functions = {
    "uniform" : lambda x, k: ((k + 1) * x) ** (1.0 / k),
    "expovariate" : lambda x, k: (math.factorial(k) / x) ** (1.0 / k)
}

def evaluateMiddleMoment(distribution_function, k, n):
    return sum([distribution_function() ** k for _ in range(n)]) / n

def evaluateDeviation(test_function, target, times):
    return (sum([(test_function() - target) ** 2 for _ in range(times)]) / times) ** 0.5

def runTest(name):
    distribution_function = lambda: distribution_functions[name](THETA)
    estime_function = estime_functions[name]
       
    
    results = []   
    for k in range(1, LIMIT, STEP):
        test_function = lambda: estime_function(evaluateMiddleMoment(distribution_function, k, MOMENT_TIMES), k)
        deviation = evaluateDeviation(test_function, THETA, TIMES)
        results.append(deviation)
        
    plt.clf()
    plt.plot([i for i in range(1, LIMIT, STEP)], results)
    plt.savefig(name)        
    
if __name__ == "__main__":
    runTest("uniform")
    runTest("expovariate")

