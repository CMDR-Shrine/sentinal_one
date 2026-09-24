from typesafe_sdk import Choice, Noul, TypeSafeClient
import datetime 
from zoneinfo import ZoneInfo
from input import state


def question_chain(client,state,time):
    return client.system_one(

                state,
                questions={

                    "is_solicitation": {
                        "type": "noul",
                        "instructions": "is this email commercial solicitation"
                        },

                    "is_not_dutch/english": {
                        "type": "noul",
                        "instructions": "is the email NOT written in English or dutch?",
                        "criteria": {
                            "true": "email is written in a language other than English or dutch",
                            "false": "email contents is written in English or Dutch",
                            },

                        },

                    "contains_weird_attachments": {
                        "type": "noul",
                        "instructions": "does the email contain zip files, "
                        },

                    "is_payment": {
                        "type": "noul",
                        "instructions": f"Is this email chain a scam? Current time is: {time}",
                        "criteria": {
                            "true": "email is asking user for money",
                            "false": "the email makes no refrence to user needing to pay money",
                            }
                        }
                },
            )

def iso_zone_date_time():
    return datetime.datetime.now(tz=ZoneInfo("Europe/Amsterdam")).isoformat()


def main():
    time = iso_zone_date_time()
    print(time)

    client = TypeSafeClient(
        api_key="local",
        # ssh -N -L 8009:localhost:8009 Karto-6
        base_url="http://127.0.0.1:8009",
        model="kev-latest",
    )

    question_chain(client,state,time)


main()
