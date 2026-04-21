class Pagamento:

    def processar_pagamento(self, limite):
        if not isinstance(limite, (float, int)):
            raise TypeError("limite deve ser um numero")

        if limite <= 0:
            raise ValueError("sem limite pra processar pagamento")
        
        
        return True
    

