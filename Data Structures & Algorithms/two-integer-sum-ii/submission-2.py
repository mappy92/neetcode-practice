class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # prevmap = {}

        # for i,n in enumerate(numbers):
        #     search_key = target-n
        #     if(search_key in prevmap):
        #         return [prevmap[search_key]+1,i+1]
        #     prevmap[n] = i
        # sorted => non-decreasing increasing order 
        l, r = 0, len(numbers)- 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if(sum == target):
                return([l+1, r+1])
            elif (sum > target):
                    r = r - 1
            else:
                    l = l + 1



