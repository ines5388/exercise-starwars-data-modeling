from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False) 
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    register_id = Column(Integer, ForeignKey('register.id'))
    favorites_characters = relationship('FavoriteCharacter', backref='users', lazy=True)
    favorites_planets = relationship('FavoritePlanet', backref='users', lazy=True)
    favorites_vehicles = relationship('FavoriteVehicle', backref='users', lazy=True)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    character_img = Column(String(500), nullable=True)
    favorites_characters = relationship('FavoriteCharacter', backref='characters', lazy=True)

class FavoriteCharacter(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    planets_img = Column(String(500), nullable=True)
    favorites_planets = relationship('FavoritePlanet', backref='planets', lazy=True)

class FavoritePlanet(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    vehicles_img = Column(String(500), nullable=True)
    favorites_vehicles = relationship('FavoriteVehicle', backref='vehicles', lazy=True)

class FavoriteVehicle(Base):
    __tablename__ = 'favorites_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
