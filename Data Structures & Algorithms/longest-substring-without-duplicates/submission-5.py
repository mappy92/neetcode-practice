class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s_list = s.split("")
        #print(s_list)
        # l, r = 0, 1
        # max_l = 1
        # if len(s) > 0 :
        #     left_list =  [s[l]] 
        # else :
        #     return 0

        # while r < len(s):
        #     if(s[r] not in left_list):
        #         left_list.append(s[r])
        #         print(s[l], s[r], left_list)
        #         r += 1
        #         max_l += 1
                
        #     else: 
        #         l = r
        #     r += 1     
        # return max_l
        charSet  = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res 

