class Pagamento:

    def processar_pagamento(self, limite):
        #raise Exception("não tem limite suficiente")
        if limite <= 0:
            raise Exception("sem limite pra processar pagamento")
        return True
    

    