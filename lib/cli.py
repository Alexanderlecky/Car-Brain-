from models import User, Vehicle, MaintenanceLog, Expense
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database Setup
engine = create_engine('sqlite:///car_brain.db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a new user
def add_user():
    name = input("Enter the user's name: ")
    email = input("Enter the user's email: ")

    # Check if email already exists
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print(f"User with email {email} already exists.")
    else:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        print(f"User {name} added successfully.")

# Modified function to add a vehicle, now associated with a user
def add_vehicle():
    user_id = int(input("Enter the user ID: "))
    # Check if the user exists
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

if __name__ == "__main__":
    print("Welcome to Car Brain!")
    while True:
        choice = input("\n1. Add User\n2. Add Vehicle\n3. Log Maintenance\n4. Exit\nChoose an option: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            add_vehicle()
        elif choice == '3':
            log_maintenance()
        elif choice == '4':
            break
        else:
            print("Invalid option!")
