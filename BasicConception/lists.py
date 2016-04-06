# a = [1, 2, 3]
# b = [3.2, 'hello']
# print a + b
# print a*2

# a = [10, 11, 12, 13, 14]
# a[0] = 100
# print a
# a = [10, 11, 12, 13, 14]
# a[1:3] = [1, 2, 3, 4]
# print a
# a = [10, 1, 2, 11, 12]
# print a[1:3]
# a[1:3] = []
# print a
# a = [10, 11, 12, 13, 14]
# a[::2] = [1, 2, 3]
# print a

# a = [1002, 'a', 'b', 'c']
# del a[0]
# print a
# a = [1002, 'a', 'b', 'c']
# del a[1:]
# print a

# a = ['a', 1, 'b', 2, 'c']
# del a[::2]
# print a
# a = [10, 11, 12, 13, 14]
# print 10 in a
# print 10 not in a
# s = 'hello world'
# print 'he' in s
# print 'world' not in s

# a = [10, 'eleven', [12, 13]]
# print a[2]

# a = [11, 12, 13, 12, 11]
# print a.count(11)
# print a.index(12)

# a = [10, 11, 12]
# a.append(11)
# print a
# a.append([11, 12])  # will output [10, 11, 12, 11, [11, 12]]
# print a
# a = [10, 11, 12, 11]
# a.extend([1, 2]) # will output [10, 11, 12, 11, 1, 2]
# print a

# a = [10, 11, 12, 13, 11]
# a.insert(3, 'a')
# print a

# a = [10, 11, 12, 13, 11]
# a.remove(11)  #remove first appearance
# print a

# a = [10, 11, 12, 13, 11]
# print a.pop(2)
# print a

# a = [10, 1, 11, 13, 11, 2]
# a.sort()  # a changed
# print a
# a = [10, 1, 11, 13, 11, 2]
# b = sorted(a)  # a not changed
# print a
# print b

# a = [1, 2, 3, 4, 5, 6]
# a.reverse()
# print a
# a = [1, 2, 3, 4, 5, 6]
# b = a[::-1]
# print a
# print b
