class Pagamento:

    def processar_pagamento(self, valor_pagamento, saldo_disponivel):
        if not isinstance(valor_pagamento, (float, int)):
            raise TypeError("valor do pagamento não é um numero")
        
        if not isinstance(saldo_disponivel, (float, int)):
            raise TypeError("saldo disponível não é um número")

        if valor_pagamento <= 0:
            raise ValueError("valor do pagamento não pode ser negativo ou 0")
        
        if valor_pagamento > saldo_disponivel:
            raise ValueError("saldo insuficiente para o pagamento")        

        
        return True
    

