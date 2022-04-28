# pylint: disable=too-few-public-methods
# pylint: disable=singleton-comparison, no-member, unused-argument, unnecessary-ellipsis

"""Interfaces de Querys"""

from abc import ABC, abstractclassmethod
from ast import List


class QuerysInterface(ABC):
    """Interfaces de Querys"""

    @classmethod
    @abstractclassmethod
    def get_all(cls) -> List:
        """
        Retorna todos os registros do banco de dados.
        """
        ...

    @classmethod
    @abstractclassmethod
    def create(cls) -> None:
        """Cria um novo registro."""
        ...

    @classmethod
    @abstractclassmethod
    def update(cls) -> None:
        """Atualiza um registro."""
        ...

    @classmethod
    @abstractclassmethod
    def delete(cls) -> None:
        """Deleta um Registro"""
        ...
