class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        # If there's only one row or the string is shorter than the number of rows,
        # it means the pattern will be the same as the input string
        if num_rows == 1 or num_rows >= len(s):
            return s

        # Create an array to hold the rows
        rows = [''] * num_rows
        # The `step` variable controls the direction the "zigzag" is going.
        # It starts as 1, meaning "downwards", and will change to -1 to go "upwards".
        step = -1 
        # Start from the first row
        curr_row = 0

        # Iterate over each character in the string
        for char in s:
            # Append the current character to the current row
            rows[curr_row] += char
            # If we're at the top or bottom row, switch direction
            if curr_row == 0 or curr_row == num_rows - 1:
                step = -step
            # Move to the next row in the current direction
            curr_row += step

        # Concatenate all rows to form the final string
        return ''.join(rows)