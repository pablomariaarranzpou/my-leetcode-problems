class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1map = defaultdict(int)
        for char in s1:
            s1map[char] += 1

        for i in range(len(s2) - len(s1) + 1):
            s2map = defaultdict(int)
            for j in range(len(s1)):
                s2map[s2[i + j]] += 1

            if self.matches(s1map, s2map):
                return True
        
        return False

    def matches(self, s1map: dict, s2map: dict) -> bool:
        for key in s1map:
            if s1map[key] != s2map.get(key, -1):
                return False
        return True