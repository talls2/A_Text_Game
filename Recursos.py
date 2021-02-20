# Letra 'f' antes do texto serve como .format
# if "..." in variavel = checa o texto inserido por completo, e se a string em questão estiver, ativa o resultado.
# if "..." = variavel = checa se somente a string especificada foi digitada
import time
import Espada

# def padrão de morte do personagem
why = 'Você morreu para o dragão'


def death(why):
    print(f'{why}, Bom trabalho.')
    exit(0)


# função da coleta de informações
def inicio():
    player_name = input('qual seu nome?')
    player_class = input('qual sua classe?')
    print(f"Seu nome é {player_name.upper()}, e sua classe é {player_class.upper()}")
    time.sleep(2)
    print('portanto, vamos começar nossa aventura.')
    time.sleep(2)
    print('você acorda em uma sala escura, e ve duas portas a sua frente, uma porta vermelha e uma azul.')
    time.sleep(2)
    wakeup()


# função da cena inicial
def wakeup():
    print('você se dirige a porta:')
    print('1- vermelha')
    print('2- azul')

    door_picked = input('>')
    if door_picked == "1" or "vermelha":
        red_door_inside()
    elif door_picked == "2" or "azul":
        blue_door_inside()
    else:
        print('Desculpe, esta não é uma opção valida, por favor escolha entre "azul" ou "vermelho".')
        time.sleep(2)
        return wakeup()


# função da porta vermelha
bau = ['espada','escudo','chave','ouro']
def red_door_inside():
    print('você abre a porta, é uma sala pequena com um bau a sua direita, e uma porta a sua frente')
    time.sleep(2)
    chest_or_guard = input('o que você fará?')
    if chest_or_guard.lower() in ["frente","porta","reto","adiante"]:
        print('você se direciona a porta')
        exit(0)
#usar "if chest_or_guard.lower()..." ao inves de "if "porta" in chest_or_guard:" permite a captura de caracteres
#maiusculos também, já que o comando ".lower" coloca todos caracteres em minusculo, diminuindo as chances de erro.
    elif chest_or_guard.lower() in ["bau","baú","direita","chest"]:
        print('você se direciona ao baú')
        num_chess_itens = len(bau)
        time.sleep(2)
        print(f'você abre o baú e se depara com: ',{num_chess_itens},"itens")
        time.sleep(2)
        print('sendo eles:')
        for treasure in bau:
            print(treasure)
            time.sleep(1)
        item = input('qual item você pegará ?')
        if "espada" in item:
            print('O caminho da espada...')
            Espada()


        elif "escudo" in item:
            print('o caminho da segurança')


        elif "chave" in item:
            print('uma chave para a... ?')


        elif "ouro" in item:
            print('ganancia?')


        else:
            print('não é uma opção')




    else:
        print('não é uma opção')
        return red_door_inside()




# função da porta azul
def blue_door_inside():
    print('você abre a porta azul, ao que parece a sala está vazia')
    time.sleep(2)
    print('porém você se depara com um dragão, o que fará?')
    action = input('fugir ou ficar?')
    if "fugir" in action:
        print('você conseguiu escapar com sucesso')
        time.sleep(2)
        exit()
    elif "ficar" in action:
        death(why)
        inicio()
    else:
        print('isso nem sequer é uma opção')
        return wakeup()
