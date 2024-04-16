from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Register(Base): 
    __tablename__ = 'register'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

class LogIn(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    success = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    register_id = Column(Integer, ForeignKey('register.id'))

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    character_img = Column(String(500), nullable=True)

class FavoriteCharacter(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_relantionship = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters_relantionship = relationship(Character)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    planets_img = Column(String(500), nullable=True)

class FavoritePlanet(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_relantionshiop = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_relationship = relationship(Planet)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    vehicles_img = Column(String(500), nullable=True)

class FavoriteVehicle(Base):
    __tablename__ = 'favorites_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_relantionshiop = relationship(User)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles_relationship = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
