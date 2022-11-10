# Malik Coleman
# Module 4C - Advnced Classes

import math
from functools import reduce



class MyMath:
    "Class with math functions"

    def __init__(self):
        "Initialize"
        self.num_list = []

    def average(self):
        "Returns average."
        return sum(self.num_list) / len(self.num_list)

    def standard_deviation(self):
        "Returns the standard deviation."
        mean = sum(self.num_list) / len(self.num_list)
        variance = sum([((x - mean) ** 2) for x in self.num_list]) / len(self.num_list)
        return math.sqrt(variance)

    def add_numbers(self):
        "Adds numbers of a list together."
        num = ''
        while num != 123:
            num = int(input("Enter a number: "))
            print("Enter 123 to quit.")
            if num != 123:
                self.num_list.append(num)

    def max_num(self):
        "Returns maxium number in a list of numbers."
        max_num = reduce(lambda x, y: y if x < y else x, self.num_list)
        return max_num

    def main(self):
        myMath = MyMath()
        myMath.add_numbers()
        print("Average: ", myMath.average())
        print("Standard Deviation: ", myMath.standard_deviation())

myMath = MyMath()
myMath.main()
