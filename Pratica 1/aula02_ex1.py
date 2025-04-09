# AFD 𝑀4 que reconheça 𝐿4 = {𝑏𝑎^𝑛𝑏𝑎 ∣ 𝑛 ≥ 0}

# Definindo transições
transicoes = {
    ('q0', 'a'): 'T',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'T',
    ('q3', 'a'): 'T',
    ('q3', 'b'): 'T',
    ('T', 'a'): 'T',
    ('T', 'b'): 'T'
}

q0 = 'q0'
F = {'q3'}

def afd(palavra):
    estado_atual = q0
    for simbolo in palavra:
        estado_atual = transicoes[(estado_atual, simbolo)]
    return estado_atual in F

# Testes
print(afd('baba'))  # True
print(afd('bba'))  # True
print(afd('ababab'))  # False
print(afd('bbbb'))  # False
print(afd('babaa'))  # False 
