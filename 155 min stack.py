'''


一个存放数字的栈，另一个存放当前最小值栈。难点在于pop时，pop的值是不是当前的最小值，如果是，需不需要在最小值栈里删除这个值？
要点是如果数值栈里还存在这这个最小值，就不删除，不存在就需要删除。 即第29行判断的条件。
'''

class MinStack:
    # @param x, an integer
    # @return an integer  	push(-2),push(0),push(-1),getMin,top,pop,getMin

    def __init__(self):
        self.stack = []
        self.minstack = []
        
        
    def push(self, x):
        self.stack.append(x)
        try:
            minval = self.getMin()
            if x<minval:
                self.minstack.append(x)
        except IndexError:
            self.minstack.append(x)

    # @return nothing
    def pop(self):
        p = self.stack.pop()
        if p <= self.getMin() and p not in self.stack:
            self.minstack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
    	# print self.minstack
    	# print self.stack
        if self.minstack:
            return self.minstack[-1]
        else:
            raise IndexError

if __name__ =='__main__':
	m = MinStack()
	# m.push(-2)
	# m.push(0)
	# m.push(-1)
	# m.getMin()
	# print m.top()
	# m.pop()
	# print m.stack,m.minstack
	# print m.getMin()
	m.push(0)
	m.push(1)
	m.push(0)
	print m.getMin()
	m.pop()
	print m.getMin()
