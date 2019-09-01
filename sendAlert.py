from twilio.rest import Client


def sendSMS():
    client = Client("ACea36acd28f6d2b4103f6c807a77ea8df",
                    "1bba95ad706ae9ece5be5325e771de21")
    client.messages.create(to="+14083246330", from_="+14088728390",
                           body="BRO NEW INTERNSHIP POSTINGS\nhttps://github.com/elaine-zheng/summer2020internships")
