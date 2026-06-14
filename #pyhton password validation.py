# pyhton password validation

email = input("Enter your email: ")
password = input("enter your password: ")
password = password.strip()
valid = True

# Must not be empty
if password == "":
    print("password cannot be empty")
    valid = False
# Must include at least 1 lowercase
elif not any(letter.islower() for letter in password):
    print("password shoud contain at least 1 lower letter")
    valid = False
# Must not be same as the email
elif password == email:
    print("password cannot match email.")
    valid = False
# Must not contain any spaces
elif " " in password:
    print("password cannot contain empty spaces.")
    valid = False
# Must start and end with a letter or digit
elif not password[0].isalnum() or not password[-1].isalnum():
    print("password start and end with a letter or a number only.")
    valid = False
elif valid:
    print("password accepted")
