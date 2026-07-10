class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(n^2), since all the checks per square are O(1), and we check n^2 squares
        # Space: O(n^2), since we store 3 copies of every square, and we have n^2 squares
        # NOTE: To make a 2D list of a certain size, never use [set()] * 9, since each sublist will be linked

        row_list = [set() for _ in range(9)]
        col_list = [set() for _ in range(9)]
        box_list = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue
                num = int(num)
                if num < 1 or num > 9:
                    return False

                if num in row_list[i] or num in col_list[j] or num in box_list[(i//3)*3 + j//3]:
                    print(num, i, j)
                    return False
                
                row_list[i].add(num)
                col_list[j].add(num)
                box_list[(i//3)*3 + j//3].add(num)

        return True
                