class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l, r = 0, len(matrix)*len(matrix[0])
        # print(l, r, len(matrix))
        # while l <= r :
        #     row = (l + r) // (2* len(matrix))
        #     col = (l + r) % (2 * len(matrix[0]))
        #     print(row-1, col-1)
        #     if matrix[row][col] > target :
        #         r = col - 1
        #     elif matrix[row][col] < target :
        #         l = row + 1
        #     else :
        #         return true

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
                
        if not ( top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1 
            elif target < matrix[row][m]:
                r = m - 1 
            else:
                return True
        return False
        