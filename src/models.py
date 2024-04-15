import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Register(Base): 
    __tablename__ = 'register'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    date_suscription = ()
    email = Column(String(250), unique=True)
    username = Column(String(25), unique=True)
    password = Column(String(50), nullable=False)

class LogIn(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    success = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    register_id = Column(Integer, ForeignKey('register.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    character_img = Column(String(500), nullable=True)
    favorites_character = relationship('favorites_characters', backref = 'characters', lazy=True)

class FavoritesCharacters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_relantionship = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    characters_relantionship = relationship(Characters)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    planets_img = Column(String(500), nullable=True)

class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_relantionshiop = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    planets_relationship = relationship(Planets)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    vehicles_img = Column(String(500), nullable=True)

class FavoritesVehicles(Base):
    __tablename__ = 'favorites_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_relantionshiop = relationship(User)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    vehicles_relationship = relationship(Vehicles)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
