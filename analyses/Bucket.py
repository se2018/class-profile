"""Bucket provides aggregate analysis of data points grouped by a common column value.

Specifically, a lot of correlations rely on grouping specific data points,
followed by seeing if any bucket is significantly greater than other buckets.
"""


class Bucket:

    def __init__(self, col_name, col_value, distributions):
        self.col_name = col_name
        self.col_value = col_value
        self.distributions = distributions   # sorted by time (i.e. term)
