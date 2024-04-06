from utiles import Utiles
from twenty_card import twenty_cards
from two_containers import two_containers

import sys

'''
twenty_cards:   Función que importo del modulo twenty_card que controla la lógica del juego de cartas
two_containers: Función que importo del modulo Two_containers que controla la lógica del juego de Contenedores
Utiles:         Clase que tiene metodos varios de apoyo, para limpiar pantala, agregar lineas en blanco, 
                inicializar el logger, verificar si un archivo especifico existe, desplegar un menu general, etc

                

'''

utiles = Utiles()

utiles.verificar_existe(path_file='./logs/app.log')
logger = utiles.init_logger()


mensaje:list = ['Please enter an option: ',
                'Please enter the number of cards ']

ejecutar_funciones:list = ['twenty_cards(number = number_of_cards)',
                           'two_containers()'
                           ]
response:str
def main():
    '''
    main: Funcion main, del archivo main de la Aplicacion... Logica Central de todo
    '''
    gano: bool
    opcion:int = 0
    number_of_cards:int
    while(True):
        response = utiles.desplegar_menu(opcion=opcion, mensaje=mensaje[opcion])
        if response.strip() == '3': sys.exit(0)
        if response.strip() in ['1','2']: 
            opcion = int(response)
            break
    
    if opcion == 1:
        while True:
            response = utiles.desplegar_menu(opcion=opcion, mensaje=mensaje[opcion])  
            try:
                number_of_cards = int(response.strip())
                break
            except: pass


    gano,puntuacion = eval(ejecutar_funciones[opcion-1])
    utiles.blanK_lines(2)
    if opcion == 1:
        logger.info(f'you WON with a score of --> {puntuacion}' if gano else 'you LOST...')
    else:
        logger.info(f'yoy WON... you needed {puntuacion} attempts' if gano else 'you LOST...')
    utiles.blanK_lines(2)
    


if __name__=='__main__':
    main()