from vehicles import Bike, Car
from decorators import ride_logger
from exceptions import (InvalidInputError,NegativeDistanceError,RideHistoryError)

# Save ride details into file
def save_history(details):
    try:
        with open("ride_history.txt", "a") as file:
            file.write(details + "\n")

    except OSError as e:
        raise RideHistoryError(f"Error writing ride history: {e}")


# Read ride history from file
def read_history():
    try:
        with open("ride_history.txt", "r") as file:
            history = file.read()
        return history

    except OSError as e:
        raise RideHistoryError(f"Error reading ride history: {e}")


# Ride Booking Function
@ride_logger
def book_ride(vehicle_type, driver_name, rating, distance):

    # Create vehicle object
    if vehicle_type.lower() == "bike":
        vehicle = Bike(driver_name, rating)

    elif vehicle_type.lower() == "car":
        vehicle = Car(driver_name, rating)

    else:
        raise InvalidInputError("Invalid vehicle type! Choose Bike or Car.")

    # Calculate fare
    fare = vehicle.calculate_fare(distance)

    #ride details
    details = (
        f"Driver Name: {driver_name} | "
        f"Vehicle Type: {vehicle_type.title()} | "
        f"Rating: {rating} | "
        f"Distance: {distance} km | "
        f"Fare: Rs. {fare}"
    )

    save_history(details) # Save ride history
    return vehicle, fare, details

# Display ride history
def display_history():
    history = read_history()
    print("\nRIDE HISTORY")

    if history.strip():
        print(history)
    else:
        print("No ride history found.")

# Book Ride Input Function
def book_ride_flow():
    vehicle_type = input("Enter Vehicle Type: ")
    driver_name = input("Enter Driver Name: ")
    rating = float(input("Enter Rating: "))
    distance = float(input("Enter Distance: "))

    if not driver_name:
        raise InvalidInputError("Driver name cannot be empty!")

    # Book the ride
    vehicle, fare, details = book_ride(vehicle_type,driver_name,rating,distance)

    # Display ride details
    print("RIDE DETAILS")
    print(f"Driver Name: {vehicle.driver_name}")
    print(f"Vehicle Type: {vehicle_type.title()}")
    print(f"Distance: {distance} km")
    print(f"Fare: Rs. {fare}")

# Main Program
def main():
    while True:
        print("RIDE SHARING SYSTEM ")
        print("1. Book a ride")
        print("2. View ride history")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                book_ride_flow()

            elif choice == "2":
                display_history()

            elif choice == "3":
                print("Thank you for riding with us!")
                break

            else:
                raise InvalidInputError("Invalid menu choice! Choose 1, 2 or 3.")

        # Handle custom input errors
        except InvalidInputError as e:
            print("Input Error:", e)

        # Handle negative distance
        except NegativeDistanceError as e:
            print("Distance Error:", e)

        except RideHistoryError as e:
            print("File Error:", e)

        except ValueError as e:
            print("Please enter a valid number:", e)

        except OSError as e:
            print("File Error:", e)

if __name__ == "__main__":
    main()
