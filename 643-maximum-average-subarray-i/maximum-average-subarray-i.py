class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_arr=sum(nums[:k])
        max_sum=sum_arr
        for i in range (k,len(nums)):
            sum_arr+=nums[i]
            sum_arr-=nums[i-k]
            max_sum=max(max_sum,sum_arr)
        return max_sum / k