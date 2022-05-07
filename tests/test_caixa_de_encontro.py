import pytest

from src.caixa_de_encontro import CaixaDeEncontro
from src.heroi import Heroi
from src.heroi_morto_error import HeroiMortoError


class TestCaixaDeEncontro:

    def test_criatura_sendo_derrotada(self):
        c = CaixaDeEncontro(Heroi().com_dados(99, 99, 99), 3, 2)

        venceu = c.turno(99, 1)

        assert venceu is True


    def test_ninguem_morto(self):
        c = CaixaDeEncontro(Heroi().com_dados(99, 99, 99), 3, 99)

        venceu = c.turno(99, 99)

        assert venceu is False


    def test_heroi_morrendo(self):
        c = CaixaDeEncontro(Heroi(), 99, 99)

        with pytest.raises(HeroiMortoError):
            c.turno(1, 99)

