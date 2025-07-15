import codewars_test as test

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    intervals.sort()
    total = 0
    current_start = None
    current_end = None

    for start, end in intervals:
        if current_start is None:
            current_start = start
            current_end = end
        elif start <= current_end:
            current_end = max(current_end, end)
        else:
            total += current_end - current_start
            current_start = start
            current_end = end

    if current_start is not None:
        total += current_end - current_start

    return total





@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(sum_of_intervals([(1, 5)]), 4)
        test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
        test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
        test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)


    @test.it("Large numbers")
    def it_2():
        test.assert_equals(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
        test.assert_equals(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)


