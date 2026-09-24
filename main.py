from typesafe_sdk import Choice, Noul, TypeSafeClient
import datetime 
from zoneinfo import ZoneInfo
from input import state
from questions import question_chain 

def main():
    time = iso_zone_date_time()
    print(time)

    client = TypeSafeClient(
        api_key="local",
        # ssh -N -L 8009:localhost:8009 Karto-6
        base_url="http://127.0.0.1:8009",
        model="kev-latest",
    )

    response = question_chain(client,state,time)

    print(type(response.answers["is_solicitation"]))
    print(response.answers["is_solicitation"])


    # i cant figure out how to access the value, rn its just type 'Answer', not sure how to interface with that
    if response.answers["is_solicitation"].noul >= 0.1:
        print("yeet")



def iso_zone_date_time():
    return datetime.datetime.now(tz=ZoneInfo("Europe/Amsterdam")).isoformat()




main()
