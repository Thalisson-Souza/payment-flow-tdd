class Pagamento:

    def processar_pagamento(self, limite):
        if not isinstance(limite, (float, int)):
            raise TypeError("limite deve ser um numero")


        limiteMax = 100000
        if limite > limiteMax:
            raise ValueError("limite máximo excedido")


        if limite <= 0:
            raise ValueError("sem limite pra processar pagamento")
        
        
        return True
    

