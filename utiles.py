import os
import logging

class Utiles():
    def __init__(self) -> None:
        pass

    def verificar_existe(self, path_file:str, header:str=None) -> None:
        '''
        Comprueba si un archivo  existe y de no existir lo crea y añade los encabezados de columnas
        si el parametro header no es None 
        parametros: path_file: path del archivo, header: encabezado de columnas
        '''
        if header is None: header = ''
        if not os.path.exists(path_file): 
            archivo = open(path_file,'w', encoding="utf-8")
            archivo.write(header)
            archivo.close()

    def init_logger(self):
        '''
        init_logger: Inicializa el logger
        '''
        # Crear un objeto logger
        logger = logging.getLogger(__name__)

        # Establecer el nivel de registro
        logger.setLevel(logging.DEBUG)

        # Crear un manejador de archivos
        file_handler = logging.FileHandler('./logs/app.log')

        # Establecer el formato del registro
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Crear un manejador de consola
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Agregar los manejadores de archivos y consola al logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
    
    def limpiar_pantalla(self) -> None:
        '''
        limpiar_pantalla: Limpia la pantalla de la terminal
        '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def blanK_lines(self, number:int) ->None: 
        '''
        blanK_lines: Agrega lineas en blanco en la terminal
        '''
        for i in range(number): 
            print('')

    def desplegar_menu(self,opcion:int=0, mensaje:str='') -> str:
        '''
        desplegar_menu: Apoyo al modulo main desplegando el menu inicial de la app
        '''
        response:str
        opciones:list = [' ',' ',' ']
        if opcion != 0:
            opciones[opcion-1] = '►' #alt 272
            
        menu:str = f'''
                                HOMEWORK OF LECTURE 5
                                   START THE GAME

        {opciones[0]} 1. Twenty Card Game
        {opciones[1]} 2. Three and Five Liter Containers
 
        {opciones[2]} 3. Exit

        {mensaje}'''
        self.limpiar_pantalla()
        response = input(menu)
        return response