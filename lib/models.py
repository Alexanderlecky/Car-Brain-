
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    vehicles = relationship('Vehicle', back_populates='owner')

class Vehicle(Base):
    __tablename__ = 'vehicles'
    vehicle_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    vin = Column(String)
    current_mileage = Column(Integer)
    purchase_date = Column(Date)

    owner = relationship('User', back_populates='vehicles')
    maintenance_logs = relationship('MaintenanceLog', back_populates='vehicle')
    expenses = relationship('Expense', back_populates='vehicle')

class MaintenanceLog(Base):
    __tablename__ = 'maintenance_log'
    maintenance_id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    task = Column(String)
    date = Column(Date)
    mileage = Column(Integer)
    description = Column(String)

    vehicle = relationship('Vehicle', back_populates='maintenance_logs')

class Expense(Base):
    __tablename__ = 'expenses'
    expense_id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    expense_type = Column(String)
    amount = Column(Float)
    date = Column(Date)
    description = Column(String)

    vehicle = relationship('Vehicle', back_populates='expenses')
