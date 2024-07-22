class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        sortede = sorted(zip(heights, names), reverse=True)
        res = []
        for i in sortede:
            res.append(i[1])
            
        return res
        