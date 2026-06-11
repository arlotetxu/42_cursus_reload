"""
Escribe una función que encuentre el número mínimo de cortes necesarios para
dividir una cadena de forma que cada subcadena resultante sea un palíndromo.

Declaración:
def palindrome_partitioner(s:str) -> int:

La función debe:
-Encontrar el número mínimo de cortes para que todas las partes sean palíndromos
- Devolver el número de cortes necesarios (no el número de partes)
- Manejar cadenas vacías
- Los caractéres individuales se consideran palíndromos
- La comprobación es sensible a mayúsculas y minúsculas

Ejemplos:
"aab" -> 1 "aa | b"
"aba" -> 0 ya es palíndromo
"abcba" -> 0 ya es palíndromo
"abcd" -> 3 "a"|"b"|"c"|"d"
"aabaa" -> 0 ya es palíndromo
"abac" -> 1 "aba"|"c"
"" -> 0
"""

# def palindrome_partitioner(s:str) -> int:
#     if not s:
#         return 0
#     cut = [x for x in range(-1, len(s))]
#     for i in range(0, len(s)):
#         for j in range(i, len(s)):
#             if s[i:j] == s[j:i:-1]:
#                 cut[j+1] = min(cut[j+1], cut[i]+1)
#     return cut[-1]



def palindrome_partitioner(s: str) -> int:
    if not s:
        return 0
    
    n = len(s)
    # Lista donde dp[i] guardará los cortes para s[:i]
    dp = [0] * (n + 1)
    
    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    
    # Vamos evaluando la palabra poco a poco, de 1 letra hasta 'n' letras
    for i in range(1, n + 1):
        
        # Si la palabra completa hasta 'i' ya es palíndromo, necesitamos 0 cortes.
        if is_palindrome(s[:i]):
            dp[i] = 0
        else:
            # En el peor de los casos, hacemos un corte entre cada letra
            min_cortes = i - 1 
            
            # Buscamos un punto de corte 'j' anterior a 'i'
            for j in range(1, i):
                # Si la parte derecha del corte (de j a i) es palíndromo...
                if is_palindrome(s[j:i]):
                    # ...los cortes totales son: (cortes que ya necesitábamos para llegar a j) + 1
                    min_cortes = min(min_cortes, dp[j] + 1)
                    
            dp[i] = min_cortes
            
    return dp[n]

print(palindrome_partitioner("aab"))
# print(palindrome_partitioner("aba"))
# print(palindrome_partitioner("abcba"))
# print(palindrome_partitioner("abcd"))
# print(palindrome_partitioner("aabaa"))
# print(palindrome_partitioner("abac"))
# print(palindrome_partitioner(""))