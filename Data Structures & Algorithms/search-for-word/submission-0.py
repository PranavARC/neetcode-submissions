class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.exists = False
        self.board = board
        self.word = word

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.recExist(0, row, col, set())

        return self.exists
    
    def recExist(self, word_ind, row, col, index_set):
        if self.exists:
            return

        if word_ind == len(self.word):
            self.exists = True
            return
        
        if not 0 <= row < len(self.board) or not 0 <= col < len(self.board[0]) or (row, col) in index_set:
            return

        char = self.board[row][col]

        if char != self.word[word_ind]:
            return
 
        index_set.add((row, col))

        for r,c in [(1,0), (-1,0), (0,1), (0,-1)]:
            self.recExist(word_ind+1, row+r, col+c, set(index_set))

        