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

    answer_dict = question_chain(client,state,time).answers

    print(type(answer_dict["is_solicitation"]))
    print(answer_dict["is_solicitation"])


    # i cant figure out how to access the value, rn its just type 'Answer', not sure how to interface with that
    answer_dict["is_solicitation"] > 0.1


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
