# AFD 𝑀7 que reconheça 𝐿7 = {𝑎^𝑚 𝑏^𝑛 ∣ 𝑚, 𝑛 ≥ 0 ∧ (𝑚 + 𝑛) mod 2 = 0}

# Definindo transições
transicoes = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q3',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'T',
    ('q2', 'b'): 'q3',
    ('q3', 'a'): 'T',
    ('q3', 'b'): 'q2',
    ('T', 'a'): 'T',
    ('T', 'b'): 'T'
}

q0 = 'q0'
F = {'q0', 'q2'}

def afd(palavra):
    estado_atual = q0
    for simbolo in palavra:
        estado_atual = transicoes[(estado_atual, simbolo)]
    return estado_atual in F

# Testes
print(afd('ab'))  # True
print(afd('aaa'))  # False
print(afd('aba'))  # False
print(afd('aaabbb'))  # True
