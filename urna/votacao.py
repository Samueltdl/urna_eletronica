#coding=UTF-8
import graphics as gf
from time import sleep

win = gf.GraphWin("urna", 1280, 720)

############################################################################################ IMAGEM BASE DA URNA

def urna():
    img = gf.Image(gf.Point(640, 350), 'C:/Users/samue/Desktop/urna/urna.png')
    img.draw(win)
    
    '''
    while True:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()

        print('x = ', x)
        print('y = ', y, '\n')
    '''
urna()

############################################################################################ DADOS DOS GOVERNADORES

#FUNÇÃO PARA SALVAR O NOME DO CANDIDATO EM UMA LISTA SEPARADA
def nomes_governadores():

    #ABRINDO O ARQUIVO
    arq_governador = open('C:/Users/samue/Desktop/urna/governador.csv', 'r')
    lista_governador = arq_governador.readlines()

    lista = []
    for elemento in lista_governador:
        lista.append(elemento [0:-1])

    lista1 = []
    for elemento in lista:
        lista1.append(elemento.split(';'))

    nome_governador = []
    for elemento in lista1:
        nome_governador.append(elemento[0])
    print(nome_governador)

    return nome_governador

nome_governador = nomes_governadores()

#FUNÇÃO PARA SEPARAR O NÚMERO DO CANDIDATO EM UMA LISTA SEPARADA
def numeros_governadores():
    
    #ABRINDO O ARQUIVO
    arq_governador = open('C:/Users/samue/Desktop/urna/governador.csv', 'r')
    lista_governador = arq_governador.readlines()

    lista = []
    for elemento in lista_governador:
        lista.append(elemento [0:-1])

    lista1 = []
    for elemento in lista:
        lista1.append(elemento.split(';'))

    numero_governador = []
    for elemento in lista1:
        numero_governador.append(elemento[1])
    print(numero_governador)

    return numero_governador

numero_governador = numeros_governadores()

#FUNÇÃO ONDE FORAM CRIADOS ALGUNS ELEMENTOS QUE POSTERIORMENTE SERÃO MOSTRADOS NA TELA DE VOTAÇÃO
def estrutura_governador():
    #RETÂNGULO ONDE SERÁ INSERIDO O PRIMEIRO NÚMERO
    retangulo1 = gf.Rectangle(gf.Point(170, 315), gf.Point(200, 365))
    #RETÂNGULO ONDE SERÁ INSERIDO O SEGUND NÚMERO
    retangulo2 = gf.Rectangle(gf.Point(205, 315), gf.Point(235, 365))
    
    #PALAVRA "GOVERNADOR" QUE SERÁ EXIBIDA NA TELA INDICANDO AO USUÁRIO QUAL CARGO O MESMO ESTÁ VOTANDO
    governador = gf.Text(gf.Point(350, 285), 'Governador')
    governador.setSize(20)

    #LISTA CRIADA PARA FACILITAR A EXIBIÇÃO DOS ELEMENTOS NA TELA POSTERIORMENTE
    lista = [retangulo1, retangulo2, governador]
    return lista

bgl_governador = estrutura_governador()

############################################################################################ DADOS DOS PRESIDENTES

#FUNÇÃO PARA SALVAR O NOME DO CANDIDATO EM UMA LISTA SEPARADA
def nomes_presidentes():

    #ABRINDO O ARQUIVO
    arq_presidente = open('C:/Users/samue/Desktop/urna/presidente.csv', 'r')
    lista_presidente = arq_presidente.readlines()

    lista = []
    for elemento in lista_presidente:
        lista.append(elemento [0:-1])

    lista1 = []
    for elemento in lista:
        lista1.append(elemento.split(';'))

    nome_presidente = []
    for elemento in lista1:
        nome_presidente.append(elemento[0])
    print(nome_presidente)

    return nome_presidente

nome_presidente = nomes_presidentes()

#FUNÇÃO PARA SEPARAR O NÚMERO DO CANDIDATO EM UMA LISTA SEPARADA
def numeros_presidentes():
    #ABRINDO O ARQUIVO
    arq_presidente = open('C:/Users/samue/Desktop/urna/presidente.csv', 'r')
    lista_presidente = arq_presidente.readlines()

    lista = []
    for elemento in lista_presidente:
        lista.append(elemento [0:-1])

    lista1 = []
    for elemento in lista:
        lista1.append(elemento.split(';'))

    numero_presidente = []
    for elemento in lista1:
        numero_presidente.append(elemento[1])
    print(numero_presidente)

    return numero_presidente

numero_presidente = numeros_presidentes()

#FUNÇÃO ONDE FORAM CRIADOS ALGUNS ELEMENTOS QUE POSTERIORMENTE SERÃO MOSTRADOS NA TELA DE VOTAÇÃO
def estrutura_presidente():
    #RETÂNGULO ONDE SERÁ INSERIDO O PRIMEIRO NÚMERO
    retangulo1 = gf.Rectangle(gf.Point(170, 315), gf.Point(200, 365))
    #RETÂNGULO ONDE SERÁ INSERIDO O SEGUND NÚMERO
    retangulo2 = gf.Rectangle(gf.Point(205, 315), gf.Point(235, 365))
    
    #PALAVRA "PRESIDENTE" QUE SERÁ EXIBIDA NA TELA INDICANDO AO USUÁRIO QUAL CARGO O MESMO ESTÁ VOTANDO
    presidente = gf.Text(gf.Point(350, 285), 'Presidente')
    presidente.setSize(20)

    #LISTA CRIADA PARA FACILITAR A EXIBIÇÃO DOS ELEMENTOS NA TELA POSTERIORMENTE
    lista = [retangulo1, retangulo2, presidente]
    return lista

bgl_presidente = estrutura_presidente()

############################################################################################ ELEMENTOS DA PARTE DE ENCERRAMENTO DA VOTAÇÃO

# FUNÇÃO QUE GERA OS ELEMENTOS DO BOTÃO DE ENCERRAR
def botao_encerra():

    #RETÂNGULO CRIADO PARA ORGANIZAR OS BOTÕES DE "SIM" E "NÃO"
    box = gf.Rectangle(gf.Point(278, 349), gf.Point(598, 489))
    box.setFill('orange')

    #TEXTO PERGUNTANDO SE O USUÁRIO DESEJA ENCERRAR A VOTAÇÃO
    texto = gf.Text(gf.Point(438, 370), 'Deseja encerrar a votação?')
    texto.setTextColor('white')
    texto.setSize(14)

    #BOTÃO "SIM", COMPOSTO POR UM RETÂNGULO E UM TEXTO
    botao_sim = gf.Rectangle(gf.Point(328, 399), gf.Point(418, 439))
    botao_sim.setFill('green')
    texto_sim = gf.Text(gf.Point(373, 419), 'SIM')
    texto_sim.setTextColor('white')
    texto_sim.setSize(20)

    #BOTÃO "NÃO", TAMBÉM COMPOSTO POR UM RETÂNGULO E UM TEXTO
    botao_nao = gf.Rectangle(gf.Point(448, 399), gf.Point(538, 439))
    botao_nao.setFill('red')
    texto_nao = gf.Text(gf.Point(493, 419), 'NÃO')
    texto_nao.setTextColor('white')
    texto_nao.setSize(20)

    #LISTA CRIADA PARA MOSTRAR OS ELEMENTOS NA TELA POSTERIORMENTE
    encerra = [box, texto, botao_sim, texto_sim, botao_nao, texto_nao]
    return encerra

# FUNÇÃO PARA DEFINIR OS DIGITOS DA SENHA DE ENCERRAMENTO DA VOTAÇÃO
def encerramento():

    #RETÂNGULO CRIADO PARA INSERIR OS ELEMENTOS
    box = gf.Rectangle(gf.Point(278, 349), gf.Point(598, 489))
    box.setFill('orange')

    #TEXTO INFORMANDO AO USUÁRIO PARA DIGITAR A SENHA DE ENCERRAMENTO
    texto = gf.Text(gf.Point(438, 370), 'Digite a senha para enerrar a votação')
    texto.setTextColor('white')
    texto.setSize(14)

    #RETÂNGULOS ONDE POSTERIORMENTE SERÃO INSERIDOS OS DIGITOS DA SENHA
    retangulo1 = gf.Rectangle(gf.Point(345, 400), gf.Point(385, 450))
    retangulo1.setFill('white')

    retangulo2 = gf.Rectangle(gf.Point(395, 400), gf.Point(435, 450))
    retangulo2.setFill('white')

    retangulo3 = gf.Rectangle(gf.Point(445, 400), gf.Point(485, 450))
    retangulo3.setFill('white')

    retangulo4 = gf.Rectangle(gf.Point(495, 400), gf.Point(535, 450))
    retangulo4.setFill('white')

    #LISTA CRIADA PARA POSTERIORMENTE MOSTRAR TODOS OS ELEMENTOS NA TELA
    lista = [box, texto, retangulo1, retangulo2, retangulo3, retangulo4]
    return lista

# FUNÇÃO PARA MOSTRAR OS DIGITOS DA SENHA NA TELA
def digitos_encerramento():
    numero1 = gf.Text(gf.Point(365, 435), '*')
    numero1.setTextColor('black')
    numero1.setSize(36)

    numero2 = gf.Text(gf.Point(415, 435), '*')
    numero2.setTextColor('black')
    numero2.setSize(36)

    numero3 = gf.Text(gf.Point(465, 435), '*')
    numero3.setTextColor('black')
    numero3.setSize(36)

    numero4 = gf.Text(gf.Point(515, 435), '*')
    numero4.setTextColor('black')
    numero4.setSize(36)

    lista = [numero1, numero2, numero3, numero4]
    return lista

#FUNÇÃO QUE MOSTRA A MENSAGEM DE "SENHA CORRETA NA TELA" ANTES DE FINALIZAR O PROGRAMA
def senha_correta():
    texto = gf.Text(gf.Point(438, 335), 'Senha correta!')
    texto.setSize(20)
    return texto

#FUNÇÃO QUE MOSTRA A MENSAGEM "SENHA INCORRETA" E PEDE PARA O USUÁRIO TENTAR NOVAMENTE
def senha_incorreta():
    texto = gf.Text(gf.Point(438, 335), 'Senha Incorreta! Tente novamente.')
    texto.setSize(20)
    return texto

############################################################################################ ESTRUTURA DE DICAS

def estrutura_dicas():
    #TEXTOS QUE APARECEM NAS DICAS APÓS O USUÁRIO DEFINIR O VOTO
    dicas = gf.Text(gf.Point(120, 585), 'Aperte a tecla: \n                               CONFIRMA para PROSSEGUIR \n                                     CORRIGE para REINICIAR este voto')
    #LINHA QUE SEPARA A PARTE DE INFORMAÇÕES DA VOTAÇÃO DA PARTE DAS DICAS
    linha = gf.Line(gf.Point(59, 550), gf.Point(789, 550))
    
    #LISTA CRIADA PARA FACILITAR A EXIBIÇÃO DOS ELEMENTOS NA TELA POSTERIORMENTE
    lista = [dicas, linha]
    return lista

############################################################################################ TEXTO DE FIM

def fim():
    #DEFININDO O TEXTO
    fim = gf.Text(gf.Point(440, 425), 'FIM')
    fim.setSize(36)

    return fim

############################################################################################ FUNÇÃO PARA ARMAZENAR OS DIGITOS DO TECLADO

def digitos():
    #STR CRIADA PARA ARMAZENAR OS NÚMEROS DO VOTO OU O VOTO EM BRANCO
    numeros = ''
    
    #INICIANDO O LOOP DOS DÍGITOS
    while len(numeros) < 2:
        #REQUISITANDO O CLIQUE DO USUÁRIO
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()

        #COORDENADAS NÚMEROS DE 1 A 3
        if 312 <= y <= 361:
            if 902 <= x <= 969:
                numeros += '1'
            elif 994 <= x <= 1059:
                numeros += '2'
            elif 1085 <= x <= 1152:
                numeros += '3'

        #COORDENADAS NÚMEROS DE 4 A 6
        if 382 <= y <= 429:
            if 902 <= x <= 969:
                numeros += '4'
            elif 994 <= x <= 1059:
                numeros += '5'
            elif 1085 <= x <= 1152:
                numeros += '6'

        #COORDENADAS NÚMEROS DE 7 A 9
        if 456 <= y <= 501:
            if 902 <= x <= 969:
                numeros += '7'
            elif 994 <= x <= 1059:
                numeros += '8'
            elif 1085 <= x <= 1152:
                numeros += '9'

        #COORDENADAS NÚMERO 0
        if 518 <= y <= 569:
            if 994 <= x <= 1059:
                numeros += '0'

        #CORDENADAS BOTÃO VOTO EM BRANCO
        if len(numeros) == 0:
            if 586 <= y <= 635:
                if 860 <= x <= 956:
                    #ADICIONANDO A PALAVRA "BRANCO" NA STR
                    numeros += 'BRANCO'
                    #ESSE LOOP COM A LEN(NUMEROS) < 2 TAMBÉM FUNCIONA PARA O VOTO EM BRANCO POIS A PALAVRA "BRANCO" É UMA STR COM LEN > 2

        print('números do voto:', numeros)
        
    return numeros

############################################################################################ VOTAÇÃO

valor_encerra = False
while valor_encerra == False:

    ############################################################################################ VOTAÇÃO PARA GOVERNADOR

    def voto_governador():
        #MOSTRANDO OS ELEMENTOS DA VOTAÇÃO PARA GOVERNADOR NA TELA
        for elem in bgl_governador:
            elem.draw(win)
        #DEFININDO O VALOR DA VARIÁVEL QUE VERIFICA SE O USUÁRIO CONFIRMOU O VOTO
        confirma = False
        #LOOP DA VALIDAÇÃO DO VOTO    
        while confirma == False:
            
            #REQUISITANDO A FUNÇÃO DE DIGITOS
            numeros = digitos()
            lista = []

            #VERIFICANDO SE FORAM DIGITADOS 2 DIGITOS
            if len(numeros) == 2:
                #DEFININDO O PRIMEIRO NÚMERO PARA MOSTRAR NA TELA
                numero1 = gf.Text(gf.Point(185, 340), numeros[0])
                numero1.setSize(36)
                #DEFININDO O SEGUNDO NÚMERO PARA MOSTRAR NA TELA
                numero2 = gf.Text(gf.Point(220, 340), numeros[1])
                numero2.setSize(36)

                #ADICIONANDO OS NÚMEROS EM UMA LISTA
                lista.append(numero1)
                lista.append(numero2)

            #VERIFICANDO SE O VOTO FOI BRANCO
            if numeros == 'BRANCO':
                #DEFININDO O TEXTO DE VOTO EM BRANCO
                voto_branco = gf.Text(gf.Point(440, 425), 'VOTO EM BRANCO')
                voto_branco.setSize(36)

                #ADICIONANDO O TEXTO DE VOTO EM BRANCO NA LISTA
                lista.append(voto_branco)
            
            #VERIFICANDO SE OS NÚMEROS DIGITADOS NÃO ESTÃO NA LISTA DE NÚMEROS DOS CANDIDATOS
            #CASO NÃO ESTEJAM O VOTO SERÁ NULO
            if numeros not in numero_governador and numeros != 'BRANCO':
                #DEFININDO O TEXTO DE VOTO NULO
                nulo = gf.Text(gf.Point(470, 425), 'VOTO NULO')
                nulo.setSize(26)
                #DEFININDO O TEXTO INDICANDO QUE O NÚMERO DIGITADO ESTÁ ERRADO
                texto = gf.Text(gf.Point(260, 423), 'NÚMERO ERRADO:')
                texto.setSize(16)

                #ADICIONANDO OS ELEMENTOS NA LISTA
                lista.append(nulo)
                lista.append(texto)

            #VERIFICANDO SE OS NÚMEROS DIGITADOS ESTÃO NA LISTA DE NÚMEROS DOS CANDIDATOS
            #CASO ESTEJAM O VOTO SERÁ VÁLIDO
            if numeros in numero_governador:
                #OBTENDO O ÍNDICE DO NÚMERO DO GOVERNADOR
                indice = numero_governador.index(numeros)
                #ATRELANDO O ÍNDICE OBTIDO A FOTO DO CANDIDATO
                foto = gf.Image(gf.Point(726, 329), f'{numeros}.png')
                #ATRELANDO O ÍNDICE OBTIDO A LISTA DE NOMES PARA OBTER O NOME DO CANDIDATO
                nome = gf.Text(gf.Point(272, 420),f'NOME: {nome_governador[indice]}')
                nome.setSize(16)

                #ADICIONANDO OS ELEMENTOS NA LISTA
                lista.append(foto)
                lista.append(nome)

            #MOSTRANDO OS ELEMENTOS DA LISTA NA TELA DE ACORDO COM O VOTO QUE FOI DADO
            for elem in lista:
                elem.draw(win)

            #CHAMANDO A FUNÇÃO DE DICAS PARA MOSTRAR AS INFORMAÇÕES NA TELA
            dicas = estrutura_dicas()
            for elem in dicas:
                elem.draw(win)

            #REQUISITANDO COORDENADAS PARA VERIFICAR SE O USUÁRIO QUER CORRIGIR O VOTO O SE CONFIRMOU O VOTO
            clique = win.getMouse()
            x = clique.getX()
            y = clique.getY()

            #COORDENADAS BOTÃO CORRIGE
            if 586 <= y <= 635 and 980 <= x <= 1074:
                print('CORRIGE')
                #CASO O USUÁRIO TENHA CLICADO EM "CORRIGE" AS INFORMAÇÕES QUE FORAM ADICIONADAS NA LISTA DE ACORDO COM O VOTO QUE FOI DADO IRÃO SER RETIRADAS DA TELA
                for elem in lista:
                    elem.undraw()

                #RETIRANDO AS DICAS DA TELA  
                for elem in dicas:
                    elem.undraw()

            #COORDENADAS BOTÃO CONFIRMA
            if 574 <= y <= 632 and 1100 <= x <= 1194:
                print('CONFIRMA')
                confirma = True
                sleep(0.2)

                #RETIRANDO OS ELEMENTOS QUE FORAM ADICIONADOS NA LISTA DA TELA
                for elem in lista:
                    elem.undraw()

                #RETIRANDO AS DICAS DA TELA
                for elem in dicas:
                    elem.undraw()

                #RETIRANDO AS INFORMAÇÕES DA VOTAÇÃO PARA GOVERNADOR DA TELA POIS O PRÓXIMO VOTO SERÁ PARA PRESIDENTE
                for elem in bgl_governador:
                    elem.undraw()
                sleep(0.7)

    voto_governador()

    ############################################################################################ VOTAÇÃO PARA PRESIDENTE

    def voto_presidente():
        
        #MOSTRANDO OS ELEMENTOS DA VOTAÇÃO PARA GOVERNADOR NA TELA
        for elem in bgl_presidente:
            elem.draw(win)
        #DEFININDO O VALOR DA VARIÁVEL QUE VERIFICA SE O USUÁRIO CONFIRMOU O VOTO
        confirma = False
        #LOOP DA VALIDAÇÃO DO VOTO    
        while confirma == False:
            
            #REQUISITANDO A FUNÇÃO DE DIGITOS
            numeros = digitos()
            lista = []

            #VERIFICANDO SE FORAM DIGITADOS 2 DIGITOS
            if len(numeros) == 2:
                #DEFININDO O PRIMEIRO NÚMERO PARA MOSTRAR NA TELA
                numero1 = gf.Text(gf.Point(185, 340), numeros[0])
                numero1.setSize(36)
                #DEFININDO O SEGUNDO NÚMERO PARA MOSTRAR NA TELA
                numero2 = gf.Text(gf.Point(220, 340), numeros[1])
                numero2.setSize(36)

                #ADICIONANDO OS NÚMEROS EM UMA LISTA
                lista.append(numero1)
                lista.append(numero2)

            #VERIFICANDO SE O VOTO FOI BRANCO
            if numeros == 'BRANCO':
                #DEFININDO O TEXTO DE VOTO EM BRANCO
                voto_branco = gf.Text(gf.Point(440, 425), 'VOTO EM BRANCO')
                voto_branco.setSize(36)

                #ADICIONANDO O TEXTO DE VOTO EM BRANCO NA LISTA
                lista.append(voto_branco)
            
            #VERIFICANDO SE OS NÚMEROS DIGITADOS NÃO ESTÃO NA LISTA DE NÚMEROS DOS CANDIDATOS
            #CASO NÃO ESTEJAM O VOTO SERÁ NULO
            if numeros not in numero_presidente and numeros != 'BRANCO':
                #DEFININDO O TEXTO DE VOTO NULO
                nulo = gf.Text(gf.Point(470, 425), 'VOTO NULO')
                nulo.setSize(26)
                #DEFININDO O TEXTO INDICANDO QUE O NÚMERO DIGITADO ESTÁ ERRADO
                texto = gf.Text(gf.Point(260, 423), 'NÚMERO ERRADO:')
                texto.setSize(16)

                #ADICIONANDO OS ELEMENTOS NA LISTA
                lista.append(nulo)
                lista.append(texto)

            #VERIFICANDO SE OS NÚMEROS DIGITADOS ESTÃO NA LISTA DE NÚMEROS DOS CANDIDATOS
            #CASO ESTEJAM O VOTO SERÁ VÁLIDO
            if numeros in numero_presidente:
                #OBTENDO O ÍNDICE DO NÚMERO DO GOVERNADOR
                indice = numero_presidente.index(numeros)
                #ATRELANDO O ÍNDICE OBTIDO A FOTO DO CANDIDATO
                foto = gf.Image(gf.Point(726, 329), f'{numeros}.png')
                #ATRELANDO O ÍNDICE OBTIDO A LISTA DE NOMES PARA OBTER O NOME DO CANDIDATO
                nome = gf.Text(gf.Point(272, 420),f'NOME: {nome_presidente[indice]}')
                nome.setSize(16)

                #ADICIONANDO OS ELEMENTOS NA LISTA
                lista.append(foto)
                lista.append(nome)

            #MOSTRANDO OS ELEMENTOS DA LISTA NA TELA DE ACORDO COM O VOTO QUE FOI DADO
            for elem in lista:
                elem.draw(win)

            #CHAMANDO A FUNÇÃO DE DICAS PARA MOSTRAR AS INFORMAÇÕES NA TELA
            dicas = estrutura_dicas()
            for elem in dicas:
                elem.draw(win)

            #REQUISITANDO COORDENADAS PARA VERIFICAR SE O USUÁRIO QUER CORRIGIR O VOTO O SE CONFIRMOU O VOTO
            clique = win.getMouse()
            x = clique.getX()
            y = clique.getY()

            #COORDENADAS BOTÃO CORRIGE
            if 586 <= y <= 635 and 980 <= x <= 1074:
                print('CORRIGE')
                #CASO O USUÁRIO TENHA CLICADO EM "CORRIGE" AS INFORMAÇÕES QUE FORAM ADICIONADAS NA LISTA DE ACORDO COM O VOTO QUE FOI DADO IRÃO SER RETIRADAS DA TELA
                for elem in lista:
                    elem.undraw()

                #RETIRANDO AS DICAS DA TELA  
                for elem in dicas:
                    elem.undraw()

            #COORDENADAS BOTÃO CONFIRMA
            if 574 <= y <= 632 and 1100 <= x <= 1194:
                print('CONFIRMA')
                confirma = True
                sleep(0.2)

                #RETIRANDO OS ELEMENTOS QUE FORAM ADICIONADOS NA LISTA DA TELA
                for elem in lista:
                    elem.undraw()

                #RETIRANDO AS DICAS DA TELA
                for elem in dicas:
                    elem.undraw()

                #RETIRANDO AS INFORMAÇÕES DA VOTAÇÃO PARA PRESIDENTE DA TELA POIS O PRÓXIMO VOTO SERÁ PARA GOVERNADOR
                for elem in bgl_presidente:
                    elem.undraw()
                sleep(0.7)

    voto_presidente()

    ############################################################################################ CÓDIGO PARA PERGUNTAR SE O USUÁRIO DESEJA ENCERRAR A VOTAÇÃO
    
    #CHAMANDO A FUNÇÃO QUE CONTÉM OS ELEMENTOS DOS BOTÕES DE ENCERRAR
    encerra = botao_encerra()

    #MOSTRANDO OS ELEMENTOS NA TELA
    for elem in encerra:
        elem.draw(win)

    clique = win.getMouse()
    x = clique.getX()
    y = clique.getY()

    #COORDENADAS DO BOTÃO "SIM"
    if (328 < x < 418) and (399 < y < 439):
        print('SIM')
        #CHAMANDO A FUNÇÃO QUE SOLICITA AO USUÁRIO QUE DIGITE A SENHA
        pede_senha = encerramento()
        #CHAMANDO A FUNÇÃO QUE ARMAZENA AS POSIÇÕES DE CADA CARACTER D SENHA
        digitados = digitos_encerramento()
        #CASO O USUÁRIO CLIQUE EM "SIM" A VARIÁVEL "VALOR_ENCERRA" PASSA A SER VERDADEIRA, FAZENDO COM QUE O PROGRAMA SAIA DO LOOP
        valor_encerra = True
        #RETIRANDO OS ELEMENTOS DA TELA PARA SOLICITAR A SENHA DE ENCERRAMENTO AO USUÁRIO
        for elem in encerra:
            elem.undraw()
        
        for elem in pede_senha:
            elem.draw(win)
        
        #SENHA CORRETA
        senha = '0000'
        #STR CRIADA PARA ARMAZENAR OS NÚMEROS DA SENHA QUE O USUÁRIO DIGITOU
        numeros = ''
        #INICIANDO O LOOP DOS DÍGITOS DA SENHA
        while numeros == '':
            while len(numeros) < 4:
                #REQUISITANDO O CLIQUE DO USUÁRIO
                clique = win.getMouse()
                x = clique.getX()
                y = clique.getY()

                #COORDENADAS NÚMEROS DE 1 A 3
                if 312 <= y <= 361:
                    if 902 <= x <= 969:
                        numeros += '1'
                    elif 994 <= x <= 1059:
                        numeros += '2'
                    elif 1085 <= x <= 1152:
                        numeros += '3'

                #COORDENADAS NÚMEROS DE 4 A 6
                if 382 <= y <= 429:
                    if 902 <= x <= 969:
                        numeros += '4'
                    elif 994 <= x <= 1059:
                        numeros += '5'
                    elif 1085 <= x <= 1152:
                        numeros += '6'

                #COORDENADAS NÚMEROS DE 7 A 9
                if 456 <= y <= 501:
                    if 902 <= x <= 969:
                        numeros += '7'
                    elif 994 <= x <= 1059:
                        numeros += '8'
                    elif 1085 <= x <= 1152:
                        numeros += '9'

                #COORDENADAS NÚMERO 0
                if 518 <= y <= 569:
                    if 994 <= x <= 1059:
                        numeros += '0'
                
                print('numeros digitados para senha:', numeros)

                #VERIFICANDO A QUANTIDADE DE NÚMEROS QUE O USUÁRIO DIGITOU PARA MOSTRAR OS "*" NA TELA
                if len(numeros) == 1:
                    digitados[0].draw(win)

                if len(numeros) == 2:
                    digitados[1].draw(win)

                if len(numeros) == 3:
                    digitados[2].draw(win)

                if len(numeros) == 4:
                    digitados[3].draw(win)
            
            #VERIFICANDO SE A SENHA QUE O USUÁRIO DIGITOU ESTÁ CORRETA
            if numeros == senha:
                print('SENHA CORRETA')

                #CHAMANDO A FUNÇÃO PARA EXIBIR A MENSAGEM INFORMANDO AO USUÁRIO QUE A SENHA DIGITADA ESTÁ CORRETA
                texto = senha_correta()
                texto.draw(win)
                sleep(1)
                texto.undraw()
                for elem in pede_senha:
                    elem.undraw()
                
                for elem in digitados:
                    elem.undraw()
                sleep(0.5)

            #CASO A SENHA NÃO ESTEJA CORRETA
            else:
                print('SENHA INCORRETA')
                #CHAMANDO A FUNÇÃO PARA EXIBIR A MENSAGEM INFORMANDO AO USUÁRIO QUE A SENHA DIGITADA ESTÁ INCORRETA
                texto = senha_incorreta()
                texto.draw(win)
                sleep(1)
                texto.undraw()

                for elem in digitados:
                    elem.undraw()
                numeros = ''   
                
    #CASO O USUÁRIO CLIQUE EM "NÃO" A VARIÁVEL NÃO MUDA SEU VALOR, SEGUINDO NO LOOP ATÉ QUE O USUÁRIO DECIDA ENCERRAR O PROGRAMA
    elif (448 < x < 538) and (399 < y < 439):
        print('NÃO')
        #RETIRANDO OS ELEMENTOS DA TELA PARA VOLTAR PARA A VOTAÇÃO
        sleep(0.15)
        for elem in encerra:
            elem.undraw()
        sleep(0.5)

#CHAMANDO A FUNÇÃO QUE CONTÉM O TEXTO "FIM"
final = fim()
#EXIBINDO O TEXTO NA TELA
final.draw(win)
sleep(2)
win.close()





##############     AINDA FALTA FAZER:     ################

#CONTADOR DE VOTOS (TALVEZ POSSA SER FEIO A PARTIR DO BOTÃO DE CONFIRMA)