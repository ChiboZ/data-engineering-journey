attempt = 0
while attempt < 3:
    answer = input('Do you agree? (yes/no)')
    if answer == 'yes':
        print("glad we are on the same page")
        break
    attempt += 1
else:
    print('you are out')
