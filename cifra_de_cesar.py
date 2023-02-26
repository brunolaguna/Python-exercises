modo = "" # Modo é o menu do programa.
resultado = "" # Resultado será tanto a criptografia ou a descriptografia dos -
#caracteres digitados.
fim = int(input("Digite 0 para sair ou 1 para iniciar: "))
# Fim é para a pessoa sair caso ela não queira mais continuar o programa.

if(fim == 1): # Se o usuário digitar 1 o menu irá mostrar todos os modos.
    modo = input("\nVocê deseja:\n0 - Sair\n1 - Criptografar\n2 - Descriptografar\n")
#No menu a pessoa escolhe o modo, para qual função ela deseja.
    if(modo == "1"):# Se a variável "modo" ser = 1, irá criptografar.
        texto = input("Insira o texto para Criptografar (até 128 carácteres): \n")
        # Texto serve para a variável receber o que o usuário digitar.
        
        if (len(texto) < 129):
#Se o tamanho da variável texto for maior que 128, irá direto para a função else.
            for i in range(0, len(texto)):
    # Var "i" percorre do primeiro carácter até o ultimo digitado pelo usuário.
                resultado = resultado + chr(ord(texto[i]) + 2)
# Resultado será sempre a criptografia nesse bloco; os caracteres vão pular 2 -
# casas para frente da tabela ASCII concluindo assim a criptografia da var "texto".                   
                print(resultado, end='')
                resultado = "" # Mostrar o resultado, na mesma linha. 
                            
        else: # Caso o número de carácteres for maior que 128.
            print("\nUltrapassou o limite de carácteres.")
            

    if(modo == "2"): # Modo = 2 irá executar esse bloco de comandos para descriptografar.
        texto = input("Insira o texto para descriptografar (até 128 carácteres): \n")
# A var "texto" aqui, tem a mesma função para o "modo = 1".       
        if (len(texto) < 129): 
# Se o tamanho da variável texto for maior que 128, irá direto para a função else.
            for i in range(0, len(texto)):
    # Var "i" percorre do primeiro carácter até o último digitado pelo usuário.
                resultado = resultado + chr(ord(texto[i]) - 2)
# Nesse bloco de comando sempre irá descriptografar, assim o "resultado" de cada
# carácter irá receber o valor de 2 casas para trás da tabela ASCII.
                print(resultado, end='')
                resultado = "" # Mostrar o resultado, na mesma linha. 

        else: # Caso o número de carácteres for maior que 128.
            print("\nUltrapassou o limite de carácteres.")

    if(modo == "0"): # "Modo = 0" irá acabar a programação.
            fim = 0
            
while(fim == 0):
    print("Fim da programação.")
    break
    
