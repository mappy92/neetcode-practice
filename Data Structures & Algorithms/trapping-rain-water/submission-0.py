class Solution:
    def trap(self, height: List[int]) -> int:
        # #max, secondmax
        # h_len = len(height)
        # max_water = 0
        # i = 1
        # while i < h_len:
        #     curr_heights = height[:i+1]
        #     print(curr_heights)
        #     curr_maxh = max(curr_heights)
        #     second_maxh = sorted(set(curr_heights))[-2] # can be equal
            
        #     # ignore and move to next if second_maxh is zero
        #     # find the index of both
        #     # for loop from lower index to higher 
        #     # keep the count of drops that can hold with each iteration
        #     # then move to next block where the max value was
        #     if(second_maxh == 0):
        #         i += 1 
        #         continue
            
        #     max_index = height.index(curr_maxh)
        #     max2_index = height.index(second_maxh)
            
        #     area = 0
        #     start_idx = min(max_index, max2_index)
        #     end_idx = max(max_index, max2_index)
        #     print(f"curr_maxh: {curr_maxh}, max2_index: {max2_index}")
        #     print(f"start_idx: {start_idx}, end_idx: {end_idx}")
        #     for i in range(start_idx, end_idx):
        #         current_bar = height[i]
        #         print(f"Index: {i}, Height: {current_bar}")
        #         area += (second_maxh - current_bar)
        #         print(f"current area:{area}")
        #     max_water += area
        #     i = end_idx
        # return max_water
        if not height: return 0

        l,r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else :
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res





