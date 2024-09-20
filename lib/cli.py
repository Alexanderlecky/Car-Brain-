from models import User, Vehicle, MaintenanceLog, Expense
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate  # Useful for printing tables in a clean format

# Database Setup
engine = create_engine('sqlite:///car_brain.db')
Session = sessionmaker(bind=engine)
session = Session()

def print_users():
    users = session.query(User).all()
    if users:
        table = [[user.id, user.name, user.email] for user in users]
        print("\nUsers Table:")
        print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="pretty"))
    else:
        print("\nNo users found.")

def print_vehicles():
    vehicles = session.query(Vehicle).all()
    if vehicles:
        table = [[vehicle.id, vehicle.make, vehicle.model, vehicle.year, vehicle.vin, vehicle.current_mileage, vehicle.user_id] for vehicle in vehicles]
        print("\nVehicles Table:")
        print(tabulate(table, headers=["ID", "Make", "Model", "Year", "VIN", "Mileage", "User ID"], tablefmt="pretty"))
    else:
        print("\nNo vehicles found.")

def print_maintenance_logs():
    logs = session.query(MaintenanceLog).all()
    if logs:
        table = [[log.id, log.vehicle_id, log.task, log.date, log.mileage, log.description] for log in logs]
        print("\nMaintenance Logs Table:")
        print(tabulate(table, headers=["ID", "Vehicle ID", "Task", "Date", "Mileage", "Description"], tablefmt="pretty"))
    else:
        print("\nNo maintenance logs found.")

def print_expenses():
    expenses = session.query(Expense).all()
    if expenses:
        table = [[expense.id, expense.vehicle_id, expense.amount, expense.date, expense.description] for expense in expenses]
        print("\nExpenses Table:")
        print(tabulate(table, headers=["ID", "Vehicle ID", "Amount", "Date", "Description"], tablefmt="pretty"))
    else:
        print("\nNo expenses found.")

if __name__ == "__main__":
    print("Welcome to Car Brain!")
    
    # Print all tables
    print_users()
    print_vehicles()
    print_maintenance_logs()
    print_expenses()
    
    # Additional functionality like adding users, vehicles, maintenancelog, Expense
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
