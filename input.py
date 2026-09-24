import datetime 
from zoneinfo import ZoneInfo

state = r"""

Scheduled Payment Notification

 Dear personal,

 You have an outgoing scheduled payment. View Details

 Thank You for choosing Wells Fargo 

 """

def iso_zone_date_time():
    return datetime.datetime.now(tz=ZoneInfo("Europe/Amsterdam")).isoformat()
