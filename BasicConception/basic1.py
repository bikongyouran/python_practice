# common string operation
# s = "hello" + 'world'
# print s
# print s[0]
# print s[-1], s[-2]
# print s[0:5]
# print s[:5]
# print s[-2:]
# print s[0:]
# print s[:]
# print s.split()
# s1 = 'hello world'
# print s1.split()
# print len(s1)

# common list operation
# a = [1, 2.0, 'hello', 5 + 1.0]
# print a
# print a + a
# print a[0],a[1]
# print len(a)
# a.append('world')
# print a

# common set operation
# set = {2, 3, 4, 2}
# print set  # without duplicate element
# print len(set)
# set.add(1)
# print set
# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5}
# print a & b
# print a | b
# print a - b, b - a
# print a ^ b

# common dictionary operation
# d = {'dogs':5, 'cats':4}
# print d
# print len(d)
# print d['dogs']
# d['dogs'] = 2
# print d
# d['pigs'] = 4
# print d
# print d.keys()
# print d.values()
# print d.items()

# Numpy Arrays
# from numpy import array
# a = array([1, 2, 3, 4])
# print a
# print a + a
# print a + 2
# b = a + 2
# print b

# Plot operation
# from matplotlib.pyplot import plot
# from numpy import array
# a = array([1, 2, 3, 4])
# print plot(a, a**2)

# Loop operation
# line = '1 2 3 4 5'
# fields = line.split()
# print fields
# total = 0
# for field in fields:
#     total += int(field)
# print total
# numbers = [int(field) for field in fields]
# print numbers
# print sum(numbers)
# print sum([int(field) for field in line.split()])

# File IO operation
# f = open('C:\codes\python_practice\data.txt', 'w')
# f.write('1 2 3 4\n')
# f.write('2 3 4 5\n')
# f.close()
# f = open('C:\codes\python_practice\data.txt')
# data = []
# for line in f:
#     data.append([int(field) for field in line.split()])
# f.close()
# print data
# for row in data:
#     print row
# import os
# os.remove('C:\codes\python_practice\data.txt')

# Function operation
# def poly(x, a, b, c):
#     y = a * x ** 2 + b * x + c
#     return y
#
# x = 1
# print poly(x, 1, 2, 3)
# from numpy import array
# x = array([1, 2, 3])
# print poly(x, 1, 2, 3)
#
# from numpy import arange
#
# def poly(x, a = 1, b = 2, c = 3):
#     y = a*x**2 + b*x + c
#     return y
#
# x = arange(10)
# print x
# print poly(x)
# print poly(x, b = 1)

# Class operation
# class Person(object):
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.__age = age
#     def full_name(self):
#         return self.first + ' ' + self.last
#     def getAge(self):
#         return self.__age
# person = Person('Mertle', 'Sedgewick', 52)
# print person.first
# print person.full_name()
# print person.getAge()
# print person.__age # this is private var, cannot directly get.

# web operation
# import urllib2
# import pandas
# url = 'http://ichart.finance.yahoo.com/table.csv?s=GE&d=10&e=5&f=2013&g=d&a=0&b=2&c=1962&ignore=.csv'
# ge_csv = urllib2.urlopen(url)
# data = []
# for line in ge_csv:
#     data.append(line.split(','))
# print data[:4]
# ge = pandas.read_csv(ge_csv, index_col=0, parse_dates=True)
# print ge.plot(y='Adj Close')


