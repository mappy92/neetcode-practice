class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # Solution 1 : 
        # count = Counter(nums)
        # is_duplicate = False
        # for key,value in count.items():
        #     if(value >= 2):
        #         is_duplicate = True
        # return is_duplicate
        
        # is_duplicate = False
        # sorted_nums = sorted(nums)
        # for i in range(len(sorted_nums)-1):
        #     if(sorted_nums[i] == sorted_nums[i+1]):
        #         is_duplicate = True
        # return is_duplicate

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False        
            
