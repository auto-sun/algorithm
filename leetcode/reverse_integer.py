class Solution(object):
    def reverse_2(self, x):
        value = abs(x)
        sign = -1 if x < 0 else 1
        rev = 0
        while True:
            digit = value % 10
            rev = rev*10 + digit
            value = value//10
            if value == 0:
                break
        return rev*sign*(rev<2**31)

    def reverse_3(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)

    def reverse_4(self, x):
        s = str(x)
        res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
        return res if -2147483648 <= res <= 2147483647 else 0

    def reverse_1(self, x):
        d, p = y//10,1
        while d >= 10:
            p += 1
            d = y//10**p
            print p, d

        t, rev = 0, 0
        print p
        while p >= 0:
            rev += (y//10**p) * 10**t
            print ('p is %r, y//10**P is %r, (y//10**p) * 10**t is %r'%(p,y//10**p,(y//10**p) * 10**t))
            y = y % 10**p
            p += -1
            t += 1
        if x < 0:
            return -rev
        return rev

a = Solution()
print a.reverse(-13234)
