class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.nums = sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        
        self.nums.append(val)
        
        mod = sorted(self.nums, reverse=True)
        return mod[self.k - 1]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)