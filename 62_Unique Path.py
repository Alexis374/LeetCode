'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
#从起点，经过（m-1，n-1）个方格才能走到终点，需要走m+n-2步，其中横着走需要走m-1步
#所以需要C(m-1)/(m+n-2)，实现组合数的计算即可。用cpp java实现容易溢出
#当然也可以考虑动态规划 f(m,n) = f(m-1,n)+f(m,n-1)
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        res = 1
        for i in range(n,n+m-1):
            res *= i 
            res /= i-n+1
        return res