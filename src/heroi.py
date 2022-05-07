class Heroi:

    def __init__(self) -> None:
        self._habilidade_inicial = 0
        self._energia_inicial = 0
        self._sorte_inicial = 0
            
        self._habilidade = 0
        self._energia = 0

        print('Criando heroi...')


    def __str__(self) -> str:
        return 'Heroi:' + str(self.__dict__)

    
    def com_dados(self, dados_energia, dados_habilidade, dados_sorte):
        self._energia_inicial = dados_energia + 12
        self._habilidade_inicial = dados_habilidade + 6
        self._sorte_inicial = dados_sorte + 6

        self._energia = self._energia_inicial
        self._habilidade = self._habilidade_inicial

        return self


    def get_habilidade(self) -> int:
        return self._habilidade


    def get_energia(self) -> int:
        return self._energia


    def leva_dano(self, pontos_dano) -> None:
        self._energia = self._energia - pontos_dano


if __name__ == '__main__': 
    Heroi()

