class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        temp = num;
        while(temp * temp > num):
            temp = (temp + (num/temp)) // 2;
        return temp * temp == num;
