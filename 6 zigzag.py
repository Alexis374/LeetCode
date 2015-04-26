'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

边界情况是 只有一行的时候。
其他情况是存哈希表
'''

def convert(s, numRows):
    result_dict = {}
    for i in range(numRows):
        result_dict[i]=[]
    print result_dict
    sign = 1
    index = 0
    for ch in s:
        if numRows==1:
            return s
        result_dict[index].append(ch)
        index+= sign
        if index == numRows:
            sign = -1
            index -= 2
        if index == -1:
            sign =1
            index = 1
    result = ''
    for i in range(numRows):
        result = result + ''.join(result_dict[i])
    return result

print convert('ab',1)