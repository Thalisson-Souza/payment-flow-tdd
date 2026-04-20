from unittest import TestCase
from pagamento import Pagamento

class TestFluxoPagamento(TestCase):


    def test_nao_deve_processar_pagamento_com_cartao_sem_saldo(self):
        pagamento = Pagamento()

        self.assertRaises(Exception, pagamento.processar_pagamento, 0)

            
    def test_deve_processar_pagamento_com_sucesso(self):
        pagamento = Pagamento()

        resultado = pagamento.processar_pagamento(100)

        self.assertTrue(resultado)
