class Solution:
    def majorityElement(self, nums):
        d={}
        for y in nums:
            if y in d:
                d[y]+=1
            else:
                d[y]=1
        return max(d,key=d.get)
        