# # map
# def cube(x):
#     return x*x*x


# print(cube(2))
# l = [1, 2, 4, 6, 4, 3]
# newl = list(map(cube, l))
# print(newl)

# # filter


# def filter_function(a):
#     return a > 2


# newl2 = list(filter(filter_function, l))
# print(newl2)
from functools import reduce
number = [1, 2, 3, 4, 5]


def mysum(x, y):
    return x+y


sum = reduce(mysum, number)
print(sum)
