from collections import deque
def eh_palindromo(string):
    string = ''.join(string.split()).lower()
    pilha = deque()
   
    meio = len(string) // 2
    for i in range(meio):

        pilha.append(string[i])
    

    if len(string) % 2 != 0:
        meio += 1
    for i in range(meio, len(string)):
        if pilha.pop() != string[i]:
            return False

    return True
string = input("Texto: ")
if eh_palindromo(string):
    print("O textp é um palíndromo.")
else:
    print("O texto não é um palíndromo.")
