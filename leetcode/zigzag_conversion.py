class Solution(object):
## this method is come from: write a example to find the relationship of the index
##    of each letter appear in each line of the zigzag string: then just apply
##    the math, this is not a good way, so the pattern is: 
##    0 line and last line, each letter have 2(numRows - 1) index distance
##    other line: each letter's distance is: (if innitial_value = 2, 2(numRows-1)=6): 
##    2, |2-6|, |4-6|...., so it is 2, 4, 2, 4 exist alternately
    def convert(self, s, numRows):
        if len(s) <= numRows or numRows == 1:
            return s
        else:
            zigzag = ''
            index = 0
            while index < len(s):
                zigzag = zigzag + s[index]
                index += 2*(numRows-1)
            for i in range(1,numRows-1):
                index = i
                zigzag += s[index]
                weight = 2*(numRows-1-i)
                while index + weight < len(s):
                    index += weight
                    zigzag += s[index]
                    weight = abs(weight - 2*(numRows-1))
            index = numRows-1
            while index < len(s):
                zigzag += s[index]
                index += 2*(numRows-1)
            return zigzag


## way 2 fatser than above
## way 2 mock how the string will be parse exactly like the zigzag, the tricky
##    part is how to convert the zigzag route to the index (the line 0,1,2...) 
##    of which line letter belong to: the idea it once the index hit 0 set it to
##    go down (step = -1), once index hit nowRows-1 set it to go up (step = 1)
# 2.1
    def convert2_1(self, s, numRows):
        if len(s) < numRows or numRows == 1:
            return s
        index, step, L = 0, 1, ['']*numRows
        for l in s:
            L[index] += l
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)

    def convert2_2(self, s, numRows):
        step = (numRows == 1) - 1  # 0 or -1  when boolean compare/ do the algebra to int false == 0 true ==1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1: 
                step = -step  #change direction  
            idx += step
        return ''.join(rows)


x = Solution()
print x.convert('PAYPALISHIRING',4)
print x.convert2_1('PAYPALISHIRING',4)                  
