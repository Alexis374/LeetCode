'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

主要思想就是每次取出第一位和最后一位，进行比较

'''



def get_len(x):
	num_len=1
	div=10
	while x/div:
		num_len+=1
		x/=10
	return num_len

def isPalindrome(x):
    if x<0:
        return False
    elif x<10:
        return True
    else:
    	num_len = get_len(x)
        while x>0:
            last = x%10
            first = x/(10**(num_len-1))
            if last!=first:
                return False
            else:
                x=x-last
                x/=10
                x=x-last*(10**(num_len-2))
                num_len -=2
        return True

if __name__=='__main__':
	print isPalindrome(1221)
	print isPalindrome(234432)
	print isPalindrome(20502)
	print isPalindrome(112344566543211)