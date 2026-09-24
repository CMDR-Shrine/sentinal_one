from typesafe_sdk import  Noul 

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
                        instructions = "do the email attachments seem strange, eg file size,naming scheme vs file type"
                        ),
                    "is_payment": Noul(
                        instructions = f"Does the email reference payments",
                        ),

                    "is_name_enumerated": Noul(
                        instructions = "does this email refer to the recipient as 'personal' eg Dear personal"
                        ),
                    "not_valid_email_domain": Noul(
                        instructions = "does the email domain NOT name match the company/correspondence content",
                        criteria = {
                            "yes" : "the email domain is being deceptive or doesnt match the contents of the email eg: 'tesco@<strangedomain>' ",
                            "no" : "the email domain does match the contents of the and is not deceptive in its naming eg: 'support@tesco.com",
                            }
                        ),
                    "is_temporal_mismatch": Noul(
                        instructions = f"does the email time stamp not coincide the current {time}",
                        ),

                    }
                )

