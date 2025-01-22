# Question: Write a function to find the sum of all even numbers in a list.
def sum_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)
