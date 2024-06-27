class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        edited = edges[:2]
        if(edited[0][0] == edited[1][0] or edited[0][0] == edited[1][1]):
            return edited[0][0]
        else:
            return edited[0][1]
            

        