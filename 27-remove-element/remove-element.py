class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for x in nums:
            if x != val:
                nums[c]=x
                c+=1
        return c