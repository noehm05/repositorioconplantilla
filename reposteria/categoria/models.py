"""Modelos de datos para las categorías de la repostería."""

from reposteria.database import Column, PKModel, db


class Categoria(PKModel):
    """Representa una categoría de productos."""

    __tablename__ = "categorias"

    nombre = Column(db.String(100), nullable=False, unique=True)
    descripcion = Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        """Devuelve una representación de la categoría."""
        return f"Categoria(nombre={self.nombre!r}, descripcion={self.descripcion!r})"
