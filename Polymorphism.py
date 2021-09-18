# Part 4
#
# Using the concept of object - oriented programming and inheritance, create a superclass named Computer, which has
# two subclasses named Desktop and Laptop.
# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications
# and display the specifications of the computer.
#
#
# You can use any specifications that you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them
# for example laptop can have weight as a special specification.
#
#
# Make sure that the subclasses have their own methods to get and display their special specification.
# Create an object of laptop / desktop and make sure to call all the methods from the computer
# class as well as the methods from the own class
#

class Computer:
    def __init__(self,cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def getspecs(self):
        cpu = 100
        ram = 32

    def displayspecs(self):
        print("Computer Cpu: " + str(self.cpu))
        print("Computer Ram: " + str(self.ram))



class Desktop(Computer):

    def getdesktopspecs(self):
        self.monitor = 32

    def printDesktopspecs(self,cpu, ram, monitor):
        print("Desktop Ram: " + str(self.ram))
        print("Desktop CPU: " + str(self.cpu))
        print("Desktop Monitor: " + str(self.monitor))


class Laptop(Computer):

    def getlaptopspecs(self):
        self.weighs = 32

    def printLaptopspecs(self,ram, cpu, weighs):
        print("Laptop Ram: " + str(self.ram))
        print("Laptop Cpu: " + str(self.cpu))
        print("Laptop Weight: " + str(self.weighs))

c = Computer(32,25)
l = Laptop(27,44)
d = Desktop(16,23)

c.getspecs()
c.displayspecs()
d.getdesktopspecs()
d.printDesktopspecs(22,15,23)
l.getlaptopspecs()
l.printLaptopspecs(15,23,9)




