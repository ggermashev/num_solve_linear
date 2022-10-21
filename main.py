from matplotlib import pyplot as plt
import numpy as np


def get_func(x):
    return x ** 5 - x ** 4 - 3 * x - 1


def get_dif_func(x):
    return 5 * x ** 4 - 4 * x ** 3 - 3


def newthon_method(e, x_prev=6, x_next=-10):
    x_next = x_prev - get_func(x_prev) / get_dif_func(x_prev)
    if (np.abs(x_prev - x_next) > e):
        return newthon_method(e, x_prev=x_next)
    else:
        return x_next


def dihotomia_method(e, left=0, right=10):
    mid = (right + left) / 2.0
    func = get_func(mid)
    if abs(func) < e:
        return mid
    elif func * get_func(left) < 0:
        return dihotomia_method(e, left, mid)
    else:
        return dihotomia_method(e, mid, right)


print('newthon`s')
print("10^-3: ", newthon_method(10 ** -3))
print("10^-6: ", newthon_method(10 ** -6))
print("10^-9: ", newthon_method(10 ** -9))
print('dihotomia')
print("10^-3: ", dihotomia_method(10 ** -3))
print("10^-6: ", dihotomia_method(10 ** -6))
print("10^-9: ", dihotomia_method(10 ** -9))
