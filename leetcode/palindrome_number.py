class Solution(object):

# reverse the integer then compare it to the origin: straigt forward
    def isPalindrome_1(self, x):
        if x < 0:
            return False
        origin = x
        rev_num = 0
        while True:
            rev_num = rev_num*10 + x%10
            x = x//10
            if x == 0:
                break
        return rev_num == origin

#  check 2 side left and right in one iterate
    def isPalindrome_2(self, x):
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div = div * 10
            
        while x:
            left = x / div
            right = x % 10
            
            if left != right:
                return False
            
            x = ( x % div ) / 10
            div = div / 100
        return True
