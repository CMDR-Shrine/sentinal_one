from typesafe_sdk import Choice, Noul, TypeSafeClient

def main():
    client = TypeSafeClient(
        api_key="local",
        base_url="http://127.0.0.1:8009",
        model="kev-latest",
    )
    response = client.system_one(
        state = r"""
    apparently needs to have been paid for in order to stand as a quote only lasts a short time and its not actually an order until its been paid for - unless you have a credit account and have agreed terms, which is what we discussed at the time. Do you actually know who has/hasn't been paid against who needs to be paid in advance? so what actually is or isn't ordered yet. also, just in the few you asked me to contact back in November there were a number that had no idea of the products we were trying to order as the product codes didn't exist - do we know everything is right and correct?
     


    On 2022-01-18 12:11, james@cucina-commercial.co.uk wrote:
    >
    > If we ordered prior to a price increase then those prices should stand - that's how it usually works 
    >  
    >
    >
    > On 2022-01-18 12:07, lucy@cucina-commercial.co.uk wrote:
    >
    >     Any company you don't have an account with is proforma and needs to be paid before anything can be ordered or processed which is what we discussed back in November. Also that they have price rises in early January and if not paid before then would be subject to the new prices. you were going to make a call on who you needed to pay before the price increases came into effect
    >
    >
    >      
    >
    >     On 2022-01-18 10:54, james@cucina-commercial.co.uk wrote:
    >
    >         No - this is from November nearly 3 months ago - I need to know anything that hasn’t been laid so I can arrange payment 
    >          
    >
    >
    >         On 2022-01-18 10:44, lucy@cucina-commercial.co.uk wrote:
    >
    >             sorted?
        """,
        questions={
            "spam": Noul(instructions="Is this email chain a scam?"),
            "tone": Choice(
                instructions="the general tone?",
                criteria={
                    "calm": None, 
                    "frustrated": None, 
                    "angry": None
                    },
            ),
        },
    )
    print(response.nouls["spam"].noul)
    print(response.choices["tone"].choice)


main()
