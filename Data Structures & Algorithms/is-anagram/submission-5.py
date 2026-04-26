class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): 
            return False
        
        # char_freq_s = {}
        # char_freq_t = {}
        # for char in s:
        #     if char in char_freq_s : 
        #         char_freq_s[char] += 1
        #     else:
        #         char_freq_s[char] = 1
        
        # for char in t:
        #     if char in char_freq_t : 
        #         char_freq_t[char] += 1
        #     else:
        #         char_freq_t[char] = 1

        # print(char_freq_t)
        # print(char_freq_s)
        # if(char_freq_t == char_freq_s):
        #     print("true")
        #     return True
        # else:
        #     print("farue")
        #     return False

        s_list = [char for char in s]
        t_list = [char for char in t]
        len1 = len(s_list)
        for char in s:
            if(char in t_list):
                t_list.remove(char)
            else:
                continue  

        if(len(t_list) == 0):
            return True
        else:
            return False


