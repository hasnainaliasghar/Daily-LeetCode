class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = x*sign
        else:
            sign = 1
        v = 0
        while x != 0:
            v = v * 10 + x % 10
            x = x / 10

        if v > 2**31 or v < -2**31:
            return 0
        else: 
            return v * sign
