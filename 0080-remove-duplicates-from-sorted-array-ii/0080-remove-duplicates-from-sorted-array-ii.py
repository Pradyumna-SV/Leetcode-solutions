class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for x in nums:
            if i==0 or i==1 or nums[i - 2] != x:
                nums[i] = x
                i+=1
        return i