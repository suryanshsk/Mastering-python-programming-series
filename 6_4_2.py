class Calculator:
    def add(self, a, b=0):
        return a + b
calc = Calculator()
print(calc.add(10))  # 10
print(calc.add(10, 5))  # 15
