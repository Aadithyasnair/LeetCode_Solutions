"""
Problem ID : 3933
Title      : Two Sum
Language   : Python
Solved Date: 2026-07-16
"""
class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        row_maxi = [max(row) for row in matrix]
        maxi = max(row_maxi)
        for i in range(m):
            for j in range(n):
                x = matrix[i][j]
                if not x: continue
                if x == maxi:
                    ans += 1
                    continue
                flag = True
                r1 = max(0, i-x)
                r2 = min(m-1, i+x)
                for r in range(r1, r2 + 1):
                    if row_maxi[r] <= x: continue
                    if r == i-x or r == i+x:
                        c1 = max(0, j - x + 1)
                        c2 = min(n - 1, j + x - 1)
                    else:
                        c1 = max(0, j - x)
                        c2 = min(n - 1, j + x)
                    if c1 <= c2:
                        if max(matrix[r][c1 : c2 + 1]) > x:
                            flag = False
                            break
                if flag:
                    ans += 1
        return ans