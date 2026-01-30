class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pilha = []
        pares = {
            ')':'(',
            '}': '{',
            ']': '['
        }

        for c in s:
            print(c)
            if c in '([{':
                print("Entrou no If:")
                pilha.append(c)
            elif c in ')]}':
                print(c)
                if not pilha or pilha.pop() != pares[c]:
                    return False
        
        print(pilha)
        return not pilha


text = input("Insira os parêntesis: \n> ")

solution = Solution()
resultado = solution.isValid(text)

print(resultado)