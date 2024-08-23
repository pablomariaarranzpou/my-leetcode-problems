from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        symbols = {'+', '-'}
        i = 0
        
        denoms = []
        divs = []
        
        while i < len(expression):
            denom = ""
            div = ""
            
            
            if expression[i] in symbols:
                denom += expression[i]
                i += 1
            
            while i < len(expression) and expression[i] != '/':
                denom += expression[i]
                i += 1
            
            i += 1 
            
            
            while i < len(expression) and expression[i] not in symbols:
                div += expression[i]
                i += 1
            
            denoms.append(denom)
            divs.append(div)
        
        
        numerador_resultado = int(denoms[0])
        denominador_resultado = int(divs[0])

        for i in range(1, len(denoms)):
            denominador_comun = denominador_resultado * int(divs[i])
            numerador_resultado = numerador_resultado * int(divs[i]) + int(denoms[i]) * denominador_resultado
            denominador_resultado = denominador_comun
            
            
        factor_comun = gcd(numerador_resultado, denominador_resultado)
        numerador_resultado //= factor_comun
        denominador_resultado //= factor_comun
        
        return f"{numerador_resultado}/{denominador_resultado}"

                
                