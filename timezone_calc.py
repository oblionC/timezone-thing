import pytz as tz
import datetime as dt

datetime_format = "%Y-%m-%d %H:%M"

def change_timezone_from_utc(timestamp, to_timezone:tz.timezone):
    return timestamp.astimezone(to_timezone)
def change_timezone_to_utc(timestamp, from_timezone:tz.timezone, utc_timezone:tz.timezone):
    return from_timezone.localize(timestamp).astimezone(utc_timezone)
def stringtoDate(dateString):
    return(dt.datetime.strptime(dateString, datetime_format))

