# helpers.py

def format_vehicle(vehicle):
    """
    Helper function to format vehicle details into a readable string.
    """
    return f"{vehicle.year} {vehicle.make} {vehicle.model} (VIN: {vehicle.vin}) - {vehicle.current_mileage} miles"

def get_vehicle_by_id(session, vehicle_id):
    """
    Retrieve a vehicle by its ID from the database.
    """
    return session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

def log_expense(session, vehicle_id, amount, description, date):
    """
    Log a new expense for a vehicle.
    """
    expense = Expense(vehicle_id=vehicle_id, amount=amount, description=description, date=date)
    session.add(expense)
    session.commit()
    print(f"Expense of ${amount} for {description} logged for vehicle ID {vehicle_id}.")
