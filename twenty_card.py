import random
from  stack_cards import Stack
from utiles import Utiles

utiles = Utiles()

def show_cards(cards:list, card_round:str) -> None:
    '''
    show_cards: Función que se encarga de dibujar las cartas del Juego
    Parametros:
        cards: Cartas a mostrar
    '''
    # Por estética vertical debe ser par.  Y horizontal debe ser 2 * vertical
    utiles.blanK_lines(4)
    print(f' {card_round} {len(cards)} cards of deck')
    vertical:int = 3
    horizontal:int = vertical * 2
    
    espacio:int = int((horizontal-4)/2)
    for i in range(vertical):
        if i == 0:
            for j in range(len(cards)):
                print('┌'+'─'*(horizontal-2)+'┐   ', end='')
        elif i == vertical - 1:
            for j in range(len(cards)):
                print('└'+'─'*(horizontal-2)+'┘   ', end='')
        elif i == vertical//2:
            for j in range(len(cards)):
                print('│' + ' ' * espacio + cards[j] + ' ' * espacio + '│   ', end='') 
        else:
            for j in range(len(cards)):
                print('│' + ' ' * (horizontal - 2) + '│   ', end='')
        print('')


def twenty_cards(number:int) -> tuple[bool, int]:
    '''
    twenty_cards: Funcion que se encarga de la logica del Juego Twenty_Cards.  Es llamada desde el principal
                  main.py y devuelve un Booleano que le indica si GANO o NO y un Entero con la puntuacion del jugador
    Parametro:
        number: es el numero de cartas que eligió el usuario sacar
    
    .- lista con todas las posibles cartas entre 1 y 20
    .- Utilizo Strings en vez de valores númeicos para poder que todos sean de longitud 2
    .- y queden igual de centrados en las cartas

    VARIABLES A TOMAR EN CUENTA:
    gano:bool                 --> Regresara a main.py el resultado de ganar o perder partida segun criterios del homework
    selected_cards:list = []   -> contendra la lista de cartas que selecciono el jugador (la n primeras cartas)
    sum_exposed_cards:int = 0  -> sumatoria de selected_cards
    missing_cards_up_to_50:int = 0 -> Cuantas cartas pudiera haber sacado extras sin llegar a 50. En caso de haber ganado
    next_card:int = 0           -> se usa para ir sacando las cartas de a una, para llegar a 50. Al final se queda con la carta que sobrepasa los 50
    next_cards:list = []        -> Lista de cartas extras que hubiese podido sacar sin llegar a 50 
    puntuacion:int = 0          -> Puntuacion del jugador.. se calcula si gano.. de lo contrario se queda 0


    '''
    cards_list:list = ['01','02','03','04','05','06','07','08','09','10',
                       '11','12','13','14','15','16','17','18','19','20']
    # DECLARO E INICIALIZO VARIABLES
    gano:bool   
    selected_cards:list = [] 
    sum_exposed_cards:int = 0 
    missing_cards_up_to_50:int = 0 
    next_card:int = 0 
    next_cards:list = []  
    puntuacion:int = 0 

    # El mazo de cartas tiene una estructura de Pila
    deck_of_cards = Stack()

    
    # Crear Mazo con las 20 Cartas Pero Ordenadas Aleatoriamente
    for i in range(19,0,-1):
        card = cards_list.pop(random.randint(0,i))
        deck_of_cards.push(item=card)
    deck_of_cards.push(item=cards_list[0])
    
    # Saco del mazo de cartas la cantidad que pidió el Jugador
    for i in range(number):
        selected_cards.append(deck_of_cards.pop())

    # Llamo a la Función que muestra las cartas
    show_cards(cards=selected_cards, card_round='First')

    # Obtengo la sumatoria de las cartas Expuestas
    for i in range(len(selected_cards)):
        sum_exposed_cards += int(selected_cards[i])
    print(f'Sum of exposed cards --> {sum_exposed_cards}')
    
    gano:bool
    gano = True if sum_exposed_cards <= 50 else False

    
    
    if not gano: 
        return (gano,0)
    
    # Si no retorno en el If anterior entonces gano y continua el codigo
    # Ahora debo averiguar cuantas cartas hay en el mazo sin que todavia supere 50
    while True:
        #En este ciclo, el ultimo valor de next_card (que no entrara en el siguiente if) es la carta que sobrepasa los 50
        next_card = deck_of_cards.pop() 
        next_cards.append(next_card)
        if sum_exposed_cards + int(next_card) <= 50:
            sum_exposed_cards += int(next_card)
            missing_cards_up_to_50 += 1
        else:
            break

    show_cards(cards=next_cards, card_round='Next')
    print(f'With the card -->{next_card} the sum exceeds 50')
    
    puntuacion = 10 - missing_cards_up_to_50

    return (gano, puntuacion)



