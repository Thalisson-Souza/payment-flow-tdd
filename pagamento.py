class Pagamento:

    def processar_pagamento(self, valor_pagamento, saldo_disponivel, metodo_pagamento):
        if not isinstance(valor_pagamento, (float, int)):
            raise TypeError("valor do pagamento não é um numero")
        
        if not isinstance(saldo_disponivel, (float, int)):
            raise TypeError("saldo disponível não é um número")

        if valor_pagamento <= 0:
            raise ValueError("valor do pagamento não pode ser negativo ou 0")
        

        if metodo_pagamento not in ("pix", "crédito", "débito"):
            raise ValueError("modalidade nao aceita agora...")

    
        valor_total = self.calcular_valor_total(valor_pagamento, metodo_pagamento)


        if valor_total > saldo_disponivel:
            raise ValueError("saldo insuficiente para o pagamento") 

        return {
            "valor_total": valor_total
        }


    def calcular_valor_total(self, valor_pagamento, metodo_pagamento):
        if metodo_pagamento != "crédito":
            return valor_pagamento
        taxa_cinco_porcento_no_credito = valor_pagamento * 0.05
        return valor_pagamento + taxa_cinco_porcento_no_credito
