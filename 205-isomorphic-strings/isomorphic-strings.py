class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st1={}
        st2={}
        for i in range (len(s)):
            a=s[i]
            b=t[i]
            if a in st1 and st1[a]!=b:
                return False
            if b in st2 and st2[b]!=a:
                return False
            st1[a]=b
            st2[b]=a
        return True
        