class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input and output is clear
        # UMPIRE - understand, match, plan, Implement, Review and Evaluate
        # Define constraints => no duplicate triplets 
        # Actions => Pseudocode and edge cases
        # Result => 
        # Alignment => spark vs pandas
        # communication
        # Body language
        # Time management
        # Conversational engagement
        #triplets = []
        # for i, num1 in enumerate(len(nums)-3) 
            # for j, num2 in enumerate(1,len(nums)-2)
                # for k, num3 in enumerate(2,len(nums)-1)
                    #if num1+num2+num3 = 0 : 
                        #list.append[num1, num2, num3]
        #nums = sorted(nums) 
        #print(nums)

        # # Two pointer solution               
        # l,r = 0, len(nums) -1
        # triplets = []
        # for i in range(len(nums)-1):
        #     l = i
        #     r = len(nums) - 1 - i
        #     sum = nums[l] + nums[r]
        #     print("sum",sum)
        #     for curr in range(l+1, r-1):
        #         print("num",nums[curr])
        #         if(nums[curr] + sum == 0):
        #           if sorted([nums[l],nums[curr],nums[curr]]) not in triplets:
        #             triplets.append([nums[l],nums[curr],nums[curr]])

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l,r = i + 1, len(nums) - 1 
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res