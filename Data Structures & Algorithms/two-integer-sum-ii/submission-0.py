class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevmap = {}

        for i,n in enumerate(numbers):
            search_key = target-n
            if(search_key in prevmap):
                return [prevmap[search_key]+1,i+1]
            prevmap[n] = i