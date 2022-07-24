from max_min import numbers


class Calc:
    def __init__(self):
        self.nums = numbers()

    def maxima(self):
        return max(self.nums)

    def minima(self):
        return min(self.nums)

    def add(self):
        return sum(self.nums)

    def exp(self):
        if len(self.nums) >= 2:
            return self.nums[0]**self.nums[1]
        else:
            pass


x = Calc()
print(f'''
the maximum no. is {x.maxima()}
the minimum no. is {x.minima()}
sum of all the nos. is {x.add()}
first no. raised to second is {x.exp()}
''')
