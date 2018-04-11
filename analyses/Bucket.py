"""Bucket provides aggregate analysis of data points grouped by a common column value.

Specifically, a lot of correlations rely on grouping specific data points,
followed by seeing if any bucket is significantly greater than other buckets.
"""


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
        if self.size() < 3:
            s['message'] = 'Only ' + str(self.size()) + ' entries, not enough points.'
            return s
        s['grades'] = [d.summary() for d in self.grades]
        s['salaries'] = [d.summary() for d in self.salaries]
        return s

    def size(self):
        return min(min(map(lambda x: x.count(), self.grades)), min(map(lambda x: x.count(), self.salaries)))
