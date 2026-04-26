class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_dict = defaultdict(int)
        # for num in sorted(nums) : 
        #     count_dict[num] += 1
        # print(count_dict)
        # sorted_desc = dict(sorted(count_dict.items(),key=lambda item: item[1], reverse=True))
        # print(sorted_desc)
        # sorted_desc_keys = list(sorted_desc.keys())
        # top_k = []
        # for i in range(k):
        #     top_k.append(sorted_desc_keys[i])
        
        # return top_k
        count = {}
        freq=[[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res
                 


          

        


        
        