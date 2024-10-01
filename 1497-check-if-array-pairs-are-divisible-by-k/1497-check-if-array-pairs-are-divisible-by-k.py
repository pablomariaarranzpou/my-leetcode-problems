class Solution:
    def canArrange(self, arr, k):
        remainder_count = {}

        # Store the count of remainders in a map.
        for i in arr:
            remainder_count[(i % k + k) % k] = (
                remainder_count.get((i % k + k) % k, 0) + 1
            )

        for i in arr:
            rem = (i % k + k) % k

            # If the remainder for an element is 0, then the count of numbers that give this remainder must be even.
            if rem == 0:
                if remainder_count[rem] % 2 == 1:
                    return False

            # If the remainder rem and k-rem do not have the same count then pairs can not be made.
            elif remainder_count[rem] != remainder_count.get(k - rem, 0):
                return False
        return True        
            
                
        return False
        