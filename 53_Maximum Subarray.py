#coding:utf-8
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''

#O(n) way:
#数组中的元素有两种去向，一是加入之前的子数组（之前的和>=0），二是重新开辟新的子数组(之前的和<0)。
#sum 记录当前元素加入子数组或是另开辟新数组后当前数组的和，result记录上次子数组的和，取最大值
#另要注意初始化的时候sum result都为0，若数组只有一个元素且该元素为负数,如[-1]，结果应为-1，而不是0，所以
#在计算第一次result时应该严格等于第一个元素
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = result= 0
        for idx,i in enumerate(A):
            sum = sum+i if sum >= 0 else i
            result = sum if idx==0 else max(result,sum)
        return result