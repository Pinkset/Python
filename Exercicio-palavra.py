 
letras_acertadas = '' #A cada letra acertada, substituira esse espaço da variavel
repeticoes = 1 #contabilizador de tentativas
palavra_secreta = 'Marcus Moreira' # palavra que o usuario deve tentar advinhas
import os #importa o termo os para o sistema, para podermos limpar e deixar mais organizado
while True:
    letra_digitada = input('Acerte a palavra secreta:') # Mensagem de entrada
    repeticoes += 1 # contabilizador de tentativas
    if len(letra_digitada) > 1: #Se o úsuario digitar mais de um letra, o progama exibira uma frase e retornará o usuario para o começo do progama.
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta: #Se a letra digitar estiver na letra secreta ele ira contabilzar como acerto.
        letras_acertadas += letra_digitada #logo a letrada digitada, será uma letra acertada.
    
    palavra_formada = '' #Variavel para pordemos tirar o inter das palavras na vertical e deixar na horizontal.
    for letra_secreta in palavra_secreta: #se a letra acertada estiver na palavra secreta, ira contabiliza um acerto.
        if letra_secreta in letras_acertadas: # Se a letra secreta estiver na letra acertada ere ira contabilizar.
         palavra_formada += letra_secreta # Aqui ele contabiliza a letra secreta, na palavra que se forma do úsuario
        else: 
            palavra_formada += '*' #caso o úsuario erre, será contabilzado '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear') #Limpar o sistema após o úsuario ganhar.
        print('Você finalizou o jogo.') 
        print(f'Numero de tentativas{repeticoes}x ') #contagem de tentativas
        letras_acertadas = '' #zerar as palavras
        repeticoes = 1 # zerar as tentativas

    
    

    

    