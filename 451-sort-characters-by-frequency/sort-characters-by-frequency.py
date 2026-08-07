class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        ans=""
        while d:
            max_ch=max(d,key=d.get)
            ans+=max_ch*d[max_ch]
            del d[max_ch]
        return ans