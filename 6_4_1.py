#Different classes can have methods with 
# the same name but different implementations
# Base class: Hrithik Roshan
class HrithikRoshan:
    def role(self):
        print("I am Hrithik Roshan, the actor!")

# Subclass 1: Hrithik as a superhero
class lady:
    def role(self):
        print("I am Hrithik as a lady!")

# Subclass 2: Hrithik as a king
class security_guard:
    def role(self):
        print("I am Hrithik as a security guard!")

# Function to show polymorphism in action
def show_role(hritik):
    hritik.role()

# Creating objects for different forms
hrithik = HrithikRoshan()
second_role = lady()
third_role = security_guard()

# Calling the same method but getting different outputs
show_role(hrithik)  # Output: I am Hrithik Roshan, the actor!
show_role(second_role)  # Output: I am Hrithik as a superhero!
show_role(third_role) #output : I am Hritik as a security guard!