class Solution(object):
    def checkRecord(self, s):
        if s.count("A") <2 and "LLL" not in s:
            return True
        else:
            return False
        