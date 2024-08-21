class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        minimum = float('inf')
        hashmp = {}
        for index, card in enumerate(cards):
            if card in hashmp:
                calc = index - hashmp[card]
                if calc < minimum:
                    minimum = calc
                hashmp[card] = index
            else:
                hashmp[card] = index
        
        if minimum == float('inf'):
            return -1
        else:
            return minimum + 1
        