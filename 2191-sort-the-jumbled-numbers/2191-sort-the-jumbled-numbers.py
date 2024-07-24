class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        

        mapped_nums = [(self.map_number(num, mapping), index, num) for index, num in enumerate(nums)]

        mapped_nums.sort(key=lambda x: (x[0], x[1]))

        return [num[2] for num in mapped_nums]
    
    def map_number(self, num: int, mapping) -> int:
        mapped_digits = [str(mapping[int(digit)]) for digit in str(num)]
        return int("".join(mapped_digits))
        