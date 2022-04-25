# pylint: disable=import-outside-toplevel, unused-import
""" Aplication Factory """



from time import process_time_ns


def init_app():
    """
    O banco de dodos é manipulado através da biblioteca
    SQLAlchemy. Todos os arquivos para interação com
    o banco de dados esta em ./src/database/, sendo que
    dentro desse diretorio existe outras duas pastas essenciais,
    que são:
    ../models que contens os models da aplicão e
    ../querys que contem as interações com o banco de dados


    SQLAlchemy - Website: https://www.sqlalchemy.org/

    """

    from .database import DBConnectionHendler
    from .database import models
    from .database import Base

    db_connection = DBConnectionHendler()
    engine = db_connection.get_engine()

    Base.metadata.create_all(engine)

    # Exemplo de uso
    from .database.querys import ExempleQuerys

    # Criando um Exemplo
    print("\n Criando exemplo \n")
    ExempleQuerys.new(name="marianoTupa")

    # Mostrando todos os exemplos
    print(" Todos os exemplos!")
    exemplos = ExempleQuerys.get_all()
    print(exemplos)

    # Deletando Exemplo
    print("\n deletando exemplo!")
    ExempleQuerys.delete(1)

    # Mostrando todos os exemplos
    print("\n Todos os exemplos:")
    exemplos = ExempleQuerys.get_all()
    print(exemplos)
