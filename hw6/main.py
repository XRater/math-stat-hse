from scipy.stats import norm, chi2

import math
import random
import numpy as np

import matplotlib.pyplot as plt

THETA = 0
DELTA = 2
TIMES = 1000 # number of experiments
LIMIT = 500 # max value for N
STEP = 10
GAMMA = 0.1

distribution_functions = {
    "uniform" : lambda th: random.uniform(0, th),
    "expovariate" : lambda th: random.expovariate(th),
    "normal" : lambda th, dl: random.normalvariate(th, dl),
    "xi2" : lambda n: sum(random.normalvariate(0, 1) ** 2 for _ in range(n))
}

def generate(distribution_function, n):
    return [distribution_function() for _ in range(n)]

def evaluateMiddle(l):
    return sum(l) / len(l)
    
left_fs = {
    "a" : lambda l, n: sum(map(lambda x: x * x, l)) / chi2.ppf((1 + GAMMA) / 2, n),
    "b" : lambda l, n: len(l) * (evaluateMiddle(l) ** 2) / (norm.ppf((3 + GAMMA) / 4) ** 2)
}

right_fs = {
    "a" : lambda l, n: sum(map(lambda x: x * x, l)) / chi2.ppf((1 - GAMMA) / 2, n),
    "b" : lambda l, n: len(l) * (evaluateMiddle(l) ** 2) / (norm.ppf((3 - GAMMA) / 4) ** 2)
}

def meanValue(generator):
    xs = [generator() for _ in range(TIMES)]
    return evaluateMiddle(xs)

def evaluateTestLength(distribution_function, n, left, right):
    xs = generate(distribution_function, n)
    return right(xs, n) - left(xs, n) 

def runTest(name):
    distribution_function = lambda: distribution_functions["normal"](THETA, DELTA)
    left = left_fs[name]    
    right = right_fs[name]    
        
    results = []   
    for k in range(10, LIMIT, STEP):
        results.append(meanValue(lambda : evaluateTestLength(distribution_function, k, left, right)))
                
    plt.clf()
    plt.plot([i for i in range(10, LIMIT, STEP)], results)
    plt.savefig(name)        
    
if __name__ == "__main__":
    runTest("a")    
    runTest("b")    

