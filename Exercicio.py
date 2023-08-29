
import os # importa o comando os. para limpeza do sistema.

lista = [] # variavel da lista.

while True:
    print('Selecione uma opção: ') # frase de entrada
    opcao = input('[i]nserir [a]pagar [l]istar:') # frase de entrada
    if opcao == 'i':  #Se a opção escolhida for (i), reproduzirá o comando a baixo.
        os.system('cls') #Limpa o sistema.
        valor = input('Valor: ') # O valor será igual ao str digitado pelo úsuario.
        lista.append(valor) #adicionará um valor ao final da lista.
    elif opcao == 'a': # Se a escolha for (a), reproduzirá o comando a baixo.
        indice_str = input(    # frase do del.
           'Escolha o índice que você quer apagar: '
           ) 
        try: #para permitir que o progama continue sendo executavel em casos de erro.
            i = int(indice_str) #transforma o indice string em um indice interavel.
            del lista[i] #apaga o indice da lista
        except ValueError: #Caso o usuario tente digitar uma letra ou um numero float(1.2).
            print('Por favor, digite numeros inteiros. ') 
        except IndexError: #Caso o usuario tente apagar um indice que não existe.
            print('Não existe o índice que você tentou apagar.')
        except Exception: #Caso o erro seja outro fora os que foram listados, exibira essa tentativa.
            print('Error 404')
    elif opcao == 'l': #se a opção for l, o sistema irá listar o que já foi adicionado pelo úsuario.
        os.system('cls') #limpa o sistema.
        if len(lista) < 0: #Se não houver nada para listar, exibirá a impressão a baixo.
            print('Não há nada para listar')

        for i, valor in enumerate(lista): #Irá exibir um laço infinito do que o usuario já adicionou a lista.
            print(i, valor)
    else: #caso o usuario não digite i, a ou l
        print('Por favor, escolha i, a ou l. ')