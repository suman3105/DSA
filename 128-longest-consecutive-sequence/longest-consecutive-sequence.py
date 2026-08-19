class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        l=1
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            elif nums[i]!=nums[i-1]:
                count=1
            l=max(l,count)
        return l
        