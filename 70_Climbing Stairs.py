'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''
#n=1只有一种，n=2有两种，从末尾考虑，设上第n个台阶有f(n)
#由于每次只能登上一个或两个台阶，登上最后一个台阶非一步即二步，而在这之前需要爬
#n-1 或n-2级台阶，各有f(n-1)和f(n-2)中方法，所以f(n)=f(n-1)+f(n-2)
#斐波那契，用空间换时间的方法，避免递归
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        result = [0,1,2]
        if n>=3:
            for i in range(3,n+1):
                result.append(result[i-1]+result[i-2])
        return result[n]