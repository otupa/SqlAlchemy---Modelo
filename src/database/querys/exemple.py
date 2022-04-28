# pylint: disable=unused-argument, no-member, arguments-differ
"""User Querys"""

from typing import List
from src.database.models import Exemple
from src.database import db_connector

from .interface import QuerysInterface


class Querys(QuerysInterface):
    """Aqui estão as consultas no banco de dados e CRUDs"""

    @classmethod
    @db_connector
    def get_all(cls, connection) -> List:
        """Pega todos os exemplos na tabela"""
        query = connection.session.query(Exemple).all()
        return query

    @classmethod
    @db_connector
    def create(cls, connection, arg):
        """Cria um novo exemplo"""
        check_name = (
            connection.session.query(Exemple).filter_by(name=arg).first()
        )
        if check_name is None:
            new_user = Exemple(name=arg)
            connection.session.add(new_user)
            connection.session.commit()

    @classmethod
    @db_connector
    def get_id(cls, connection, arg):
        """Pesquisa um exemplo pelo id"""
        return connection.session.query(Exemple).filter_by(id=arg).first()

    @classmethod
    @db_connector
    def delete(cls, connection, arg):
        """Deleta umm exemplo"""
        exemple = connection.session.query(Exemple).filter_by(id=arg).first()
        connection.session.delete(exemple)
        connection.session.commit()

    @classmethod
    @db_connector
    def update(cls, connection, arg1, arg2):
        """Deleta umm exemplo"""

        query = (
            connection.session.query(Exemple)
            .filter_by(id=arg1)
            .first()
        )

        query.update(name=arg2)
