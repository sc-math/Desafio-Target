"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de
informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente
definida no código;
"""
def a_count(word):
    word = word.lower()
    print(word.count('a'))


string = str(input())
a_count(string)
