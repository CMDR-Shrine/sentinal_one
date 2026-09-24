from typesafe_sdk import Choice, Noul, TypeSafeClient
import datetime 
from zoneinfo import ZoneInfo
from input import state

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


def question_chain(client,state,time):
    return client.system_one(
                state,
                questions={

                    "is_solicitation": Noul(
                        instructions = "is this email commercial solicitation",
                        ),
                    "is_not_dutch/english": Noul(
                        instructions = "is the email NOT written in English or dutch?",
                        criteria = {
                            "true": "email is written in a language other than English or dutch",
                            "false": "email contents is written in English or Dutch",
                            }
                        ),
                    "contains_weird_attachments": Noul(
                        instructions = "does the email contain zip files"
                        ),
                    "is_payment": Noul(

                        instructions = f"Is this email chain a scam? Current time is: {time}",
                        criteria = {
                            "true": "email is asking user for money",
                            "false": "email makes no refrence to user needing to pay money",
                            }
                        ),
                    }
                )

def iso_zone_date_time():
    return datetime.datetime.now(tz=ZoneInfo("Europe/Amsterdam")).isoformat()




main()
