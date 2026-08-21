class Solution(object):
    def intersect(self, nums1, nums2):
        z=[]
        for x in nums1:
            if x in nums2:
                z.append(x)
                nums2.remove(x)
        return z
        