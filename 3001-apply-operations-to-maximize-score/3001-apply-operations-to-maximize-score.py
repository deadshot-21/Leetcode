from typing import List

def prime_factors(n: int) -> int:
    # Initialize the starting divisor and an empty set to store unique prime factors
    divisor = 2
    unique_prime_factors = set()
  
    # Loop to find prime factors
    while divisor * divisor <= n:
        while n % divisor == 0:
            unique_prime_factors.add(divisor)
            n //= divisor
        divisor += 1
      
    # If there is a remaining prime factor larger than the square root of original n, add that too
    if n > 1:
        unique_prime_factors.add(n)
  
    # Return the count of unique prime factors
    return len(unique_prime_factors)


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7  # The modulo value given in the problem
      
        # Create an array that holds tuples of (index, number of prime factors, value) for each number
        arr = [(index, prime_factors(x), x) for index, x in enumerate(nums)]
        n = len(nums)  # The length of the provided nums list
      
        left_boundaries = [-1] * n  # Will hold the left boundaries for each number
        right_boundaries = [n] * n  # Will hold the right boundaries for each number
        stack = []  # Initialize an empty stack
      
        # Calculate left boundary for each element
        for index, factors_count, value in arr:
            while stack and stack[-1][0] < factors_count:
                stack.pop()
            if stack:
                left_boundaries[index] = stack[-1][1]
            stack.append((factors_count, index))
      
        stack.clear()  # Clear the stack for reuse
      
        # Calculate right boundary for each element, processing from the end to the front
        for index, factors_count, value in reversed(arr):
            while stack and stack[-1][0] <= factors_count:
                stack.pop()
            if stack:
                right_boundaries[index] = stack[-1][1]
            stack.append((factors_count, index))
      
        # Sort the array in decreasing order based on the value
        arr.sort(key=lambda x: -x[2])
      
        answer = 1  # Initialize answer to 1 since we'll be multiplying
        for index, factors_count, value in arr:
            left_index, right_index = left_boundaries[index], right_boundaries[index]
            count = (index - left_index) * (right_index - index)
          
            # If we can use the entire count within the limit k
            if count <= k:
                answer = answer * pow(value, count, mod) % mod
                k -= count
            else:
                # Use only the remaining k increments and then break
                answer = answer * pow(value, k, mod) % mod
                break
      
        # Return the final answer modulo the given mod value
        return answer