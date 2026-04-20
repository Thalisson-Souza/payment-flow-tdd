from unittest import TestCase
from pagamento import Pagamento

class TestFluxoPagamento(TestCase):


    def test_nao_deve_processar_pagamento_com_cartao_sem_saldo(self):
        pagamento = Pagamento()


