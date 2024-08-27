class LFUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}  
        self.freq_map = collections.defaultdict(collections.OrderedDict)

    def update_freq(self, key: int):
        value, freq = self.key_map[key]
        
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        freq += 1
        self.key_map[key] = (value, freq)
        self.freq_map[freq][key] = value

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        self.update_freq(key)
        return self.key_map[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_map:
            
            self.key_map[key] = (value, self.key_map[key][1])
            self.update_freq(key)
        else:
            if len(self.key_map) == self.capacity:
                
                evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
                del self.key_map[evict_key]
            
            self.key_map[key] = (value, 1)
            self.freq_map[1][key] = value
            self.min_freq = 1

            
            
            
            
        
            
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)