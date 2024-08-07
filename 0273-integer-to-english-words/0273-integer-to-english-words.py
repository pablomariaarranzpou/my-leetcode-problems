class Solution:
    
    def __init__(self):
        self.word = ""
        
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"
        
        if num == 1:
            return "One"
        
        nums = {
            1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
            9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
            13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen"
        }
        
        dic = {20: "Twenty", 30: "Thirty", 40: "Forty",
            50: "Fifty", 60: "Sixty", 70: "Seventy",
            80: "Eighty", 90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }
        dic_keys = sorted(dic.keys(), reverse=True)
        
        
        def auxiliar_function(num, word):
            
            if num == 0:
                pass  
            elif num in nums.keys():
                self.word += " " + nums[num]
            else:
            
                for div in dic_keys:
                    
                    if num / div < 1:
                        continue
                    elif div >= 100:
                        calc = num // div
                        mod = num % div
                        auxiliar_function(calc, self.word)
                    else:
                        mod = num - div
                    self.word += " " + dic[div] 
                    auxiliar_function(mod, self.word)
                    break
                                  
        auxiliar_function(num, self.word)
        
        return self.word[1:]
        
        
            
        
            
                    
            
            
                    
            
                    
                    
            
        
        