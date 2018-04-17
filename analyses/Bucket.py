"""Bucket provides aggregate analysis of data points grouped by a common column value.

Specifically, a lot of correlations rely on grouping specific data points,
followed by seeing if any bucket is significantly greater than other buckets.
"""
import numpy as np
from Distribution import Distribution


class Bucket:

    def __init__(self, col_name, col_value, grades, salaries):
        self.col_name = col_name
        self.col_value = col_value
        self.grades = grades   # sorted by time (i.e. term)
        self.salaries = salaries   # sorted by time (i.e. term)

    def summary(self):
        s = {}
        s['col_name'] = self.col_name
        s['col_value'] = self.col_value
        if self.max_size() < 3:
            s['message'] = 'Only ' + str(self.max_size()) + ' entries, not enough points.'
            return s
        s['grades'] = [d.summary() for d in self.grades]
        s['salaries'] = [d.summary() for d in self.salaries]
        s['size'] = self.max_size()
        return s

    def size(self):
        return min(min(map(lambda x: x.count(), self.grades)), min(map(lambda x: x.count(), self.salaries)))

    def max_size(self):
        return max(max(map(lambda x: x.count(), self.grades)), min(map(lambda x: x.count(), self.salaries)))

    @staticmethod
    def create_from_bucket(col_name, buckets):
        b = {}
        for val in buckets:
            if 'grades' not in buckets[val]:
                b[val] = buckets[val]
                continue
            grades = []
            for g in buckets[val]['grades']:
                a = np.array([])
                for split in g['split_count']:
                    a = np.append(a, split)
                grades.append(Distribution(a))

            salaries = []
            for s in buckets[val]['salaries']:
                a = np.array([])
                for split in s['split_count']:
                    a = np.append(a, split)
                salaries.append(Distribution(a))

            b[val] = Bucket(col_name, val, grades, salaries)
        return b
