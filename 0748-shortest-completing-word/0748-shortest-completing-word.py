class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
       
        licensePlate = [a.lower() for a in licensePlate if a.isalpha()]
        
        plate_counter = Counter(licensePlate)

        def can_complete(word: str) -> bool:
            word_counter = Counter(word)
            for letter, count in plate_counter.items():
                if word_counter[letter] < count:
                    return False
            return True
        shortest_word = None
        for word in words:
            if can_complete(word):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word

                    
                    