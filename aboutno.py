import phonenumbers
from phonenumbers import carrier,geocoder,timezone

mobileno=input("Enter mobile no. with country code")
no=phonenumbers.parse(mobileno)

print(timezone.time_zones_for_number(no))#getting timezone of a no

print(carrier.name_for_number(no, "en")) #getting carrier information

print(geocoder.description_for_number(no, "en")) #getting region info

print("Valid mobile number :",phonenumbers.is_valid_number(no)) #validating

print("Checking possibility of a number:",phonenumbers.is_possible_number(no))

