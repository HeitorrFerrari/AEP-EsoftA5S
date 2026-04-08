from enum import Enum

class TipoIdentificacao(Enum):
    IDENTIFICADO = "Identificado"
    ANONIMO = "Anonimo"

    def __str__(self):
        return self.value
