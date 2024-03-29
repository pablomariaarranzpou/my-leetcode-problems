class Solution:
    def isUgly(self, n: int) -> bool:
       # Un número debe ser mayor que 0 para ser considerado feo
        if n <= 0:
            return False
        # Dividir n repetidamente por 2, 3, y 5 mientras sea posible
        for i in [2, 3, 5]:
            while n % i == 0:
                n /= i
        # Si el resultado final de las divisiones es 1, el número es feo
        return n == 1
            

                    
                    
        