import os


# Essa função serve para definir o estado do boneco na forca em relação aos erros do usuário
def homenzinho(erros = 0):
    if erros == 0:
        print('''JOGO DA FORCA
      _________      
      |       |
      |       
      |      
      |      
    __⊥__
    ''')
    
    if erros == 1:
        print('''JOGO DA FORCA
      _________      
      |       |
      |       ◓
      |      
      |      
    __⊥__
    ''')
        
    if erros == 2:
        print('''JOGO DA FORCA
      _________      
      |       |
      |       ◓
      |       |
      |      
    __⊥__
    ''')
        
    if erros == 3:
        print('''JOGO DA FORCA
      _________      
      |       |
      |       ◓
      |       |\\
      |      
    __⊥__
    ''')
        
    if erros == 4:
        print('''JOGO DA FORCA
      _________      
      |       |
      |       ◓
      |      /|\\
      |      
    __⊥__
    ''')
        
    if erros == 5:
        print('''JOGO DA FORCA
      _________      
      |       |
      |       ◓
      |      /|\\
      |      /
    __⊥__
    ''')
        
    if erros == 6:
        print('''JOGO DA FORCA
      _________      
      |       |
      |       ◓
      |      /|\\
      |      / \\
    __⊥__
    ''')
        
    if erros == 7:
        print('''      _________      
      |       |
      |       ✕
      |      /|\\
      |      | |
    __⊥__
    ''')

# DIGITE A PALAVRA PARA SER ADIVINHADA
# NÃO ADICIONE ACENTUAÇÃO!! iquei cm preguiça de otimizar :)
palavra_escolhida = 'CAIXA DAGUA'


# Essa variável serve para definir quais letras o usuário informou
letras_escolhidas = '' # Caso a letra não esteja na palavra, a palavra aparecerá no prompt de forma oculta

letras_erradas = [] # Essa lista serve para armazenar, e posteriormente mostrar, quais letras o usuário digitou e não pertencem a palavra

tentativas = 0 # Essa variável define o número de tentativas o usuário tem
erros = 0 # Essa variável serve para definir a quantidade de erros do usuário. O mesmo perde o jogo se seus erros chegarem a 7


    
homenzinho() # Função criada para apresentar visualmente o boneco na forca

# Laço para manipular as jogadas
while True:
    tentativas += 1 
    letra = str(input('Informe uma letra: ')).lower() # Lê um caractere do teclado e o transforma em minúsculo para uma melhor manipulação da variável posteriormente
    
    os.system('cls') # Função da biblioteca "os" para limpar o terminal

# Verificação de entrada do usuário. Obriga ao usuário a digitar um único caractere
    if len(letra) != 1:
        homenzinho(erros)
        print('Informe somente uma letra!')
        print(palavra_que_aparece)
        print(f"LETRAS ERRADAS: {letras_erradas}")
        continue


    # Incrementa a letra informada pelo usuário  
    letras_escolhidas += letra 

    
    # Essa flag servirá para definir um erro, conferindo se o usuário digitou alguma letra que não consta na palavra
    flag = True

    # Seleciona as letras que o usuário informou e que não estão na palavra
    if letra not in palavra_escolhida.lower() and letra.upper() not in letras_erradas:
        letras_erradas.append(letra.upper())
    
    # Essa variável será mostrada no prompt de forma oculta, a maneira que o usuário for digitando as letras corretas
    palavra_que_aparece = '' # 

    # Para cada letra que esteja na palavra escolhida...
    for letra_da_palavra in palavra_escolhida:
        if letra == letra_da_palavra.lower(): # Verificamos se o usuário informou uma letra que não esteja na palavra inicial
            flag = False # Caso tenha digitado uma letra correta, a flag permanece falsa por todo o laço, constando assim que o usuário não cometeu erros
        
        # Caso a letra da palavra inicial estiver dentre as letras que o usuário informou...
        if letra_da_palavra.lower() in letras_escolhidas.lower():
            palavra_que_aparece += letra_da_palavra # A palavra que será mostrada no prompt de forma oculta, incrementa essa letra

        # Caso a letra da palavra inicial for um espaço, será substituída por um ífen. Para uma melhor representação no prompt
        elif letra_da_palavra == ' ':
            palavra_que_aparece += '-'

        # E por fim, caso a letra da palavra inicial não estiver dentre as letras já informadas pelo usuário, a letra aparecerá de forma oculta no prompt
        else:
            palavra_que_aparece += '*'
    
    # Caso a flag não seja alterada dentro do laço, significa que o usuário digitou uma letra que não existe na palavra inicial. Incramentando um erro cometido
    if flag == True:
        erros += 1
    
    # Insere no prompt o layout do jogo, exibindo a forca, a palavra oculta e as letras informadas incorretamente
    homenzinho(erros)
    print(palavra_que_aparece)
    print(f"LETRAS ERRADAS: {letras_erradas}")
    
    # Aqui analisa-se a condição de parada.
    if palavra_que_aparece.lower().replace('-', ' ') == palavra_escolhida.lower():
        # Caso a palavra oculta se transforme exatamente na palavra inicial, o usuário vence o jogo é exibido a mensagem de vitória
        os.system('cls')
        homenzinho(erros)
        print(f'PARABÉNS! VOCÊ GANHOU!')
        print(f'A palavra certa era: {palavra_escolhida}')
        print(f"LETRAS ERRADAS: {letras_erradas}")
        break

    elif erros >= 7:
        # Caso o usuário atinja o limite e erros, o jogo encerra e é exibido a mensagem de derrota
        os.system('cls')
        homenzinho(erros)
        print(f'VOCÊ PERDEU! O BONECO MORREU!')
        print(f'A palavra certa era: {palavra_escolhida}')
        print(f"LETRAS ERRADAS: {letras_erradas}")
        break
        
# Apresenta o número de tentativas
print(f'Tentativas: {tentativas}')
        