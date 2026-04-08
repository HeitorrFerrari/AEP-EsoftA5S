from enum import Enum
from Models.tipoCategoria import TipoCategoria
from Models.tipoIdentificacao import TipoIdentificacao


class Categoria:

    def __init__(self, tipo_categoria: TipoCategoria, descricao: str, opcao: TipoIdentificacao):
        self.tipo_categoria = tipo_categoria
        self.descricao = descricao
        self.opcao = opcao