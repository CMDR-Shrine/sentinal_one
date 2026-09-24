import datetime 
from zoneinfo import ZoneInfo

state = r"""

FROM: WellsOnline@servermail.com
Scheduled Payment Notification

 Dear personal,

 You have an outgoing scheduled payment. View Details

 Thank You for choosing Wells Fargo 

# attachments: 'forwardedmessage.eml': 10kb 'images.txt' : 6kb
 """

def iso_zone_date_time():
    return datetime.datetime.now(tz=ZoneInfo("Europe/Amsterdam")).isoformat()
