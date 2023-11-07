class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        m = nums[0]
        for i in range(len(nums)):
            if count == 0:
                m = nums[i]
                count += 1
            elif m == nums[i]:
                count+=1
            else:
                count -= 1
        return m
        