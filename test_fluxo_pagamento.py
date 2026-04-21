from unittest import TestCase
from pagamento import Pagamento

class TestFluxoPagamento(TestCase):
            
    def test_deve_processar_pagamento_com_sucesso(self):
        pagamento = Pagamento()

        resultado = pagamento.processar_pagamento(100)

        self.assertTrue(resultado)


    def test_nao_deve_processar_pagamento_com_valor_negativo(self):
        pagamento = Pagamento()

        self.assertRaises(ValueError, pagamento.processar_pagamento, -10)

    def test_nao_deve_processar_pagamento_com_valor_zerado(self):
        pagamento = Pagamento()

        self.assertRaises(ValueError, pagamento.processar_pagamento, 0)

    def test_deve_processar_pagamento_com_valor_quebrado(self):
        pagamento = Pagamento()

        resultado = pagamento.processar_pagamento(99.90)

        self.assertTrue(resultado)

    def test_deve_processar_pagamento_com_valor_minimo_permitido(self):
        pagamento = Pagamento()

        resultado = pagamento.processar_pagamento(0.01)

        self.assertTrue(resultado)

    def test_nao_deve_processar_pagamento_acima_do_teto_maximo(self):
        pagamento = Pagamento()
        valor_acima_teto = 100000.01

        self.assertRaises(ValueError, pagamento.processar_pagamento, valor_acima_teto)


    def test_nao_deve_processar_com_tipo_invalido(self):
        pagamento = Pagamento()

        self.assertRaises(TypeError, pagamento.processar_pagamento, "cem")
        

    