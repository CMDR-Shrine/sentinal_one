from typesafe_sdk import Noul, TypeSafeClient
from input import state, iso_zone_date_time 
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
    print(response.answers["not_valid_email_domain"])


    YES_THRESH = 0.80
    is_name_enumerated_ans = response.answers["is_name_enumerated"].noul 
    not_valid_email_domain = response.answers["not_valid_email_domain"].noul 
    is_temporal_mismatch  = response.answers["is_temporal_mismatch"].noul

    if response.answers["is_not_dutch/english"].noul > YES_THRESH:
        print("NON NATIVE LANG DETECTED")

    if response.answers["contains_weird_attachments"].noul > YES_THRESH:
        print("WEIRD ATTACHMENTS DETECTED")

    if response.answers["is_payment"].noul > YES_THRESH:
        print("PAYMENT REQUEST DETECTED")

    if response.answers["is_solicitation"].noul > YES_THRESH:
        print("SOLICITATION DETECTED")

    if is_name_enumerated_ans > YES_THRESH:
        print(f"NAME ENUMERATION DETECTED")

    if not_valid_email_domain > YES_THRESH:
        print(f"EMAIL DOMAIN MISMATCH DETECTED")

    if is_temporal_mismatch > YES_THRESH:
        print(f"EMAIL DOMAIN MISMATCH DETECTED")
    








main()
