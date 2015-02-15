'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        new_s = s[::-1]
        cnt = 0
        sum = 0
        while cnt<len(s):
            if 'A'<=new_s[cnt]<='Z':
                sum += (ord(new_s[cnt])-64)*(26**cnt)
                cnt+=1
        return sum