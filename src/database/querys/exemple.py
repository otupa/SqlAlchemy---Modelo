# pylint: disable=consider-using-f-string
# pylint: disable=bare-except
# pylint: disable=too-few-public-methods
# pylint: disable=too-few-public-methods
# pylint: disable=singleton-comparison
""" User Querys"""

from typing import List
from src.database.db_connection import DBConnectionHendler
from src.database.models import Exemple


class ExempleQuerys:
    """Aqui estão as consultas no banco de dados e CRUDs"""

    @classmethod
    def get_all(cls) -> List:
        """Retorna todos os exempls na base de dados"""
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Exemple).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


    @classmethod
    def new(cls, name):
        """Cria um novo exemplo"""
        with DBConnectionHendler() as db_connection:
            try:
                check_name = (
                    db_connection.session.query(Exemple).filter_by(name=name).first()
                )
                if check_name == None:
                    new_user = Exemple(name=name)
                    db_connection.session.add(new_user)
                    db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_id(cls, _id):
        """Pesquisa um exemplo pelo id"""
        with DBConnectionHendler() as db_connection:
            try:
                return (
                    db_connection.session.query(Exemple).filter_by(id=_id).first()
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def delete(cls, exemple_id):
        """Deleta umm exemplo"""
        with DBConnectionHendler() as db_connection:
            try:
                exemple = (
                    db_connection.session.query(Exemple)
                    .filter_by(id=exemple_id)
                    .first()
                )
                db_connection.session.delete(exemple)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
