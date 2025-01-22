class Phone:
    def __init__(self, brand):
        self.brand = brand
        print(f"successfully  Purchased {self.brand}")

    def __del__(self):
        print(f"successfully Sold  {self.brand} ")

# Create an object
Buy = Phone("Redmi Note 7")

# Delete the object 
del Buy
