# Definindo transições
transicoes = {
    ('q00', 'a'): 'q10',
    ('q00', 'b'): 'q01',
    ('q10', 'a'): 'q00',
    ('q10', 'b'): 'q11',
    ('q01', 'a'): 'q11',
    ('q01', 'b'): 'q02',
    ('q11', 'a'): 'q01',
    ('q11', 'b'): 'q12',
    ('q02', 'a'): 'q12',
    ('q02', 'b'): 'q00',
    ('q12', 'a'): 'q02',
    ('q12', 'b'): 'q10'
}

q0 = 'q00'
F = {'q10'}

def afd(palavra):
    estado_atual = q0
    for simbolo in palavra:
        estado_atual = transicoes[(estado_atual, simbolo)]
    return estado_atual in F

# Testes
print (afd('abbb'))  # True
print (afd('ab'))  # False
print (afd('ababab'))  # True
print (afd('bbb'))  # False
print (afd('abbbabbba'))  # True