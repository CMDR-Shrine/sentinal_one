# email 
from imaplib import IMAP4_SSL
# kev
from typesafe_sdk import Noul, TypeSafeClient
# time handling
from input import state, iso_zone_date_time 
# file imports
from questions import question_chain 
from CONSTANTS import YES_THRESH, EMAIL_PWD, EMAIL_ADDR, EMAIL_DOMAIN, EMAIL_MAX


def main():
    time = iso_zone_date_time()
    print(time)

    with IMAP4_SSL(EMAIL_DOMAIN) as M:
        M.login(EMAIL_ADDR, EMAIL_PWD)
        print(type(M.list()))

        message_total_status, message_total = M.select("INBOX")
        message_total = int(message_total[0])
        print(f"fetch status is: {message_total_status} total number of messages is: {message_total}")

        #message_body = M.fetch("0", "(RFC822)")
        res, raw_messages = M.fetch(str(1), "(RFC822)")

        

        


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
