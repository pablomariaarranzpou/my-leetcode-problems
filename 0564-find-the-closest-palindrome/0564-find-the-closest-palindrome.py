class Solution:
    def mirror_left_to_right(self, number: int) -> int:
        number_str = str(number)
        length = len(number_str)
        left_idx, right_idx = (length - 1) // 2, length // 2
        mirrored_list = list(number_str)
        while left_idx >= 0:
            mirrored_list[right_idx] = mirrored_list[left_idx]
            right_idx += 1
            left_idx -= 1
        return int("".join(mirrored_list))

    def find_smaller_palindrome(self, number: int) -> int:
        low, high = 0, number
        closest_palindrome = float("-inf")
        while low <= high:
            mid = (high - low) // 2 + low
            candidate_palindrome = self.mirror_left_to_right(mid)
            if candidate_palindrome < number:
                closest_palindrome = candidate_palindrome
                low = mid + 1
            else:
                high = mid - 1
        return closest_palindrome

    def find_larger_palindrome(self, number: int) -> int:
        low, high = number, int(1e18)
        closest_palindrome = float("-inf")
        while low <= high:
            mid = (high - low) // 2 + low
            candidate_palindrome = self.mirror_left_to_right(mid)
            if candidate_palindrome > number:
                closest_palindrome = candidate_palindrome
                high = mid - 1
            else:
                low = mid + 1
        return closest_palindrome

    def nearestPalindromic(self, number_str: str) -> str:
        number = int(number_str)
        smaller_palindrome = self.find_smaller_palindrome(number)
        larger_palindrome = self.find_larger_palindrome(number)
        if abs(smaller_palindrome - number) <= abs(larger_palindrome - number):
            return str(smaller_palindrome)
        return str(larger_palindrome)
        