from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    global current_date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", future_date)
display_current_datetime()
calculate_future_date()