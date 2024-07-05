class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count=1
        for num in range(1,len(nums)):
            if nums[num] != nums[num-1]:
                nums[count] = nums[num]
                count+=1
        return count
            
