class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        minimum = float('inf')
        hashmp = {}
        for index, card in enumerate(cards):
            
            if card in hashmp.keys():
                
                if index - hashmp[card][-1] < minimum:
                    minimum = index - hashmp[card][-1]
                
                hashmp[card].append(index)
            else:
                
                hashmp[card] = [index]
        
        
        """
        for key in hashmp.keys():
            
            appaerences = hashmp[key]
            if len(appaerences) > 1:
                
                for aparition in range(len(appaerences) - 1):
                    #print(appaerences[aparition + 1], "-", appaerences[aparition])
                    if appaerences[aparition + 1] - appaerences[aparition] < minimum:
                        minimum = appaerences[aparition + 1] - appaerences[aparition]
        """
        if minimum == float('inf'):
            return -1
        else:
            return minimum + 1
        