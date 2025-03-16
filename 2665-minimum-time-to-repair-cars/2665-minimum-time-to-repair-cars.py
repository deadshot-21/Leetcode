from bisect import bisect_left
from typing import List
from math import sqrt

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Define a function to check if a given time 't' is sufficient
        # to repair 'cars' number of cars with the given 'ranks'.
        def is_time_sufficient(t: int) -> bool:
            # For each rank, calculate how many cars can be repaired
            # by the given time 't', and sum them all up. If the sum
            # equals or exceeds the total number of cars needed to be repaired,
            # then the time 't' is sufficient.
            return sum(int(sqrt(t // rank)) for rank in ranks) >= cars

        # Since 'check' function returns a boolean, we need a range
        # to apply bisect_left on. The range starts from 0 to an upper limit.
        # The upper limit is the maximum rank times the square of the number
        # of cars as a worst-case scenario for the required time.
        max_time = ranks[0] * cars * cars
      
        # Perform a binary search for the leftmost time 't' for which
        # is_time_sufficient(t) is True. This will be the minimum time
        # required to repair 'cars' cars given the 'ranks'.
        min_time_required = bisect_left(range(max_time), True, key=is_time_sufficient)

        # Return the minimum time found
        return min_time_required
