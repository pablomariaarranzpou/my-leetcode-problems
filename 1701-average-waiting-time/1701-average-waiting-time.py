class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        total = customers[0][1] + customers[0][0]
        calc = customers[0][1]
        
        for i in range(1, len(customers)):
            if(total < customers[i][0]):
                calc += customers[i][1]
                total = (customers[i][1] + customers[i][0])
                
            else:
                calc += (total - customers[i][0] + customers[i][1])
                total += customers[i][1]
                
                
 
        return calc / len(customers)
            