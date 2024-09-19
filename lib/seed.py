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
    user1 = User(name="John Doe", email="john.doe@example.com")
    user2 = User(name="Jane Smith", email="jane.smith@example.com")

    session.add_all([user1, user2])
    session.commit()

    # Add Vehicles
    vehicle1 = Vehicle(make="Toyota", model="Corolla", year=2020, vin="1HGBH41JXMN109186", current_mileage=15000, user=user1)
    vehicle2 = Vehicle(make="Honda", model="Civic", year=2019, vin="2HGCM82633A123456", current_mileage=22000, user=user2)

    session.add_all([vehicle1, vehicle2])
    session.commit()

    # Add Maintenance Logs
    log1 = MaintenanceLog(vehicle_id=vehicle1.id, task="Oil Change", date=datetime.date(2023, 1, 10), mileage=15000)
    log2 = MaintenanceLog(vehicle_id=vehicle2.id, task="Tire Rotation", date=datetime.date(2023, 2, 15), mileage=22000)

    session.add_all([log1, log2])
    session.commit()

    print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()
