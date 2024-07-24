class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num: int) -> int:
            mapped_digits = [str(mapping[int(digit)]) for digit in str(num)]
            return int("".join(mapped_digits))

        mapped_nums = [(map_number(num), index, num) for index, num in enumerate(nums)]

        mapped_nums.sort(key=lambda x: (x[0], x[1]))

        return [num[2] for num in mapped_nums]

        return res
        