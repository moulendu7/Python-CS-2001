import datetime

def get_day_of_week(date_str):
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return d.strftime("%A")
print(get_day_of_week("2025-11-14"))
print(get_day_of_week("2005-06-12"))
print(get_day_of_week("2023-01-01"))