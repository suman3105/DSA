class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)
        d=set()
        for y in nums2:
            if y in x:
                d.add(y)
        return list(d)
        