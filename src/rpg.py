from heroi import Heroi
from dado import Dado
from caixa_de_encontro import CaixaDeEncontro

def main():
    # criando o dado para rolar durante o jogo
    dado = Dado()
    
    # criando inicialmente o heroi
    heroi = Heroi().com_dados(dados_habilidade=dado.rola_dados().total(),
                            dados_sorte=dado.rola_dados().total(),
                            dados_energia=dado.rola_dados(2).total())

    print(heroi)

    # comecando uma batalha
    batalha = CaixaDeEncontro(heroi, monstro_habilidade=10, monstro_energia=10)
    print(batalha.__str__())


    batalha.turno(dado.rola_dados(2).total(), dado.rola_dados(2).total())
    print('Pontos depois da batalha:')
    print(batalha.__str__())

    print('Heroi depois da batalha:')
    print(heroi)

    
if __name__ == '__main__':
    main()