from matplotlib import pyplot as plt
import numpy as np

# plt.plot([1,2,3,4],[3,4,6,9],'ro')
# plt.ylabel('test')
# plt.axis([0,5,0,10])
# plt.show()
#####################################
# t = np.arange(0,5,0.2)
# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
# plt.show()
#####################################
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure(1)
# plt.subplot(322)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
#####################################
# # create some data to use for the plot
# dt = 0.001
# t = np.arange(0.0, 10.0, dt)
# r = np.exp(-t[:1000]/0.05)               # impulse response
# x = np.random.randn(len(t))
# s = np.convolve(x, r)[:len(x)]*dt  # colored noise
#
# # the main axes is subplot(111) by default
# plt.plot(t, s)
# plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
# plt.xlabel('time (s)')
# plt.ylabel('current (nA)')
# plt.title('Gaussian colored noise')
#
# # this is an inset axes over the main axes
# a = plt.axes([.65, .6, .2, .2], axisbg='y')
# n, bins, patches = plt.hist(s, 400, normed=1)
# plt.title('Probability')
# plt.xticks([])
# plt.yticks([])
#
# # this is another inset axes over the main axes
# a = plt.axes([0.2, 0.6, .2, .2], axisbg='y')
# plt.plot(t[:len(r)], r)
# plt.title('Impulse response')
# plt.xlim(0, 0.2)
# plt.xticks([])
# plt.yticks([])
#
# plt.show()
#####################################
# Simple data to display in various forms
# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)
#
# plt.close('all')

# Just a figure and one subplot
# f, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')
#
# # Two subplots, the axes array is 1-d
# f, axarr = plt.subplots(2, sharex=False)
# axarr[0].plot(x, y)
# axarr[0].set_title('Sharing X axis')
# axarr[1].scatter(x, y)
#
# # Two subplots, unpack the axes array immediately
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)
#
# # Three subplots sharing both x/y axes
# f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing both axes')
# ax2.scatter(x, y)
# ax3.scatter(x, 2 * y ** 2 - 1, color='r')
# # Fine-tune figure; make subplots close to each other and hide x ticks for
# # all but bottom plot.
# f.subplots_adjust(hspace=0)
# plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

# row and column sharing
# f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
# ax1.plot(x, y)
# ax1.set_title('Sharing x per column, y per row')
# ax2.scatter(x, y)
# ax3.scatter(x, 2 * y ** 2 - 1, color='r')
# ax4.plot(x, 2 * y ** 2 - 1, color='r')
#
# # Four axes, returned as a 2-d array
# f, axarr = plt.subplots(2, 2)
# axarr[0, 0].plot(x, y)
# axarr[0, 0].set_title('Axis [0,0]')
# axarr[0, 1].scatter(x, y)
# axarr[0, 1].set_title('Axis [0,1]')
# axarr[1, 0].plot(x, y ** 2)
# axarr[1, 0].set_title('Axis [1,0]')
# axarr[1, 1].scatter(x, y ** 2)
# axarr[1, 1].set_title('Axis [1,1]')
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
# plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
# plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

# Four polar axes
# plt.subplots(2, 2, subplot_kw=dict(projection='polar'))

# plt.show()

#####################################
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
#
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
#
#
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

#####################################
# ax = plt.subplot(111)
#
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# # line, = plt.plot(t, s, lw=2)
# plt.plot(t, s, lw=2)
#
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )
#
# plt.ylim(-2,2)
# plt.show()

#####################################
# make up some data in the interval ]0, 1[
# y = np.random.normal(loc=0.5, scale=0.4, size=1000)
# y = y[(y > 0) & (y < 1)]
# y.sort()
# x = np.arange(len(y))
#
# # plot with various axes scales
# plt.figure(1)
#
# # linear
# plt.subplot(221)
# plt.plot(x, y)
# plt.yscale('linear')
# plt.title('linear')
# plt.grid(True)
#
#
# # log
# plt.subplot(222)
# plt.plot(x, y)
# plt.yscale('log')
# plt.title('log')
# plt.grid(True)
#
#
# # symmetric log
# plt.subplot(223)
# plt.plot(x, y - y.mean())
# plt.yscale('symlog', linthreshy=0.05)
# plt.title('symlog')
# plt.grid(True)
#
# # logit
# plt.subplot(224)
# plt.plot(x, y)
# plt.yscale('logit')
# plt.title('logit')
# plt.grid(True)
#
# plt.show()
#####################################