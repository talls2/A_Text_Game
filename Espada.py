import time


def espada():
    print("você retira a espada do baú")
    print("ao retirar a espada, você escuta a porta a sua frente se mover, o que fará?")
    print("1- Esconder-se")
    print("2- Correr em direção ao barulho")
    print("3- Voltar pela porta em que cheguei")
    surprise_move = input('>')
    if "1" or "esconder" or "esconder-me" in surprise_move.lower():
        print('Você se esconde atrás do baú')
        print('o guarda entra na sala.')
        for i in range(3):
            print(''.join(['.' for _ in range(i + 1)]), end='\r')
            time.sleep(1)

    elif "2" or "correr" or "barulho" or "atacar" in surprise_move.lower():
        print('Você avança rapidamente em direção a porta, que bravura!')

    elif "3" or "voltar" or "porta" in surprise_move.lower():
        print('você')


