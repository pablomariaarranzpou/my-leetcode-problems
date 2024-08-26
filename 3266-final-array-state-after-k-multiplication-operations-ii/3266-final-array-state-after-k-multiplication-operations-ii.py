class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1: 
            return nums
        
        MOD = 10 ** 9 + 7
        n = len(nums)
        
        # Initialize the heap with values and their indices
        heap = [[x, i] for i, x in enumerate(nums)]
        heapify(heap)
        count = [0] * n

        # Perform the heap operations
        while k and heap[0][0] <= 1e9:
            k -= 1
            num, i = heappop(heap)
            count[i] += 1
            heappush(heap, [num * multiplier, i])
        
        # Calculate the number of complete rounds and the remainder
        q, r = divmod(k, n)
        heap.sort()
        
        for ix, (num, i) in enumerate(heap):
            count[i] += q + (ix < r)
        
        # Apply the multiplications to each element in nums
        for i, c in enumerate(count):
            nums[i] *= pow(multiplier, c, MOD)
            nums[i] %= MOD
        
        return nums
