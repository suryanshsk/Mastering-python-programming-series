#Generators are functions that return an iterable 
# set of items, one at a time, in a lazy manner. 
def meal_generator():
    yield "Starter"
    yield "Main Course"
    yield "Dessert"

for meal in meal_generator():
    print(meal)

#The yield keyword is used to return a list of values from a function.
"""Use generators when you need to handle large datasets
 or infinite sequences, like reading huge files line by line.
 They’re like smart, memory-saving functions!"""