class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        outputs = set()

        for m in range(1, n - 1):
            l, r = 0, n - 1
            while l < m and m < r:
                if nums[l] + nums[m] + nums[r] < 0:
                    l += 1
                elif nums[l] + nums[m] + nums[r] > 0:
                    r -= 1
                else:
                    outputs.add((nums[l], nums[m], nums[r]))
                    l += 1
        
        return [[num for num in output] for output in outputs]