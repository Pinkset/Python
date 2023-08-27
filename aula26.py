 
frase = ' aaaa                         bbbb '

i = 0 #indice
qtd_m_vzs = 0 #
letra_m_vzs = '' #variavel

while i < len(frase): #len contador de frase com while repetidor
    letra_atual = frase[i] # frase [i] é utilizado para direcionar o contador a primeira letra da frase, ou seja o ' ' no caso.


    if letra_atual == ' ': #Para definir caso o caracter seja vazio o sistema pular para o proximo, sem contabilizar.
        i += 1
        continue


    qtd_atual = frase.count(letra_atual) # Esse é o sistema do contador com o .count, que ira contar a letra atual.

    if qtd_m_vzs < qtd_atual: #Se a quantidade de vezes for menor que a quantidade atual, não ira contabilziar.
        qtd_m_vzs = qtd_atual #Se for maior, será trasformado no novo valor.
        letra_m_vzs = letra_atual #Logo a letra que se repetir mais vezes, sera a letra atual
        
    i += 1 #soma mais um a letra, ''a+1'' ''aa+1'' e ''aaa'' e por ai vai.

print('A letra que apareceu mais vezes foi '\
        f'{letra_m_vzs} que apareceu '\
        f'{qtd_m_vzs}x'
    )
 