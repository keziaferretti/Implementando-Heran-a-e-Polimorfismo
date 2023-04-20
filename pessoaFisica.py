from contribuinte import ContribuinteAbstrato

class PessoaFisica(ContribuinteAbstrato):
    def __init__(self, nome, documento, rendaBruta,sexo):
        super().__init__(nome, documento, rendaBruta)
        self._sexo = sexo

    def getSexo(self):
        return self._sexo
    
    def calcImposto(self):
        if self._rendaBruta <= 1400:
            imposto = 0
        elif self._rendaBruta <= 2100:
            imposto = (self._rendaBruta * 0.10) - 100
        elif self._rendaBruta <= 2800:
            imposto = (self._rendaBruta * 0.15) - 270
        elif self._rendaBruta <= 3600:
            imposto = (self._rendaBruta * 0.25) - 500
        else: 
            imposto = (self._rendaBruta * 0.30) - 700 
        return imposto
        