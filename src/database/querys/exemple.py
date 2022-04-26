# : disable=consider-using-f-string
# : disable=bare-except
# : disable=too-few-public-methods
# : disable=too-few-public-methods
# pylint: disable=singleton-comparison, no-member, unused-argument, bad-classmethod-argument
""" User Querys"""

from typing import List
from src.database.models import Exemple
from src.database import db_connector


class ExempleQuerys:
    """Aqui estão as consultas no banco de dados e CRUDs"""

    @classmethod
    @db_connector
    def get_all(connection, arg1, arg2=None) -> List:
        """Pega todos os exemplos na tabela"""
        query = connection.session.query(Exemple).all()
        return query


    @classmethod
    @db_connector
    def new(connection, arg1, arg2=None):
        """Cria um novo exemplo"""
        print(arg2)

        check_name = (
            connection.session.query(Exemple).filter_by(name=arg2).first()
        )
        if check_name == None:
            new_user = Exemple(name=arg2)
            connection.session.add(new_user)
            connection.session.commit()


    @classmethod
    @db_connector
    def get_id(connection, arg1, arg2=None):
        """Pesquisa um exemplo pelo id"""
        return connection.session.query(Exemple).filter_by(id=arg2).first()


    @classmethod
    @db_connector
    def delete(connection, arg1, arg2=None):
        """Deleta umm exemplo"""
        exemple = (
            connection.session.query(Exemple)
            .filter_by(id=arg2)
            .first()
        )
        connection.session.delete(exemple)
        connection.session.commit()
        
    
    @classmethod
    @db_connector
    def nova(connection, arg1, arg2=None):
        """Deleta umm exemplo"""
        query = connection.session.query(Exemple).all()
        return query
