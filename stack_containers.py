from  typing import Union

class Stack():
    def __init__(self, capacity)-> None:
        self.__list = []
        self.capacity = capacity


    def fill(self) -> None:
        '''
        fill: llena la pila de acuerdo a la Capacidad 
        '''
        while self.size() < self.capacity:
            self.push(item=1)


    def unfill(self) -> None:
        '''
        unfill: Vacia la pila
        '''
        while not self.is_empty():
            self.pop()


    def push(self, item:int) -> None:
        '''
        push: Agrega un Elemento a la Pila
        Parametros:
           item: elemento a agregar a la Pila
        '''
        self.__list.append(item)


    def pop(self) -> Union[str, int]:
        '''
            pop: Elimina el último elemento de la Pila y lo retorna
        '''
        if self.__list == []:
            return 'Is Empty'
        else:
            return self.__list.pop()
    

    def peek(self) -> Union[int, None]:
        '''
            peek: retorna el último elemento de la Pila, sin eliminarlo
        '''
        if self.__list:
            return self.__list[-1]
        else:
            return None


    def is_empty(self) -> bool:
        '''
            is_empty: Determina si la pila está vacia
        '''
        return self.__list == []
   
    
    def size(self) -> int:
        '''
            size: Devuelve el número de elementos en la Pila
        '''
        return len(self.__list)