import re

pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
string = input("Enter a valid password :- ")
password = pattern.fullmatch(string)
if password :

 print("Password is valid :) ")
else:
    print("Sorry, password is not valid as it may be missing some security requirements. Try again !")





