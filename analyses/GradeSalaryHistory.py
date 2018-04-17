"""History before each coop. """
import numpy as np
import math


class GradeSalaryHistory:

    def __init__(self, grades, salaries, location, salary):
        self.grades = grades
        self.salaries = salaries
        self.location = location
        self.salary = salary

    def avg_salary(self):
        return np.mean(self.salaries[self.salaries != 0])

    def cum_avg(self):
        return np.mean(self.grades[self.grades != 0])

    def city(self):
        if len(self.location.split(',')) < 2:
            return ''
        return self.location.split(',')[0].strip()

    def country(self):
        if len(self.location.split(',')) < 2:
            return ''
        return self.location.split(',')[1].strip()

    def max_salary(self):
        if self.salaries.size == 0:
            return 0.0
        return np.amax(self.salaries)

    def max_grade(self):
        if self.grades.size == 0:
            return 0.0
        return np.amax(self.grades)

    def summary(self):
        return {
            'avg_salary': self.avg_salary(),
            'cumulative_avg': math.floor(self.cum_avg()),
            'highest_grade': self.max_grade(),
            'highest_salary': self.max_salary(),
            'result_salary': self.salary,
            'city': self.city(),
            'country': self.country()
        }
