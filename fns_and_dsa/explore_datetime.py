from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date(number_of_days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()

try:
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    calculate_future_date(number_of_days)
except ValueError:
    print("Please enter the number of days." )
