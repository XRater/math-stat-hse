import numpy as np
import matplotlib.pyplot as plt

a = 2
c = 1 / (2 * np.exp(-a) + 2 * a) #normalize
N = 2000 # amount of expirements

def random1():
    y = np.random.uniform(0, 1)
    if y < c * np.exp(-a):
        return np.log(y / c)
    if y > 1 - c * np.exp(-a):
        return -np.log((1 - y) / c)
    return y / c - np.exp(-a) - a


def random2():
    y = np.random.uniform(0, 1)
    if y < c * np.exp(-a):
        return -np.random.exponential(1) - a      
    if y > 1 - c * np.exp(-a):
        return np.random.exponential(1) + a    
    return np.random.uniform(-a, a)      


if __name__ == "__main__":
    results1 = [random1() for _ in range(N)]
    results2 = [random2() for _ in range(N)]
    results1.sort()
    results2.sort()
    plt.plot([i for i in range(N)], results1)
    plt.plot([i for i in range(N)], results2)
    plt.savefig('results.png')
