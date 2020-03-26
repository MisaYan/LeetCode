import numpy as np
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row, col = 0, 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    row, col = i, j
                    break
        s = ''.join(board[row])
        s = s.replace('.', '')
        if 'Rp' in s:
            count += 1
        if 'pR' in s:
            count += 1
        m = ''.join(x[col] for x in board)
        m = m.replace('.', '')
        if 'Rp' in m:
            count += 1
        if 'pR' in m:
            count += 1
        return count
