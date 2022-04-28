"""Models para Exemplo"""


from sqlalchemy import String, Column, Integer

from src.database import Base


class Exemple(Base):
    """Exemple Table"""

    __tablename__ = 'exemple'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
