class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forw = [1]
        back = [1]

        for i in range(1,n):
            forw.append(forw[i-1] * nums[i-1])
            back.append(back[i-1] * nums[-i])
        
        back = list(reversed(back))

        return [forw[i] * back[i] for i in range(n)]
        
