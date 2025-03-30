class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Create a dictionary to store the last occurrence of each character.
        last_occurrence = {char: index for index, char in enumerate(S)}
      
        # Initialize variables.
        # `max_last` represents the farthest index any character in the current partition has been seen.
        # `partition_start` represents the start of the current partition.
        max_last = partition_start = 0
      
        # This list will hold the sizes of the partitions.
        partition_sizes = []
      
        # Iterate through the characters of the string along with their indices.
        for index, char in enumerate(S):
            # Update `max_last` to be the max of itself and the last occurrence of the current character.
            max_last = max(max_last, last_occurrence[char])
          
            # If the current index is the last occurrence of all characters seen so far in this partition,
            # that means we can end the partition here.
            if max_last == index:
                # Append the size of the current partition to the list (`index - partition_start + 1`).
                partition_sizes.append(index - partition_start + 1)
              
                # Update `partition_start` to the next index to start a new partition.
                partition_start = index + 1
      
        # Return the list of partition sizes.
        return partition_sizes