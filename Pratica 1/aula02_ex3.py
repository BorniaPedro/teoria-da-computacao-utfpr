# AFD 𝑀6 que reconheça 𝐿6 = {𝑤 ∈ {𝑎, 𝑏}∗ ∣ (|𝑤|𝑎 + |𝑤|𝑏) mod 2 = 0}

# Definindo transições
transicoes = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q0'
}

q0 = 'q0'
F = {'q0'}

def afd(palavra):
    estado_atual = q0
    for simbolo in palavra:
        estado_atual = transicoes[(estado_atual, simbolo)]
    return estado_atual in F

# Testes
print(afd('ab'))  # True
print(afd('aaa'))  # False
print(afd('aba'))  # False
print(afd('abba'))  # True
print(afd('bababa'))  # True 