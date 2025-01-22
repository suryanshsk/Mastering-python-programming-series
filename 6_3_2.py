"""A feature where a class can inherit from more than one parent class """
class employee:
    def feature1(self):
        print('Quality of employee')

class clients:
    def feature2(self):
        print('Quality of clients')
class compnay(employee, clients):
    def feature3(self):
        print('emoloyee + clients = company')

obj = compnay()
obj.feature1()
obj.feature2()
obj.feature3()

""" it can sometimes lead to complexity like the Diamond Problem. 
 Diamond Problem is a potential issue in multiple
   inheritance where a class inherits from two classes that share
     a common ancestor
       A
      / \
     B   C
      \ /
       D
"""