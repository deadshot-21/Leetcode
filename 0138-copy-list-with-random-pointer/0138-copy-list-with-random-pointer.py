"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyHashmap = {None:None}
        curr = head
        while curr:
            copyHashmap[curr] = Node(curr.val)
            curr=curr.next
        curr = head
        while curr:
            copy = copyHashmap[curr]
            copy.next = copyHashmap[curr.next]
            copy.random = copyHashmap[curr.random]
            curr = curr.next
        return copyHashmap[head]