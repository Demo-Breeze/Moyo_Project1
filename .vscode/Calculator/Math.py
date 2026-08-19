import math
class Math:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    def arcosine(self, x):
        if x < -1 or x > 1:
            raise ValueError("Input must be in the range [-1, 1].")
        return math.acos(x)
    def arcsine(self, x):
        if x < -1 or x > 1:
            raise ValueError("Input must be in the range [-1, 1].")
        return math.asin(x)
    def arctangent(self, x):
        return math.atan(x)
    def cosine(self, x):
        return math.cos(x)
    def sine(self, x):
        return math.sin(x)
    def tangent(self, x):
        return math.tan(x)
    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot compute factorial of a negative number.")
        return math.factorial(n)
    def logarithm(self, x, base=10):
        if x <= 0:
            raise ValueError("Logarithm input must be positive.")
        return math.log(x, base)
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return math.sqrt(x)
    def square(self, x):
        return x * x
    def power(self, x, y):
        return math.pow(x, y)
    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulus with a divisor of zero.")
        return a % b
    def absolute(self, x):
        return abs(x)
    def plus_minus(self,x):
        if x < 0:
            return x * -1
    def root(self,a,b):
        if b == 0:
            raise ValueError("The degree of the root (n) cannot be zero.")
    
        try:
            # Raising a number to the power of 1/n is equivalent to finding the n-th root
            return math.pow(a, 1 / b)
        except ValueError as e:
            # math.pow raises ValueError for negative numbers raised to fractional powers
            raise ValueError(f"Mathematical error computing the {b}-th root of {a}: {e}")
    
        