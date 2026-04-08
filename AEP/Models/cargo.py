from enum import Enum

class Cargo(Enum):
	CIDADAO = "Cidadao"
	FUNCIONARIO_PUBLICO = "Funcionario publico"

	def __str__(self):
		return self.value
