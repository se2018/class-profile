"""Bucket provides aggregate analysis of data points grouped by a common column value.

Specifically, a lot of correlations rely on grouping specific data points,
followed by seeing if any bucket is significantly greater than other buckets.
"""
import json


class Bucket:

    def __init__(self, col_name, col_value, grades, salary):
        self.col_name = col_name
        self.col_value = col_value
        self.grades = grades   # sorted by time (i.e. term)
        self.salary = salary   # sorted by time (i.e. term)

    def summary(self):
        print 'Grade Summary for ', self.col_name, self.col_value
        for d in self.grades:
            print json.dumps(d.summary(), indent=True)

        print 'Salary Summary for ', self.col_name, self.col_value
        for d in self.salary:
            print json.dumps(d.summary(), indent=True)

    def size(self):
        return self.grades[0].count()  # Any distribution can work
