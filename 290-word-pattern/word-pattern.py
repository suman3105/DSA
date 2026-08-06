class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st1={}
        st2={}
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for i in range (len(pattern)):
            a=pattern[i]
            b=words[i]
            if a in st1 and st1[a]!=b:
                return False
            if b in st2 and st2[b]!=a:
                return False
            st1[a]=b
            st2[b]=a
        return True
        