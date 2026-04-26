class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l, r = 0, 1
        # curr_max_l = 1
        # res = 0
        # while r < len(s):
        #     print("l and r, k values : ", l, r, k)
        #     print("char values : ", s[l], s[r])
        #     if(s[l] == s[r]):
        #         r += 1
        #         curr_max_l += 1
        #     elif(s[l] != s[r] and k > 0):
        #         k -= 1
        #         r += 1
        #         curr_max_l += 1
        #     elif(s[l] != s[r] and k == 0):
        #         l += curr_max_l
        #         r = l + 1
        #         res = max(res, curr_max_l)
        #         curr_max_l = 0
        # return max(curr_max_l, res)
        # standard O(26*n)
        count ={}
        res = 0
        
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while ((r - l + 1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l +1)
        return res

            
        