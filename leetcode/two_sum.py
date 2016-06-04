#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].



class Solution(object):
    def twoSum(self, nums, target):
        # WRONG, because element in nums, which is the key in map can be duplicate:   [0,4,3,0] target = 0 or 7
        # map = {}
        # for i in range(len(nums)):
        #     map[nums[i]] = i
                
        # print map
        # for key in map:
        #     if target-key in map:
        #         return [map[key],map[target-key]]
        #     else:
        #         pass
        # map = {}
# idea, use a dict map store target-nums[i]: i, i is nums[i]'s index, once a nums[i] in map, then ith element in nums is target-k(processed before), return[k's index, nums[i]'s index] = [map[num[i]],i]
# thinking the tricky part it check a key in map is O(1) but check a element in list is O(n), so the basic idea:
#   each k in nums, check if taget - i in the list -  i, will cost O(n) in each iterate, use the map in the way below is smarter
# when using map, remember if value of key will cause duplicate issue, here because it says:"each input would have exactly one solution", so we are sure that
#   although there might be duplicate value in the nums but, those number can't be in the answer, so the duplicate is fine here.
        for i in range(len(nums)):
            if nums[i] in map:
                return[map[nums[i]],i]
            else:
                map[target-nums[i]] = i
     
