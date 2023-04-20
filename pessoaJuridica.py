from contribuinte import ContribuinteAbstrato

class PessoaJuridica(ContribuinteAbstrato):
    def __init__(self, nome, documento, rendaBruta,anoDeFundacao):
        super().__init__(nome, documento, rendaBruta)
        self.__anoDeFundacao = anoDeFundacao
    
    def getAnoDeFund(self):
        return self.__anoDeFundacao
    
    def calcImposto(self):
        imposto = (self._rendaBruta * 0.10)
        return imposto
    