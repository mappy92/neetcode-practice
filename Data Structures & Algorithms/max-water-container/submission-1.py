class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                h = min(heights[i], heights[j])
                d = j-i
                #print("Indexes :  ", i,j)
                #print("Heights at this point : ",heights[i], heights[j])
                print("H Min an D values are : ", h,d, "Cuurent area :", h*d)
                max_area = max(max_area, h*d)
                #print("Max area after ::",j," inner iteration :", max_area)
            print("max area after",i+1,"iteration",max_area)
        return max_area

