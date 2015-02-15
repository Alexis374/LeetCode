'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        try:#to see if the target is in A,if it is,just return
            return A.index(target)
        except ValueError:
            # find the limit element of the target in the A list
            for idx,num in enumerate(A):
                if num>target:
                    return idx
            # if target is bigger than anyone in A,return the length of list
            return idx+1