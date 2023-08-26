

while True:
    number_one = input('Digite um número: ')
    number_two = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(number_one)
        num_2_float = float(number_two)
        numeros_validos = True
    except:
         numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos. ')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Ou você escolheu um operador inválido, ou não é um operador.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador. ')
        continue

    print('Realizando sua conta. Confira o Resultado a baixo.')
    if operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
    elif operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
    else:
        print('erro 2024')



    sair = input('Quer sair? [s]im: ')
    sair = sair.lower() #Serve para deixar tudo com letra minuscula .lower
    sair= sair.startswith('s') # Serve para indentificar o que começa em cada frase .startswith
    print(sair)

    if sair is True: #se sair for verdadeiro
        break