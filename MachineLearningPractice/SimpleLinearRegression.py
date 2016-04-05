import numpy as np

def fitSLR(x, y):
    n = len(x)
    dinominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += (x[i] - np.mean(x))*(y[i] - np.mean(y))
        dinominator += (x[i] - np.mean(x))**2

    print "numerator:", numerator
    print "dinominator:", dinominator
    b1 = numerator/float(dinominator)
    b0 = np.mean(y)/float(np.mean(x))

    return b0, b1

def predict(x, b0, b1):
    return b0 + x*b1

x = [1, 3, 2, 1, 3]
y = [14, 24, 18, 17, 27]

b0, b1 = fitSLR(x, y)

print "intercept:", b0, ' slope:', b1

test_x = 6
test_y = predict(test_x, b0, b1)

print 'test_y:', test_y
