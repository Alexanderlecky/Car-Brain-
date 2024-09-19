# seed.py
from models import User, Vehicle, MaintenanceLog, Expense, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

# Database Setup
engine = create_engine('sqlite:///car_brain.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)

# Seed Data
def seed_data():
    # Add Users
    user1 = User(name="John Doe", email="john.doe@gmail.com")
    user2 = User(name="Jane Smith", email="jane.smith@gmail.com")
    user3 = User(name="Khalid Ali", email="khalid.ali@gmail.com")
    user4 = User(name="Alexander Karanja", email="alexnder.karanja@gmail.com")
    user5 = User(name="Sufyaan Jibril", email="sufyaan.jibril@gmail.com")
    user6 = User(name="Ismail Hani", email="ismail.hani@gmail.com")
    user7 = User(name="Ruth Kamau", email="ruth.kamau@gmail.com")

    session.add_all([user1, user2, user3, user4, user5, user6, user7])
    session.commit()

    # Add Vehicles
    vehicle1 = Vehicle(make="Toyota", model="Corolla", year=2020, vin="1HGBH41JXMN109186", current_mileage=15000, user=user1)
    vehicle2 = Vehicle(make="Honda", model="Civic", year=2019, vin="2HGCM82633A123456", current_mileage=22000, user=user2)
    vehicle3 = Vehicle(make="BMW", model="M4", year=2017, vin="2HGCM82733B124456", current_mileage=220000, user=user3)
    vehicle4 = Vehicle(make="Nissan", model="Note", year=2018, vin="2BJCM82633A124577", current_mileage=22000, user=user4)
    vehicle5 = Vehicle(make="RR", model="Ghost", year=2022, vin="4ADER82633A123490", current_mileage=22000, user=user5)
    vehicle6 = Vehicle(make="Alpina", model="BMW G82", year=2019, vin="2HGCM82633A123456", current_mileage=1754, user=user6)
    vehicle7 = Vehicle(make="Lamboghini", model="Urus", year=2024, vin="2HGCM82633A134578", current_mileage=45896, user=user7)

    session.add_all([vehicle1, vehicle2, vehicle3, vehicle4, vehicle5, vehicle6, vehicle7])
    session.commit()

    # Add Maintenance Logs
    log1 = MaintenanceLog(vehicle_id=vehicle1.id, task="Oil Change", date=datetime.date(2023, 1, 10), mileage=15000)
    log2 = MaintenanceLog(vehicle_id=vehicle2.id, task="Tire Rotation", date=datetime.date(2023, 2, 15), mileage=22000)
    log3 = MaintenanceLog(vehicle_id=vehicle3.id, task="Brake Check", date=datetime.date(2023, 3, 20), mileage=220000)
    log4 = MaintenanceLog(vehicle_id=vehicle4.id, task="Inspection", date=datetime.date(2023, 4, 25), mileage=22000)
    log5 = MaintenanceLog(vehicle_id=vehicle5.id, task="Oil Change", date=datetime.date(2023, 5, 10), mileage=22000)
    log6 = MaintenanceLog(vehicle_id=vehicle6.id, task="Tire Rotation", date=datetime.date(2023, 6, 15), mileage=1754)
    log7 = MaintenanceLog(vehicle_id=vehicle7.id, task="Brake Check", date=datetime.date(2023, 7, 20), mileage=45896)

    session.add_all([log1, log2, log3, log4, log5, log6, log7])
    session.commit()

    print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()
