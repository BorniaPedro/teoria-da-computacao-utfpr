# Considere Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} e defina autômatos finitos determinísticos para as seguintes linguagens: 
# AFD 𝑀9 que reconheça 𝐿9 = {𝑥 ∈ Σ∗ ∣ 𝑥 mod 5 = 0}

# Definindo transições
transicoes = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q2',
    ('q0', '2'): 'q2',
    ('q0', '3'): 'q2',
    ('q0', '4'): 'q2',
    ('q0', '5'): 'q1',
    ('q0', '6'): 'q2',
    ('q0', '7'): 'q2',
    ('q0', '8'): 'q2',
    ('q0', '9'): 'q2',
    
    ('q1', '0'): 'q1',
    ('q1', '1'): 'q2',
    ('q1', '2'): 'q2',
    ('q1', '3'): 'q2',
    ('q1', '4'): 'q2',
    ('q1', '5'): 'q1',
    ('q1', '6'): 'q2',
    ('q1', '7'): 'q2',
    ('q1', '8'): 'q2',
    ('q1', '9'): 'q2',

    ('q2', '0'): 'q1',
    ('q2', '1'): 'q2',
    ('q2', '2'): 'q2',
    ('q2', '3'): 'q2',
    ('q2', '4'): 'q2',
    ('q2', '5'): 'q1',
    ('q2', '6'): 'q2',
    ('q2', '7'): 'q2',
    ('q2', '8'): 'q2',
    ('q2', '9'): 'q2'
}

q0 = 'q0'
F = {'q1'}

def afd(palavra):
    estado_atual = q0
    for simbolo in palavra:
        estado_atual = transicoes[(estado_atual, simbolo)]
    return estado_atual in F

# Testes
print(afd('120'))  # True
print(afd('65'))  # True
print(afd('94'))  # False
print(afd('123'))  # False
print(afd('456'))  # False