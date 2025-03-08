class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Initial count of 'W' in the first window of size k
        white_count = blocks[:k].count('W')
        # Initialize minimum white blocks to be recolored with the count from the first window
        min_recolors = white_count

        # Slide the window of size k through the blocks string
        for index in range(k, len(blocks)):
            # If the newly included block in the window is white, increment the count
            if blocks[index] == 'W':
                white_count += 1
            # If the block that is exiting the window is white, decrement the count
            if blocks[index - k] == 'W':
                white_count -= 1
            # Update the minimum if the current count is less than the previous minimum
            min_recolors = min(min_recolors, white_count)

        # Return the minimum number of white blocks that need to be recolored
        return min_recolors