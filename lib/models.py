# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    vehicles = relationship('Vehicle', back_populates='user')

class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    vin = Column(String, unique=True, nullable=False)
    current_mileage = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='vehicles')
    maintenance_logs = relationship('MaintenanceLog', back_populates='vehicle')
    expenses = relationship('Expense', back_populates='vehicle')

class MaintenanceLog(Base):
    __tablename__ = 'maintenance_logs'
    
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    task = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    mileage = Column(Integer, nullable=False)
    description = Column(String)
    
    vehicle = relationship('Vehicle', back_populates='maintenance_logs')

class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    
    vehicle = relationship('Vehicle', back_populates='expenses')
