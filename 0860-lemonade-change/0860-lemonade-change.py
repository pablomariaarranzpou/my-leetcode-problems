class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five = ten = 0
        for bill in bills:
            
            #print("Bill",bill, "five", five, "ten", ten)
            
            if bill == 5:
                five += 1
                
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            elif bill == 20:
                
                if (ten == 0):
                    if (five < 3):
                        return False
                    else:
                        five -= 3
                else:
                    if five == 0:
                        return False
                    else:
                        ten -= 1
                        five -= 1

                
        return True
                
                
                
            
            

