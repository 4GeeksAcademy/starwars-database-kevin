import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    contrasenia = Column(String(250), nullable=False)
    fecha_suscrip = Column(datetime, nullable=False, default=datetime.utcnow)
    # Relación uno a muchos con Favorite
    favorites = relationship('Favorite', back_populates='usuario')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship('Usuario', back_populates='favorites')
    
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character')
    
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet')
    
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship('Vehicle')

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
