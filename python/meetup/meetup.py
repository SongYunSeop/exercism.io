from datetime import datetime, date
import calendar

def meetup_day(year, month, weekday, factor):
    weekday_dict = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    week_number = weekday_dict[weekday]

    if factor[0].isdigit():
        base_weekday = date(year, month, 1).weekday()
        offset = ((int(factor[0]) - 1) * 7 ) + 1
        calc_date = week_number - base_weekday if week_number >= base_weekday else 7 + week_number - base_weekday
        meetup_date = offset + calc_date

    elif factor == 'teenth':
        base_weekday = date(year, month, 20).weekday()
        offset = 20
        calc_date = week_number - base_weekday - 7 if week_number >= base_weekday else week_number - base_weekday
        meetup_date = offset + calc_date

    elif factor == 'last':
        base_weekday, offset = calendar.monthrange(year, month)
        base_weekday = date(year, month, offset).weekday()
        calc_date = week_number - base_weekday - 7 if week_number > base_weekday else week_number - base_weekday
        meetup_date = offset + calc_date

    return date(year, month, meetup_date)
