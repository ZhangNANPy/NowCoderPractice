class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0:
            return 0
        self.hasbeen = []
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            for j in range(cols):
                if self.isMoving(threshold, i, j):
                    self.hasbeen.append([i, j])
        return len(self.hasbeen)

    def isMoving(self, threshold,  row, col):
        if row == 0 and col == 0:
            return True
        if sum([int(i) for i in str(row) + str(col)]) <= threshold:
            if col - 1 >= 0 and [row, col - 1] in self.hasbeen:  # left
                return True
            if row - 1 >= 0 and [row - 1, col] in self.hasbeen:  # up
                return True
            if col + 1 < self.cols and [row, col + 1] in self.hasbeen:  # right
                return True
            if row + 1 < self.rows and [row + 1, col] in self.hasbeen:  # down
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(10, 30, 30))