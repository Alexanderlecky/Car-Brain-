from models import User, Vehicle, MaintenanceLog, Expense
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Database Setup
engine = create_engine('sqlite:///car_brain.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_user():
    name = input("Enter the user's name: ")
    email = input("Enter the user's email: ")

    # Check if email already exists
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print(f"User with email {email} already exists.")
    else:
        new_user = User(name=name, email=email)
        try:
            session.add(new_user)
            session.commit()
            print(f"User {name} added successfully.")
        except IntegrityError:
            session.rollback()
            print("Error: Could not add user. Email must be unique.")

def add_vehicle():
    user_id = int(input("Enter the user ID: "))
    user = session.query(User).get(user_id)
    
    if user:
        make = input("Enter the make of the vehicle: ")
        model = input("Enter the model of the vehicle: ")
        year = int(input("Enter the year of the vehicle: "))
        vin = input("Enter the VIN: ")
        current_mileage = int(input("Enter the current mileage: "))

        new_vehicle = Vehicle(make=make, model=model, year=year, vin=vin, current_mileage=current_mileage, user_id=user_id)
        session.add(new_vehicle)
        session.commit()
        print(f"Vehicle {make} {model} added for user {user.name}!")
    else:
        print(f"User with ID {user_id} does not exist.")

def log_maintenance():
    vehicle_id = int(input("Enter the vehicle ID: "))
    task = input("Enter the maintenance task: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    mileage = int(input("Enter the mileage: "))
    description = input("Enter a description (optional): ")

    new_maintenance = MaintenanceLog(vehicle_id=vehicle_id, task=task, date=date, mileage=mileage, description=description)
    session.add(new_maintenance)
    session.commit()
    print("Maintenance task logged successfully.")

def add_expense():
    vehicle_id = int(input("Enter the vehicle ID: "))
    vehicle = session.query(Vehicle).get(vehicle_id)
    
    if vehicle:
        amount = float(input("Enter the amount: "))
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter a description (optional): ")

        try:
            # Parse date input to datetime object
            expense_date = datetime.strptime(date, '%Y-%m-%d').date()

            new_expense = Expense(vehicle_id=vehicle_id, amount=amount, date=expense_date, description=description)
            session.add(new_expense)
            session.commit()
            print(f"Expense of {amount} added for vehicle {vehicle.make} {vehicle.model}.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    else:
        print(f"Vehicle with ID {vehicle_id} does not exist.")

if __name__ == "__main__":
    print("Welcome to Car Brain!")
    while True:
        choice = input("\n1. Add User\n2. Add Vehicle\n3. Log Maintenance\n4. Add Expense\n5. Exit\nChoose an option: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            add_vehicle()
        elif choice == '3':
            log_maintenance()
        elif choice == '4':
            add_expense()
        elif choice == '5':
            break
        else:
            print("Invalid option!")
