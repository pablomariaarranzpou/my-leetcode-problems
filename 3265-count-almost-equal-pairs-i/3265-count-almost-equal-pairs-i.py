class Solution:
    def countPairs(self, nums: List[int]) -> int:
        
        def check(num1, num2):
        
            s_num1 = str(num1)
            s_num2 = str(num2)
            
            while len(s_num1) > len(s_num2):
                
                s_num2 = '0' + s_num2
            
            while len(s_num1) < len(s_num2):
                s_num1 = '0' + s_num1
                
                
            diff_1 = -1
            diff_2 = -1
            
            count_diff = 0
            
            for i in range(len(s_num1)):
                
                if s_num1[i] != s_num2[i]:
                    
                    count_diff += 1
                    
                    if count_diff == 1:
                        diff_1 = i
                        
                    elif count_diff == 2:
                        diff_2 = i
                        
                    else:
                        return False
                    
                    
            if count_diff == 2:

                lista = list(s_num1)
                lista[diff_1], lista[diff_2] = lista[diff_2], lista[diff_1]
                s_num1 = "".join(lista)
            
            return s_num1 == s_num2
    
        c = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                if check(nums[i], nums[j]) or nums[i] == nums[j]:
                    c += 1
                    
        return c
                    
            
                    
                
                