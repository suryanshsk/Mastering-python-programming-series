# Base Class
class Phone:
    def speak(self):
        print("I am an Phone.")

# Derived Class 1
class Samsung(Phone):
    def android(self):
        print("I am Samsung Galaxy S23")

# Derived Class 2
class Apple(Phone):
    def ios(self):
        print("I am Iphone 15 pro Max")

# Object of Samsung Class
Samsung = Samsung()
Samsung.speak()  # Inherited method
Samsung.android()   # Unique to Samsung class

# Object of Apple Class
Apple = Apple()
Apple.speak()  # Inherited method
Apple.ios()   # Unique to Apple class