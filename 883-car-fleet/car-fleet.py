class Solution(object):
    def carFleet(self, target, position, speed):
        y=[]
        count=0
        last=0
        for i in range(len(position)):
            x=(target-position[i])/float(speed[i])
            y.append([position[i],x])
        y.sort(reverse=True)
        for pos,t in y:
            if t>last:
                count+=1
                last=t
        return count

