class ProductOfNumbers:
    def __init__(self):
        # Initialize a list with one element '1' to represent the prefix product
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        # Adds the number to the sequence of numbers
        if num == 0:
            # If the number is zero, reset the list since any subsequent product will be zero
            self.prefix_products = [1]
        else:
            # Calculate the new product by multiplying the last product in the list with the new number
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # Returns the product of the last k numbers in the sequence
        if len(self.prefix_products) <= k:
            # If k is greater than or equal to the number of elements, the product is zero
            return 0
        else:
            # Otherwise, return the product of the last k numbers
            # by dividing the last prefix product by the product at (n-k-1)th position
            return self.prefix_products[-1] // self.prefix_products[-k - 1]