class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 : O(n*n)
        # num_len = len(nums)
        # for i in range(0,num_len-1):
        #     for j in range(i+1,num_len): 
        #         if(nums[i]+nums[j] == target):
        #             return [i,j]
        prevmap = {}

        for i,n in enumerate(nums):
            search_key = target-n
            if(search_key in prevmap):
                return [prevmap[search_key],i]
            prevmap[n] = i
                