def method_decorator(func):
    def wrapper(self):
        print(f"Before {func.__name__} is called")
        result = func(self)
        print(f"After {func.__name__} is called")
        return result
    return wrapper

class MyClass:
    @method_decorator
    def greet(self):
        print("Greetings from MyClass!")

obj = MyClass()
obj.greet()
