class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
                
        for num in d:
            if d[num]==1:
                return num
        