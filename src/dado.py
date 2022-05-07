import random


class Dado():

    def __init__(self) -> None:
        self._valores_dados = []
        print('Criando dado...')


    def __str__(self) -> str:
        return 'Dado:' + str(__dict__)

    
    def __rola_dado(self) -> int:
        v = random.randint(a=1, b=6)
        print(f'dado: {v}')
        return v
    
    
    def rola_dados(self, n=1):
        self._valores_dados = []
        
        while(n > 0):
            self._valores_dados.append(self.__rola_dado())
            n = n - 1

        return self
    

    def total(self) -> int:
        return sum(self._valores_dados)


if __name__ == '__main__':
    Dado()

