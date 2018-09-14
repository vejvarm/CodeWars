""" Pyramid Slide Down
https://www.codewars.com/kata/pyramid-slide-down/python
Let's say that the 'slide down' is a sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23
Your task is to write a function longestSlideDown (in ruby: longest_slide_down) that takes a pyramid representation as argument and returns its' longest 'slide down'.
"""
from random import randint


class Pyramid(object):

    def __init__(self, pyramid):
        self.pyramid = pyramid
        self.memo = [*pyramid[0]]  # Memoization

    def __str__(self):
        result = ''
        for row_num, row in enumerate(self.pyramid):
            result += ' '*2*(len(self.pyramid)-row_num) + '  '.join('{:02d}'.format(num) for num in row) + '\n'

        return result

    # using Memoization
    def longest_slide_down(self):
        for row in self.pyramid[1:]:
            placeholder = []
            for i in range(1, len(row)-1):
                placeholder.append(max(self.memo[i-1], self.memo[i]) + row[i])
            # update memo
            self.memo.append(self.memo[-1] + row[-1])
            self.memo[0] += row[0]
            self.memo[1:-1] = placeholder

        return max(self.memo)


if __name__ == '__main__':
    # list_pyr = [[randint(1, 99) for i in range(j)] for j in range(1, 100)]
    list_pyr = [
                [75],
                [95, 64],
                [17, 47, 82],
                [18, 35, 87, 10],
                [20,  4, 82, 47, 65],
                [19,  1, 23, 75,  3, 34],
                [88,  2, 77, 73,  7, 63, 67],
                [99, 65,  4, 28,  6, 16, 70, 92],
                [41, 41, 26, 56, 83, 40, 80, 70, 33],
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
               ]
    pyr = Pyramid(list_pyr)
    print(pyr)
    print(pyr.longest_slide_down())
