import numpy as np

def bubble_sort(source):
    length = len(source)
    i = 0
    j = 0
    while j < length:
        while i < length - j - 1:
            if source[i] > source[i + 1]:
                temp = source[i]
                source[i] = source[i + 1]
                source[i+1] = temp
            i += 1
        j += 1
        i = 0

if __name__ == '__main__':
    source = np.random.random_integers(1, 20, 10)
    print "source is ", source
    bubble_sort(source)
    print 'target is ', source