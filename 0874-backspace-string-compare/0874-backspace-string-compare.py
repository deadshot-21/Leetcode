class Solution:
    def backspaceCompare(self, string1: str, string2: str) -> bool:
        # Initialize pointers for both strings starting from the end
        index1, index2 = len(string1) - 1, len(string2) - 1
        # Initialize counters for skip characters ('#')
        skip_count1, skip_count2 = 0, 0

        # Compare characters in the strings from the end
        while index1 >= 0 or index2 >= 0:
            # Find the position of next valid character in string1
            while index1 >= 0:
                if string1[index1] == '#':
                    skip_count1 += 1
                    index1 -= 1
                elif skip_count1 > 0:
                    skip_count1 -= 1
                    index1 -= 1
                else:
                    break  # Found a valid character

            # Find the position of next valid character in string2
            while index2 >= 0:
                if string2[index2] == '#':
                    skip_count2 += 1
                    index2 -= 1
                elif skip_count2 > 0:
                    skip_count2 -= 1
                    index2 -= 1
                else:
                    break  # Found a valid character

            # If both strings have valid characters to compare
            if index1 >= 0 and index2 >= 0:
                if string1[index1] != string2[index2]:
                    # Characters do not match
                    return False
            # If one index is negative, it means one string has more characters left after processing backspaces
            elif index1 >= 0 or index2 >= 0:
                return False

            # Move to the next character
            index1, index2 = index1 - 1, index2 - 1

        # If all characters matched, return True
        return True