cpf = input("Digite o seu cpf: ")
*cpf, last_one, last_two = cpf

# Logica de verificação do primeiro digito

r = 0
v = 10
for n in cpf:
    r += (v * int(n))
    v -= 1
i = 11 - (r % 11)
d1 = 0 if (i > 9) else i

cpf += f'{d1}'

# Lógica de verificação do segundo digito

r = 0
v = 11
for n in cpf:
    r += (v * int(n))
    v -= 1
n = 11 - (r % 11)
d2 = 0 if (n > 9) else n

# Verifica se os resultados finais são iguais aos digitos do cpf

if d1 == int(last_one) and d2 == int(last_two):
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')
