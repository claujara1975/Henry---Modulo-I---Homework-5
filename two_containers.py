from stack_containers import Stack
from utiles import Utiles

'''
Utiles:  clase Utiles, importada del modulo utiles, la caul posee metodos para borrar pantalla,
         imprimir lineas en blanco, verificar si existen archivos, desplegar menus, etc

Stack:   calse Stack importada del modulo stack_containers, Estructura de datos a usar en el ejercicio

VARIABLES
container_3 --> Variable tipo Stack donde se llevara el control del contenedor de 3 Litros
container_5 --> Variable tipo Stack donde se llevara el control del contenedor de 3 Litros
show_3      --> Variable tipo Diccionario donde se Guardaran los caracteres (░ o espacios en blanco)
                correspondientes para representar graficamente el contenedor de 3 litros
show_5      --> Variable tipo Diccionario donde se Guardaran los caracteres (░ o espacios en blanco)
                correspondientes para representar graficamente el contenedor de 5 litros
'''

# DECLARACION DE VARIABLES
utiles = Utiles()

container_3 = Stack(capacity=3)
container_5 = Stack(capacity=5)
 
show_5:dict = {0:'       ', 1:'       ', 2:'       ', 3:'       ', 4:'       ', 'content': '0 liters'}
show_3:dict = {0:'       ', 1:'       ', 2:'       ', 'content': '0 liters'}

def show_containers() -> None:
    '''
    show_containers: Representacion Grafica del estado de los containers
    '''
    liters_5:str = show_5['content']
    liters_3:str = show_3['content']
    print('             ┌'+'───────'+'┐')
    print('             │' + show_5[4] + '│')
    print('             │' + show_5[3] + '│    ' + '┌'+'───────'+'┐')
    print('             │' + show_5[2] + '│    ' + '│' + show_3[2] + '│')
    print('             │' + show_5[1] + '│    ' + '│' + show_3[1] + '│')
    print('             │' + show_5[0] + '│    ' + '│' + show_3[0] + '│')
    print('             └'+'───────'+'┘    ' + '└'+'───────'+'┘')
    print(f'             {liters_5}     {liters_3}')

def fill_containers_dicts(number:int, container:int):
    '''
        fill_containers_dicts: Asigna los valores String a los diccionarios necesarios para la representacion grafica
        parametros:
            number: representa la cantidad de valores del diccionario a los que se les asignara 7*"░"
            container: indica a que container hace mencion
    '''
    show_5['content'] = str(container_5.size()) + ' Liters'
    show_3['content'] = str(container_3.size()) + ' Liters'
    for i in range(number):
        if container == 5:
            show_5[i] = '░' * 7
        else:
            show_3[i] = '░' * 7
    if number < container:
        for i in range(number,container):
            if container == 5:
                show_5[i] = ' ' * 7    
            else:
                show_3[i] = ' ' * 7

def display_screen(gano:bool=False) -> int:
    '''
    display_screen: Funcion que se encarga de renderizar Toda la pantalla y lee la opcion del usuario
    Atributo:
        gano: atributo booleano. Se usa para poder renderizar una vez haya ganado el usuario y retornar inmediatamente
              sin esperar opcion del usuario
    '''
    option:int = 0
    menu_containers_game = f'''
                             TWO CONTAINERS GAME
                           YOU HAVE ONLY 20 ATTEMPT

    OPTIONS:

    1. Fill 3 liters Container
    2. Fill 5 liters Container
    3. Unfill 3 liters Container
    4. Unfill 5 liters Container
    5. Add the contents of the 3 liter Container ​​into the 5 liter Container.
    6. Add the contents of the 5 liter Container ​​into the 3 liter Container.

    Please enter an option: '''

    while True:
        utiles.limpiar_pantalla()
        utiles.blanK_lines(4)
        show_containers()
        print(menu_containers_game, end='')

        # Si el usuario ya encontro la solucion (Ganó) despues de renderizar retorna a la funcion que lleva la logica de la app
        if gano: return 0
        
        response = input()
        if response.strip() in ['1','2','3','4','5','6']:
            option = int(response.strip())
            return option
        else: 
            utiles.blanK_lines(2)
            print('OPCION NO VALIDA')
            input()


def two_containers() -> tuple:
    '''
    two_containers: Funcion que se encarga de llevar la logica del Juego TWO_CONTAINERS, es llamada desde la app.py
                    y retorna en un booleano, si el usuario GANO o NO, y el NUMERO DE INTENTOS
    '''
    add:int = 0
    option:int = 0
    attempts:int = 0
    while True:
        attempts += 1
        option = display_screen()

        if option == 1: container_3.fill()
        
        if option == 2: container_5.fill()
        
        if option == 3: container_3.unfill()
            
        if option == 4: container_5.unfill()
            
        if option == 5:
            add = container_3.size()
            while add > 0 and container_5.size() < 5:
                add -= 1
                container_5.push(1)
                container_3.pop()

        if option == 6:
            add = container_5.size()
            while add > 0 and container_3.size() < 3:
                add -= 1
                container_3.push(1)
                container_5.pop()
       
        fill_containers_dicts(number = container_3.size(), container = 3)
        fill_containers_dicts(number = container_5.size(), container = 5)
   
        if attempts == 20: return (False, 0)

        if container_5.size() == 4: 
            option = display_screen(gano = True)
            return (True, attempts)


