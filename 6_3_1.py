# Parent Class
class Phone:
    def sound(self):
        print("This phone can make a call and vice verca.")

# Child Class
class Ring(Phone):
    def sound(self):  # Overriding the parent method
        print("Phone ringing..... ")

# Using Inheritance
nokia = Ring()
nokia.sound()  # Calls the overridden method
