class Pagamento:
    TAXA_CREDITO = 0.05

    def validar_pagamento(self, valor_pagamento, saldo_disponivel, metodo_pagamento):
        if not isinstance(valor_pagamento, (float, int)):
            raise TypeError("valor do pagamento não é um numero")
        
        if not isinstance(saldo_disponivel, (float, int)):
            raise TypeError("saldo disponível não é um número")

        if valor_pagamento <= 0:
            raise ValueError("valor do pagamento não pode ser negativo ou 0")
        

        if metodo_pagamento not in ("pix", "crédito", "débito"):
            raise ValueError("modalidade nao aceita agora...")

    
        valor_final = self._calcular_valor_final(valor_pagamento, metodo_pagamento)


        if valor_final > saldo_disponivel:
            raise ValueError("saldo insuficiente para o pagamento") 

        return {
            "valor_a_pagar": valor_final
        }


    def _calcular_valor_final(self, valor_base, metodo_pagamento):
        if metodo_pagamento != "crédito":
            return valor_base
        
        taxa_credito = valor_base * self.TAXA_CREDITO
        return valor_base + taxa_credito
