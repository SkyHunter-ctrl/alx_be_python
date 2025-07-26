# a script that performs specified operations with dates and times.
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()

    try:
        user_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
