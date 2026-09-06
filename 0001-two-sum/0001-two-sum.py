class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        index = 0
        for i in nums:
            compliment = target - i
            if compliment in seen:
                return [seen[compliment], index]
            seen[i] = index
            index+=1
