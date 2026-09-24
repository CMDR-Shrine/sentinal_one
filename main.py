from typesafe_sdk import Choice, Noul, TypeSafeClient
import datetime 
from zoneinfo import ZoneInfo
from input import state

def iso_zone_date_time():
    return datetime.datetime.now(tz=ZoneInfo("Europe/Amsterdam")).isoformat()

def main():

    time = iso_zone_date_time()
    print(time)

    client = TypeSafeClient(
        api_key="local",
        base_url="http://127.0.0.1:8009",
        model="kev-latest",
    )
    response = client.system_one(

            state,

            questions={
                "is_spam_email": {
                    "type": "noul",
                    "instructions": f"Is this email chain a scam? Current time is: {time}",
                    "criteria": {
                        "true": "email is asking for money and/or asking to click on links, instigating time pressure and/or times of correspondence don't align with current time and/or is asking to open a file/attachment and/or is not in English",
                        "false": "",
                        }
                    }
            },
        )
    print(response.nouls["is_spam_email"].noul)

main()
