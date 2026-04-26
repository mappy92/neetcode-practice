from itertools import permutations
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1

        while r <= len(s2) - 1:
            substr = s2[l:r+1]
            # all substrings from this s2 substring 
            #substr_list = [''.join(p) for p in permutations(substr, len(s1))]
            if Counter(s1) == Counter(substr) :
                return True

            l += 1
            r += 1
        return False