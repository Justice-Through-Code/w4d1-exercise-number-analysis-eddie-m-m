#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.

    # declare accumulator variable and initialize it to zero
    # loop through range of numbers bounded by 'start' and 'end + 1'
    # for each iteration, add current value of loop variable to accumulator variable
    # return accumulator variable after loop terminates

    sum = 0
    for num in range(start, end + 1):
        sum += num

    return sum


def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

    # declare variable for storing smallest number and initialize it to start value
    # loop through range of numbers bounded by 'start' and 'end + 1'
    # for each iteration, if (current value of loop variable < storage variable) then (set storage variable to current value of loop variable)
    # return storage variable after loop terminates

    smallest_num = start
    for num in range(start, end + 1):
        if num < smallest_num:
            smallest_num = num

    return smallest_num


def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

    # declare variable for storing largest number and initialize it to start value
    # loop through range of numbers bounded by 'start' and 'end + 1'
    # for each iteration, if (current value of loop variable > storage variable) then (set storage variable to current value of loop variable)
    # return storage variable after loop terminates

    largest_num = start
    for num in range(start, end + 1):
        if num > largest_num:
            largest_num = num

    return largest_num


def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.

    # declare accumulator variable and initialize it to zero
    # loop through range of numbers bounded by 'start' and 'end + 1'
    # for each iteration, if (the modulus/remainder of current value of loop variable is zero) then (increment the accumulator variable)
    # return accumulator variable after loop terminates

    even_nums = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_nums += 1

    return even_nums

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.

    # declare accumulator variable and initialize it to zero
    # loop through range of numbers bounded by 'start' and 'end + 1'
    # for each iteration, if (the modulus/remainder of current value of loop variable is not zero) then (increment the accumulator variable)
    # return accumulator variable after loop terminates

    odd_nums = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            odd_nums += 1

    return odd_nums
