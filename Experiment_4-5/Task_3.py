import datetime

def get_day_of_week(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A")

print(get_day_of_week("2025-11-14"))
print(get_day_of_week("2023-01-01"))
print(get_day_of_week("2004-02-29"))
print(get_day_of_week("2010-12-25"))
