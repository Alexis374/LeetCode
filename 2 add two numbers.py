'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        num1= self.getNum(l1)
        num2 = self.getNum(l2)
        print num1+num2
        return self.buildListNode(num1+num2)
    
    def getNum(self,listnode):
        i,result=1,0
        end=False
        while not end:
            result +=listnode.val*i
            i*=10
            if not listnode.next:
                end = True
            listnode = listnode.next
        return result
    def buildListNode(self,num):
        ln = ListNode(num%10)
        start = ln
        num/=10
        while num>0:
            ln.next = ListNode(num%10)
            ln = ln.next
            num/=10
        return start

    def printlistnode(self,ln):
        end =False
        while not end:
            print ln.val,
            if not ln.next:
                end = True
            ln=ln.next

if __name__ == '__main__':
    # l1 = ListNode(9)
    # l1.next = ListNode(9)
    # l2 = ListNode(1)
    s = Solution()
    # s.addTwoNumbers(l1,l2)
    ln = s.buildListNode(100)
    s.printlistnode(ln)