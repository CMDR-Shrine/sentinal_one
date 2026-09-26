from typesafe_sdk import Noul, TypeSafeClient
from input import state, iso_zone_date_time 
from questions import question_chain 
from CONSTANTS import YES_THRESH


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
    print(response.answers["not_valid_email_domain"])

    is_name_enumerated_ans = response.nouls["is_name_enumerated"].noul 
    not_valid_email_domain = response.nouls["not_valid_email_domain"].noul 
    is_temporal_mismatch  = response.nouls["is_temporal_mismatch"].noul
    is_not_dutch_english = response.nouls["is_not_dutch/english"].noul
    contains_weird_attachments = response.nouls["contains_weird_attachments"].noul 
    is_payment = response.nouls["is_payment"].noul 
    is_solicitation = response.nouls["is_solicitation"].noul 

    # could actually iterate through the dict instead of doing all these if statments
    # for answer in response.nouls.noul
    for answer in response.nouls:
        score = response.nouls[answer].noul
        if score > YES_THRESH:
            print(f"Answer: {answer} Scored: {score} Threshold was set to: {YES_THRESH} ")

main()
