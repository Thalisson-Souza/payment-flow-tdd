from unittest import TestCase
from pagamento import Pagamento

class TestFluxoPagamento(TestCase):
        
    def test_nao_deve_processar_pagamento_com_saldo_insuficiente(self):
        pagamento = Pagamento()
        saldo_insuficiente = 10
        self.assertRaises(ValueError, pagamento.processar_pagamento, 200, saldo_insuficiente, "pix")
    

    def test_deve_processar_pagamento_com_saldo_suficiente(self):
        pagamento = Pagamento()
        saldo_suficiente = 1000
        resultado = pagamento.processar_pagamento(100, saldo_suficiente, "pix")
        self.assertTrue(resultado)


    def test_nao_deve_processar_pagamento_com_tipo_invalido(self):
        pagamento = Pagamento()
        self.assertRaises(TypeError, pagamento.processar_pagamento, "cem", 500, "pix")


    def test_nao_deve_processar_pagamento_com_valor_negativo(self):
        pagamento = Pagamento()
        self.assertRaises(ValueError, pagamento.processar_pagamento, -10, 500, 'pix')


    def test_nao_deve_processar_pagamento_com_valor_zero(self):
        pagamento = Pagamento()
        self.assertRaises(ValueError, pagamento.processar_pagamento, 0, 500, "pix")


    def  test_nao_deve_processar_pagamento_com_saldo_zerado(self):
        pagamento = Pagamento()
        saldo_zerado = 0

        self.assertRaises(ValueError, pagamento.processar_pagamento, 200, saldo_zerado, "pix")

    
    def test_nao_deve_processar_pagamento_com_saldo_informado_de_tipo_invalido(self):
        pagamento = Pagamento()

        self.assertRaises(TypeError, pagamento.processar_pagamento, 100, "quinhentos", "pix")

    
    #“o sistema ainda não suporta método de pagamento”
    def test_deve_processar_pagamento_com_metodo_pix(self):
        pagamento = Pagamento()

        resultado = pagamento.processar_pagamento(100, 500, "pix")
        self.assertTrue(resultado)

    def test_nao_deve_processar_pagamento_com_metodo_invalido(self):
        pagamento = Pagamento()

        self.assertRaises(ValueError, pagamento.processar_pagamento, 100, 500, "boleto")

    def test_deve_processar_pagamento_com_metodo_cartao_de_credito(self):
        pagamento = Pagamento()

        resultado = pagamento.processar_pagamento(100, 500, "cartão de crédito")
        self.assertTrue(resultado)