class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {key: 0 for key in range(-1000, 1001)}
        for num in nums:
            frequencies[num] += 1
        
        return [pair[0] for pair in sorted(frequencies.items(), key = lambda x: x[1], reverse = True)[:k]]