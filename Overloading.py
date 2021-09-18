# Part 5

# Using the concept of operator overloading in Python, change the behavior of the multiplication
# operator in a way that multiplication operator behaves like an addition operator.
import tkinter


class amount:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __mul__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        a3 = amount(m1, m2)

        print("Test")

        return a3


s1 = amount(5,6)
s2 = amount(6,7)

a3 = s1 * s2
print(str(a3))

#https://www.youtube.com/watch?v=9wd50TKv_OQ
