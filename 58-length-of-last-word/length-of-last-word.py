class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split()
        y=len(x)
        z=x[y-1]
        count=0
        for i in z:
            count+=1
        return count
        