# Validate the Quality and Correctness of Email Values
# Must not be empty
email = input("Enter your email address: ")
Valid = True
email = email.strip()  # Remove leading and trailing whitespace
if email == "":
    print("Email address cannot be empty.")
    Valid = False
# Must contain '. and '@'
if '.' not in email or '@' not in email:
    print("Email address must contain both '.' and '@' symbols.")
    Valid = False
# Must contain exactly one '@' symbol
if email.count('@') != 1:
    print("Email address must contain exactly one '@' symbol.")
    Valid = False
# Must end with '.com', 'org', or '.net'
if not (email.endswith('.com') or email.endswith('.org') or email.endswith('.net')):
    print("Email address must end with '.com', '.org', or '.net'.")
    Valid = False
# Must not be longer than 254 characters
if len(email) > 254:
    print("Email address must not be longer than 254 characters.")
    Valid = False
# Must start and end with a letter or digit
if not (email[0].isalnum() and email[-1].isalnum()):
    print("email must start and end with a letter or number")
    Valid = False
if Valid:
    print("Email accepted")
