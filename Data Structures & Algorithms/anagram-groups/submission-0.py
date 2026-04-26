class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26 # a.....z

            for char in s:
                count[ord(char) - ord("a")] += 1
            print(count, tuple(count))
            res[tuple(count)].append(s)
        
        return list(res.values())