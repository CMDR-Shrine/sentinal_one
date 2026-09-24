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
                        instructions = "does the email contain zip files"
                        ),
                    "is_payment": Noul(
                        instructions = f"does this email ask user to make a payment?",
                        criteria = {
                            "true": "email is asking user for money",
                            "false": "email makes no reference to user needing to pay money",
                            }
                        ),

                    "is_name_enumerated": Noul(
                        instructions = "does this email refer to the recipient as 'personal' eg Dear personal"
                        )
                    }
                )

