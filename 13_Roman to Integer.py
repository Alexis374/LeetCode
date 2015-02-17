#coding:utf-8
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
#根据百度百科里罗马数字的构造规则
#3、V 和X 左边的小数字只能用Ⅰ。4、L 和C 左边的小数字只能用X。5、D 和M 左边的小数字只能用C。
#所以给定的字符串 从第二个数字开始遍历，判断是不是独立的情况，是独立的情况则把前面的数字加入sum，
#同时指针向下移动一位；若不是独立的情况，则将指针当前指向的位置减去前面一个位置的数字，加入sum，同时指针
#要向后移动2位。到最后一个元素时，会出现最后一个元素独立的情况，会出现异常，需要在异常中加上最后一个元素

class Solution:
    # @return an integer
    trans = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
    def romanToInt(self, s):
        sum,i = 0,1
        dependent = True
        if len(s) == 1:
            return self.trans[s[0]]
        while i <= len(s):
            try:
                if self.judge_dependent(s,i):
                    sum += self.trans[s[i-1]]
                    i +=1
                elif not self.judge_dependent(s,i):
                    sum += self.trans[s[i]] - self.trans[s[i-1]]
                    i += 2
            except:
                return sum+self.trans[s[-1]]
        return sum
    def judge_dependent(self,s,i):
        if (s[i] in 'VX' and s[i-1]=='I') or (s[i] in 'LC' and s[i-1]=='X') or (s[i] in 'DM' and s[i-1]=='C') :
                return  False
        else:
            return  True