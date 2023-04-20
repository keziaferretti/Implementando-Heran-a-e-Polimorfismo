

from pessoaFisica import PessoaFisica


class GrupoDeContribuintes():
    def __init__(self):
        self.__contribuintes = []
    
    def addContribuinte(self, ObjContribuinte):
        self.__contribuintes.append(ObjContribuinte)
    
    def getTotalImposto(self):
        totalImposto = 0
        for contruibuinte in self.__contribuintes:
            totalImposto += contruibuinte.calcImposto()
        return totalImposto
    
    def getPorcentagemContribuintesFeminino(self):
        contrFemenino = 0
        for contribuinte in self.__contribuintes:
            if isinstance(contribuinte, PessoaFisica) and contribuinte.getSexo() == "Feminino":
                contrFemenino += 1
        return (contrFemenino / len(self.__contribuintes)) * 100