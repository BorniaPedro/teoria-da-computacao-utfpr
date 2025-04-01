# AFD 𝑀5 que reconheça 𝐿5 = {𝑥 ∈ {𝑎, 𝑏}∗ ∣ |𝑥| mod 3 = 0}

# Definindo transições
transicoes = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q0',
    ('q2', 'b'): 'q0'
}

estado_inicial = 'q0'
estados_finais = {'q0'}

def afd(palavra):
    estado_atual = estado_inicial
    for simbolo in palavra:
        estado_atual = transicoes[(estado_atual, simbolo)]
    return estado_atual in estados_finais

# Testes
print(afd('ab'))  # False
print(afd('aaa'))  # True
print(afd('aba'))  # True
print(afd('abba'))  # False
print(afd('bababa'))  # True 
