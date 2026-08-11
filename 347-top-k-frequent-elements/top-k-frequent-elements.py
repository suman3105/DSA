class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        z={}
        for x in nums:
            z[x]=z.get(x,0)+1
        ans=[]
        while z:
            maxch=max(z,key=z.get)
            ans.append(maxch)
            del z[maxch]
        y=[]
        for i in range (k):
            y.append(ans[i])
        return y
