class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0  # Initialize with 0 for XOR operation

        for i in range(len(nums)):
            temp ^= nums[i]  # XOR operation to find the single number
        return temp 
        