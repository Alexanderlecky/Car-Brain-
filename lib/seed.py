# seed.py
from models import User, Vehicle, MaintenanceLog, Expense, FuelEfficiency, Reminder, Base
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

    # Add Expenses
    expense1 = Expense(vehicle_id=vehicle1.id, description="New Tires", amount=500.00, date=datetime.date(2023, 3, 5))
    expense2 = Expense(vehicle_id=vehicle2.id, description="Brake Pads", amount=300.00, date=datetime.date(2023, 4, 12))
    expense3 = Expense(vehicle_id=vehicle3.id, description="Oil Change", amount=1000.00, date=datetime.date(2023, 5, 8))
    expense4 = Expense(vehicle_id=vehicle4.id, description="New Engine", amount=1500.00, date=datetime.date(2023, 6, 15))
    expense5 = Expense(vehicle_id=vehicle5.id, description="New Tires", amount=500.00, date=datetime.date(2023, 3, 5))
    expense6 = Expense(vehicle_id=vehicle6.id, description="Brake Pads", amount=300.00, date=datetime.date(2023, 4, 12))
    expense7 = Expense(vehicle_id=vehicle7.id, description="Oil Change", amount=1000.00, date=datetime.date(2023, 5, 8))

    session.add_all([expense1, expense2, expense3, expense4, expense5, expense6, expense7])
    session.commit()


    # Add Fuel Efficiency Logs
    fuel1 = FuelEfficiency(vehicle_id=vehicle1.id, date=datetime.date(2023, 2, 1), mileage=15000, fuel_used=10.0, efficiency=30.0)
    fuel2 = FuelEfficiency(vehicle_id=vehicle2.id, date=datetime.date(2023, 3, 1), mileage=22000, fuel_used=8.0, efficiency=28.0)
    fuel3 = FuelEfficiency(vehicle_id=vehicle3.id, date=datetime.date(2023, 4, 1), mileage=220000, fuel_used=12.0, efficiency=32.0)
    fuel4 = FuelEfficiency(vehicle_id=vehicle4.id, date=datetime.date(2023, 5, 1), mileage=22000, fuel_used=10.0, efficiency=28.0)
    fuel5 = FuelEfficiency(vehicle_id=vehicle5.id, date=datetime.date(2023, 6, 1), mileage=22000, fuel_used=10.0, efficiency=28.0)
    fuel6 = FuelEfficiency(vehicle_id=vehicle6.id, date=datetime.date(2023, 7, 1), mileage=1754, fuel_used=10.0, efficiency=28.0)
    fuel7 = FuelEfficiency(vehicle_id=vehicle7.id, date=datetime.date(2023, 8, 1), mileage=45896, fuel_used=10.0, efficiency=28.0)


    session.add_all([fuel1, fuel2, fuel3, fuel4, fuel5, fuel6, fuel7])
    session.commit()

    # Add Reminders
    reminder1 = Reminder(vehicle_id=vehicle1.id, message="Next oil change in 500 miles", date=datetime.date(2023, 5, 1))
    reminder2 = Reminder(vehicle_id=vehicle2.id, message="Tire rotation due", date=datetime.date(2023, 6, 1))
    reminder3 = Reminder(vehicle_id=vehicle3.id, message="Brake pad change in 1000 miles", date=datetime.date(2023, 7, 1))
    reminder4 = Reminder(vehicle_id=vehicle4.id, message="Engine oil change in 1000 miles", date=datetime.date(2023, 8, 1))
    reminder5 = Reminder(vehicle_id=vehicle5.id, message="Next oil change in 500 miles", date=datetime.date(2023, 5, 1))
    reminder6 = Reminder(vehicle_id=vehicle6.id, message="Tire rotation due", date=datetime.date(2023, 6, 1))
    reminder7 = Reminder(vehicle_id=vehicle7.id, message="Brake pad change in 1000 miles", date=datetime.date(2023, 7, 1))

    session.add_all([reminder1, reminder2, reminder3, reminder4, reminder5, reminder6, reminder7])
    session.commit()


    print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()
