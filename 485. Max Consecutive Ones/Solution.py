class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi, temp = 0, 0
        for num in nums:
            if num != 0:
                maxi += 1
                if maxi > temp:
                    temp = maxi
            else:
                maxi = 0
        return temp