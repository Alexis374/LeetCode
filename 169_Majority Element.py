'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    # @param num, a list of integers
    # @return an integer
    #频率超过1/2，所以中间元素必为那个大多数的元素
    def majorityElement(self, num):
        num.sort()
        return num[len(num)/2]