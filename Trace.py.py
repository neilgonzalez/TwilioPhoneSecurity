

from twilio.rest import Client
import requests
account_sid = "sid"
auth_token = "token"
client = Client(account_sid, auth_token)


r = requests.get('https://lookups.twilio.com/v1/PhoneNumbers/+numberhere/?Type=fraud \
    -u \'sid:token\'')

number = client.lookups.phone_numbers("+numberhere").fetch(
	type=["carrier", "caller-name"],
    add_ons="whitepages_pro_caller_id"
)

print(number.carrier['type'])
print(number.carrier['name'])


print (r)




