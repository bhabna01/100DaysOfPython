# def double(x): return x*2


# print(double(5))
def appl(fx, value):
    return 6+fx(value)


def cube(x): return x*x*x
def avg(x, y): return (x+y)/2


print(avg(3, 5))
print(appl(cube, 2))
