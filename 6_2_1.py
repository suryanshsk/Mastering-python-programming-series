class Phone:
    def __init__(self, brand, Processor, Price):
        self.brand = brand
        self.processor = Processor
        self.price = Price

    def display_info(self):
        print(f"{self.brand} {self.processor} {self.price}")

a = Phone( "Pixel 9 pro fold" ,"Tensor G4 processor" , "₹1,72,999" )
a.display_info()


"""self refers to the current instance of the class. It
 is used to access variables that belong to the class.
 
 self ensures that the attributes and methods are correctly 
 referenced within the class. It differentiates between instance
   variables and local variables.
 """
