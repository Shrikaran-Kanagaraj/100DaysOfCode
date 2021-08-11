import phonenumbers
from phonenumbers import carrier, geocoder, timezone


mobileNum = input("Enter Mobile Number with country code: ")
mobileNum = phonenumbers.parse(mobileNum)


print(timezone.time_zones_for_number(mobileNum))

print(carrier.name_for_number(mobileNum, "en"))

print(geocoder.description_for_number(mobileNum, "en"))

print("valid Mobile Number :",phonenumbers.is_valid_number(mobileNum))

print("checking possibility of Number : ",phonenumbers.is_possible_number(mobileNum))