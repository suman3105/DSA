class Solution:
    def maxArea(self, height: List[int]) -> int:
       l=0
       ans=0
       r=len(height)-1
       while l<r:
        z=(r-l)*min(height[l],height[r])
        ans=max(ans,z)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
       return ans

    
        