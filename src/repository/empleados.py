#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from .implement import Base



class Empleados(Base):
    """This class defines a user by various attributes."""

    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True)
    primer_nombre = Column(String(60), nullable=False)
    segundo_nombre = Column(String(60), nullable=True)
    primer_apellido = Column(String(60), nullable=False)
    segundo_apellido = Column(String(60), nullable=True)
    cedula = Column(String(60), nullable=False)
    area_a_ingresar = Column(String(60), nullable=True)
    telefono = Column(String(60), nullable=False)
    direccion_residencia = Column(String(60), nullable=True)
    ciudad = Column(String(60), nullable=True)
    usuario = Column(String(20), nullable=False)
    clave = Column(String(60), nullable=False)
