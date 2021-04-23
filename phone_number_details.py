import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

mobile_number = input("Enter the mobile number: ")
number = phonenumbers.parse(mobile_number)#enter your number here
country = geocoder.description_for_number(number , 'en')
ISP = carrier.name_for_number(number , 'en')
print("country = {}".format(country))
print("internet service provider = {}".format(ISP))