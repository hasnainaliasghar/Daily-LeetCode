class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            n = -n

        if n <= 999:
            return 0

        total = 0
        d = 4
        while 10 ** (d - 1) <= n:
            lower = 10 ** (d - 1)
            upper = min(n, 10 ** d - 1)
            count_in_this_range = upper - lower + 1
            commas_per_number = (d - 1) // 3
            total += count_in_this_range * commas_per_number
            d += 1

        return total