# debug.py
from models import Vehicle, MaintenanceLog, Expense, User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import format_vehicle

# Database Setup
engine = create_engine('sqlite:///car_brain.db')
Session = sessionmaker(bind=engine)
session = Session()

# Debugging Functions
def list_all_vehicles():
    vehicles = session.query(Vehicle).all()
    for vehicle in vehicles:
        print(format_vehicle(vehicle))

def list_user_vehicles(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        print(f"Vehicles for {user.name}:")
        for vehicle in user.vehicles:
            print(format_vehicle(vehicle))
    else:
        print(f"No user found with ID {user_id}")

if __name__ == "__main__":
    print("Listing all vehicles in the database:")
    list_all_vehicles()
