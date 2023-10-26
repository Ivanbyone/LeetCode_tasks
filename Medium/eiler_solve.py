from time import perf_counter
from numba import jit


@jit(nopython=True, fastmath=True)
def f():
    for a in range(1, 150):
        for b in range(1, 150):
            for c in range(1, 150):
                for d in range(1, 150):
                    for e in range(1, 150):
                        if a**5+b**5+c**5+d**5 == e**5:
                            return a+b+c+d+e


start = perf_counter()
print(f())
end = perf_counter()
print(end-start)
