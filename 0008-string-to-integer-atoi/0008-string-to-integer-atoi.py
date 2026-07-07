class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()

        if not s:
            return 0

        index = 0
        sign = 1
        if s[0] == "-":
            sign = -1
            index += 1
        elif s[0] == "+":
            sign = 1
            index += 1
    

        cleaned = 0
        while index < len(s) and '0' <= s[index] <= '9':
            cleaned = cleaned * 10 + int(s[index])
            index += 1
        
        val = sign * cleaned

        INT_MIN, INT_MAX = -2147483648, 2147483647
        if val < INT_MIN:
            return INT_MIN
        if val > INT_MAX:
            return INT_MAX
            
        return val
        
        