import math


class frange:
    def __init__(self, left, right=None, step=1, around: int = 2):
        if right is None:
            self._left = 0
            self._right = left
        else:
            self._left = left
            self._right = right
        self._step = step
        self._around = around
        self._value = self._left

    def __next__(self):
        if self._step > 0:
            if self._value >= self._right:
                raise StopIteration('Stop')
        else:
            if self._value <= self._right:
                raise StopIteration('Stop')
        result = round(self._value, self._around)
        self._value += self._step
        return result

    def __iter__(self):
        return self


a = frange(10, 2, -2)
print(list(a))

assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')

