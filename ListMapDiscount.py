# Part 3

# Consider a list in Python which includes prices of all the items in a store.
# Build a function to discount the price of all the products by 10 %.
# Use a map to apply the function to all the elements of the list so that all the product prices are discounted.


mypricelist = [2.36, 3.58, 15.43, 39.39, 25.25]


def discounts(x):
    xdiscount = x*.1
    xdiscount2=x-xdiscount
    xdiscount2 = float(xdiscount2)
    xdiscount2 = "{:.2f}".format(xdiscount2)
    return xdiscount2

results = list(map(discounts, mypricelist))


print(results)
