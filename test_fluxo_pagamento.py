from unittest import TestCase
from pagamento import Pagamento

class TestFluxoPagamento(TestCase):
            
    def test_deve_processar_pagamento_com_sucesso(self):
        pagamento = Pagamento()

        resultado = pagamento.processar_pagamento(100)

        self.assertTrue(resultado)

    def test_nao_deve_processar_pagamento_com_valor_negativo(self):
        pagamento = Pagamento()

        self.assertRaises(ValueError, pagamento.processar_pagamento, 0)


    def test_nao_deve_processar_com_tipo_invalido(self):
        pagamento = Pagamento()

        self.assertRaises(TypeError, pagamento.processar_pagamento, "cem")
        

    