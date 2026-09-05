class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []
        for c in s:
            if c in map.values():
                stack.append(c)
            elif c in map:
                if not stack or stack.pop() != map[c]:
                    return False
        return len(stack) == 0