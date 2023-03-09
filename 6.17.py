#Alexander Ho
#1677933


current_password = input()
new_password = ''

for i in current_password:
    if (i == 'i'):
        new_password += '!'
    elif (i == 'a'):
        new_password += '@'
    elif (i == 'm'):
        new_password += 'M'
    elif (i == 'B'):
        new_password += '8'
    elif (i == 'o'):
        new_password += '.'
    else:
        new_password += i

new_password = new_password + 'q*s'
print(new_password)