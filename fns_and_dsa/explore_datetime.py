from datetime import datetime as dt
from datetime import timedelta as delta
def display_current_datetime():
    global current_datetime
    current_datetime = dt.now().replace(microsecond=0)
    print("Current date and time:", current_datetime)
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_datetime = current_datetime + delta(days=days)
    future_date = future_datetime.strftime("%Y-%m-%d")
    print("Future date:", future_date)
display_current_datetime()

calculate_future_date()