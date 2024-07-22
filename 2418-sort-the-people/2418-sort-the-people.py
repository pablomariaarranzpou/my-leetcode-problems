class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [item[1] for item in sorted(zip(heights, names), reverse=True)]
        