class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        s=[]
        for a in asteroids:
            while s and s[-1]>0 and a<0 and s[-1]<-a:
                s.pop()
            if s and s[-1]>0 and a<0:
                if s[-1]==-a:
                    s.pop()
                continue
            s.append(a)
        return s
        