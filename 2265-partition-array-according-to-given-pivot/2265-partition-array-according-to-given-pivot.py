class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Initialize lists to hold numbers smaller than,
        # equal to, and greater than the pivot
        smaller_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        # Iterate through each number in the input list
        for number in nums:
            # If the number is less than the pivot,
            # add it to the smaller_than_pivot list
            if number < pivot:
                smaller_than_pivot.append(number)
            # If the number is equal to the pivot,
            # add it to the equal_to_pivot list
            elif number == pivot:
                equal_to_pivot.append(number)
            # If the number is greater than the pivot,
            # add it to the greater_than_pivot list
            else:
                greater_than_pivot.append(number)

        # Combine the lists and return the result,
        # with all numbers less than the pivot first,
        # followed by numbers equal to the pivot,
        # and finally numbers greater than the pivot
        return smaller_than_pivot + equal_to_pivot + greater_than_pivot