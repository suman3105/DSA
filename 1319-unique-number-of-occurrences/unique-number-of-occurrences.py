class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        s={}
        for x in arr:
            s[x]=s.get(x,0)+1
        freq=list(s.values())
        return len(freq)==len(set(freq))