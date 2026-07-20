class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            current_len = right - left + 1    
            max_len = max(max_len, current_len)

        return max_len