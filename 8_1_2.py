"""An iterator is an object in Python that allows 
you to traverse through all the elements
 in a collection, like a list or a tuple, one at a time. 
 Think of it like a bookmark—you can go to the next item 
 whenever you want."""

# A simple example
bookmark = [1, 2, 3]  # A collection
my_iter = iter(bookmark)  # Create an iterator

# Access elements one by one
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3

