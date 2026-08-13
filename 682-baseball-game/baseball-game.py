class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for x in operations:
            if x  not in ["C", "D", "+"]:
                st.append(int(x))
            elif x=="C":
                st.pop()
            elif x=="D":
                st.append((st[-1]*2))
            elif x=="+":
                st.append((st[-1]+st[-2]))
        
        return sum(st)