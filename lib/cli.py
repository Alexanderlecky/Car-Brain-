from models import  User, Vehicle, MaintenanceLog, Expense
from sqlalchemy import create_engine  # Fix this line
from sqlalchemy.orm import sessionmaker  # Fix this line


# Database Setup
engine = create_engine('sqlite:///car_brain.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_vehicle():
    make = input("Enter the make of the vehicle: ")
    model = input("Enter the model of the vehicle: ")
    year = int(input("Enter the year of the vehicle: "))
    vin = input("Enter the VIN: ")
    current_mileage = int(input("Enter the current mileage: "))


    new_vehicle = Vehicle(make=make,  model= model, year=year, vin=vin, current_mileage=current_mileage)
    session.add(new_vehicle)
    session.commit()
    print(f"Vehicle {make} {model} added!")

def log_maintenance():
    vehicle_id = int(input("Enter the vehicle ID: "))
    task = input("Enter the maintenance task: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    milage = int(input("Enter the milage: "))
    description = input("Enter a description (optional): ")

    new_maintenance = MaintenanceLog(vehicle_id=vehicle_id, task=task, date=date, mileage=mileage, description=description )
    session.add(new_maintenace)
    session.commit()
    print("Maintenance task logged successfully.")

if __name__ == "__main__":
    print("Welcome to Car Brain!")
    while True:
        choice = input("\n1. Add Vehicle\n2. Log Maintenance\n3. Exit\nChoose an option: ")
        if choice == '1':
            add_vehicle()
        elif choice == '2':
            log_maintenance()
        elif choice == '3':
            break
        else:
            print("Invalid option!")