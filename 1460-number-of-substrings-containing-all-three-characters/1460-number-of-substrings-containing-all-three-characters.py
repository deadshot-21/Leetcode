class Solution:
    def numberOfSubstrings(self, string: str) -> int:
        # Create a dictionary to keep track of the last seen index of 'a', 'b', and 'c'
        last_seen_index = {"a": -1, "b": -1, "c": -1}
        # Initialize answer to store the number of valid substrings
        answer = 0
        # Enumerate over the characters of the string
        for index, char in enumerate(string):
            # Update the last seen index for the current character
            last_seen_index[char] = index
            # Increment the answer by one more than the smallest last seen index among 'a', 'b', and 'c'
            # This is because a valid substring must include at least one of each
            answer += min(last_seen_index.values()) + 1

        # Return the total count of valid substrings that contain at least one of each 'a', 'b', and 'c'
        return answer