import numpy as np

def mc_pi(n=100):
    """use Monte Calo method to estimate pi."""
    m=0
    i=0
    while i < n:
        x,y = np.random.rand(2,1)
        if x**2 + y**2 < 1:
            m += 1
        i += 1

    pi = 4. * m / n
    res = {'total_point':n,'point_in_circle':m,'estimated_pi':pi}
    return res

if __name__ == '__main__':
    pi = mc_pi(1000000)
    print pi