# import numpy
# import matplotlib
# from matplotlib import pyplot as plt
#
# # x = [1, 2, 3]
# pi = 3.14
# # both linespace and arange are for creating lists.
# x = numpy.linspace(0, 2*pi, 50)
# # t = numpy.arange(0, 2*pi, 0.1)
# # print x
# # print t
# plt.plot(x, numpy.sin(x), 'r+',x, numpy.sin(2*x),'g-',label='test demo', linewidth=5)
# # plt.plot(t, numpy.sin(t))
# plt.show()

# # object-oriented plot
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#
# fig    = Figure()
# canvas = FigureCanvas(fig)
#
# # first axes
# ax1    = fig.add_axes([0.1, 0.1, 0.2, 0.2])
# line,  = ax1.plot([0,1], [0,1])
# ax1.set_title("ax1")
#
# # second axes
# ax2    = fig.add_axes([0.4, 0.3, 0.4, 0.5])
# sca    = ax2.scatter([1,3,5],[2,1,2])
# ax2.set_title("ax2")
#
# canvas.print_figure('demo.jpg')

# import numpy
# list = [1,2,3,4]
# a = numpy.array(list)
# print a
# print type(a)
# print a[:-1]
# a.fill(5.9)
# print a #[5 5 5 5]

# from numpy import *
# a = array([[ 0, 1, 2, 3],
#            [10,11,12,13]])
# print a.ndim
# print a[1,3] #13
# print a[1] #[10,11,12,13]
# print a[0, 1:3] #[1 2]
# a = array([[ 0, 1, 2, 3, 4, 5],
#            [10,11,12,13,14,15],
#            [20,21,22,23,24,25],
#            [30,31,32,33,34,35],
#            [40,41,42,43,44,45],
#            [50,51,52,53,54,55]])
# print a[4:, 4:]
# print a[:, 2]
# print a[2::2, ::2] #[lower:upper:step]

# from numpy import *
# a = array([ 0, 1, 2, 3])
# print average(a)
# print a.std()
# print a.var()
# b = range(1, 4, 1)
# c = arange(1, 4, 1)
# print b
# print c

import numpy as np
a = np.array([[1,2,4],
              [2,5,3],
              [7,8,9]])
A = np.mat(a)
print A
print a




