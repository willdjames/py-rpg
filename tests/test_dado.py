from src.dado import Dado


class TestDado:


    def test_rola_um_dado(self):
        dado = Dado()
        numero = dado.rola_dados().total()

        assert numero <= 6


    def test_total_sem_rolar_dado(self):
        dado = Dado()
        numero = dado.total()

        assert numero is 0