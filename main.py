# email 
from imaplib import IMAP4_SSL
# kev
from typesafe_sdk import Noul, TypeSafeClient
# time handling
from input import state, iso_zone_date_time 
# file imports
from questions import question_chain 
from CONSTANTS import YES_THRESH, EMAIL_PWD, EMAIL_ADDR, EMAIL_DOMAIN


def main():
    time = iso_zone_date_time()
    print(time)

    with IMAP4_SSL(EMAIL_DOMAIN) as M:
        M.login(EMAIL_ADDR, EMAIL_PWD)
        M.noop()

    client = TypeSafeClient(
        api_key="local",
        # ssh -N -L 8009:localhost:8009 Karto-6
        base_url="http://127.0.0.1:8009",
        model="kev-latest",
    )

    response = question_chain(client,state,time)
    # could actually iterate through the dict instead of doing all these if statments
    # for answer in response.nouls.noul
    for answer in response.nouls:
        score = response.nouls[answer].noul
        if score > YES_THRESH:
            print(f"Answer: {answer} Scored: {score} Threshold was set to: {YES_THRESH} ")

main()
