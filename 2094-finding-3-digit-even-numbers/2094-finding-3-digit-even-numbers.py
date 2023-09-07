class Solution:
    from itertools import combinations
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        a = list(set(permutations(digits, 3)))
        
        convert_to_integer = lambda combo: int(''.join(map(str, combo)))

        integer_combinations = list(map(convert_to_integer, a))
        
        print(integer_combinations)

        filter_even = lambda x: x % 2 == 0 and len(str(x)) > 2

        even_integer_combinations = list(filter(filter_even, integer_combinations))

        return sorted(even_integer_combinations)
        
