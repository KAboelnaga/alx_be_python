from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    global current_date
    current_date = datetime.now().replace(microsecond=0)
    print("Current date and time:", current_date)
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_datetime = current_date + timedelta(days=number_of_days)
    future_date = future_datetime.strftime("%Y-%m-%d")
    print("Future date:", future_date)
display_current_datetime()
calculate_future_date()