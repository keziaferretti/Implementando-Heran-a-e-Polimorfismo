
from abc import ABC
import abc


class ContribuinteAbstrato(ABC):
    def __init__(self, nome,documento, rendaBruta):
        self.__nome = nome
        self.__documento = documento
        self._rendaBruta = rendaBruta
    
    def getNome(self):
        return self.__nome
    def setNumero(self, nome):
        self._nome = nome
    
    def getDoc(self):
        return self.__documento
    def setDoc(self, __documento):
        self.__documento = __documento
    
    def getRendaBruto(self):
        return self._rendaBruta
    def setRendaBruto(self, _rendaBruta):
        self._rendaBruta = _rendaBruta

    @abc.abstractmethod
    def calcImposto():
        pass