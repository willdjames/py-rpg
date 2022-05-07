from heroi import Heroi
from src.heroi_morto_error import HeroiMortoError

class CaixaDeEncontro:
    
    def __init__(self, heroi: Heroi, monstro_habilidade: int, monstro_energia: int):
        print('iniciando batalha...')
        
        self._heroi = heroi
        self._monstro_habilidade = monstro_habilidade
        self._monstro_energia = monstro_energia


    def __str__(self) -> str:
        return 'Batalha:' + str(self.__dict__)
    

    def turno(self, dados_heroi: int, dados_monstro: int) -> bool:
        is_criatura_derrotada = False

        monstro_forca_ataque = dados_monstro + self._monstro_habilidade
        heroi_forca_ataque = dados_heroi + self._heroi.get_habilidade()

        print(f'monstro_forca_ataque {monstro_forca_ataque}; heroi_forca_ataque: {heroi_forca_ataque}')

        if heroi_forca_ataque > monstro_forca_ataque:
            self.__criatura_leva_dano()
        elif monstro_forca_ataque > heroi_forca_ataque:
            self.__heroi_leva_dano()

        if self._monstro_energia <= 0:
            is_criatura_derrotada = True
        elif self._heroi.get_energia() <= 0:
            raise HeroiMortoError

        return is_criatura_derrotada


    def __criatura_leva_dano(self, pontos_dano = 2) -> None:
        print('heroi feriu a criatura')
        self._monstro_energia = self._monstro_energia - pontos_dano

    
    def __heroi_leva_dano(self, pontos_dano = 2) -> None:
        print('criatura feriu o heroi')
        self._heroi.leva_dano(pontos_dano)


if __name__ == '__main__':
    CaixaDeEncontro(Heroi(), 5, 5).turno(7, 8)

