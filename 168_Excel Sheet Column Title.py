'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

'''
class Solution:
    # @return a string
    #将数字换成26进制的数，但要注意换算过的数字没有0（从1开始），所以需先将num-1，否则z换算成的为10
    def convertToTitle(self, num):
        num_list = []
        while num>0:
            num -= 1
            num_list.append(num%26)
            num=num/26
        result_list = []
        return ''.join(chr(65+i) for i in num_list[::-1])

#or:
class Solution:
    # @return a string
    def convertToTitle(self, num):
        num_list = []
        while num>0:
            num -= 1
            num_list.append(num%26)
            num=num/26
        result = ''
        for i in num_list[::-1]:
            result += chr(i+65)
        return result