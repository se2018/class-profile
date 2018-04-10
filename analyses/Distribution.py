"""Distribution represents an array of integers, as well as any statistical
metadata on the distribution.
"""
import numpy as np


class Distribution:

    def __init__(self, arr):
        self.errors = []
        unique, counts = np.unique(arr, return_counts=True)
        c = dict(zip(unique, counts))
        if None in c:
            self.errors.append('Found ' + str(c[None]) + ' occurrences of None. Removed.')
        self.arr = np.array(arr)

    def mean(self):
        if self.count() == 0:
            return None
        return np.mean(self.arr)

    def stddev(self):
        if self.count() == 0:
            return None
        return np.std(self.arr)

    def count(self):
        return self.arr.size

    def minimum(self, include_zero=False):
        if self.count() == 0:
            return None
        num = np.amin(self.arr)
        if include_zero and num == 0:
            return np.partition(self.arr, 1)[1]
        return num

    def maximum(self):
        if self.count() == 0:
            return None
        return np.amax(self.arr)

    def median(self):
        if self.count() == 0:
            return None
        return np.median(self.arr)

    def split_count(self):
        if self.count() == 0:
            return [[], [], [], []]
        upper = self.arr[self.arr >= self.mean()]
        lower = self.arr[self.arr < self.mean()]

        s1 = lower[lower < self.mean() - self.stddev()].tolist()
        s2 = lower[lower >= self.mean() - self.stddev()].tolist()
        s3 = upper[upper < self.mean() + self.stddev()].tolist()
        s4 = upper[upper >= self.mean() + self.stddev()].tolist()

        return [s1, s2, s3, s4]

    def summary(self):
        s = {
            'mean': self.mean(),
            'stddev': self.stddev(),
            'count': self.count(),
            'minimum': self.minimum(),
            'maximum': self.maximum(),
            'median': self.median(),
            'split_count': self.split_count(),
            'errors': self.errors
        }

        return s
