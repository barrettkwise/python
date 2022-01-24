productCost = int
try:
    productCost = int(productCost)
except ValueError:
    pass  # it was a string, not an int.
