# Part 1

# Assume you want to build two functions for discounting products on a website.
# Function number 1 is for student discount which discounts the current price by 10 %.
# Function number 2 is for an additional discount for regular buyers which discounts an additional 5 % on the current student discounted price.
# Depending on the situation, we want to be able to apply both discounts on the products.
# Design the above two mentioned functions and apply them both simultaneously on the price.


person = input("Who does the Discount apply to a Student, Buyer or Both: ")
price = input("Please enter the price")

price = int(price)

person = person.lower()


def student(price):
    newprice = price * .10
    studentprice = price - newprice
    studentprice = str(studentprice)
    price = str(price)
    print("Before Discount " + price)
    print("The Student price is: " + studentprice)


def buyer(price):
    newprice = price * .15
    buyerprice = price - newprice
    buyerprice = str(buyerprice)
    price = str(price)
    print("Before Discount " + price)
    print("The Buy Price After Discount is: " + buyerprice)


def both(price):
    newprice = price * .25
    bothprice = price - newprice
    bothprice = str(bothprice)
    price = str(price)
    print("Before Discount: " + price)
    print("The Price After Both Discounts is: " + bothprice)


if person == "student":
    print("Getting Student Discount")
    student(price)
elif person == "buyer":
    print("Getting Regular Buyer Discount")
    buyer(price)
elif person == "both":
    print("Getting Discount for Student and Regular Buyer")
    both(price)
