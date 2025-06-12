class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWords(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWords(w)
        
        r,c = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(i,j,node,word):
            if (i<0 or j<0 or i == r or j == c or (i,j) in visit or board[i][j] not in node.children):
                return
            visit.add((i,j))
            node = node.children[board[i][j]]
            word+=board[i][j]

            if node.isWord:
                res.add(word)
            
            dfs(i+1,j,node,word)
            dfs(i-1,j,node,word)
            dfs(i,j+1,node,word)
            dfs(i,j-1,node,word)
            visit.remove((i,j))

        for i in range(r):
            for j in range(c):
                dfs(i,j,root,"")
        return list(res)