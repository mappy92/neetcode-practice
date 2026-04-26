class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []
        lessFound = False
        for i in range(len(temperatures)):
            lessFound = False
            for j in range(i+1,len(temperatures)):
                if(temperatures[j] > temperatures[i]):
                    temp.append(j - i)
                    lessFound = True
                    break
            if(not lessFound):
                temp.append(0)
        return temp