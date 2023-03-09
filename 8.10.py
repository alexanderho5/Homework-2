#Alexander Ho
#1677933


start_word = str(input())
no_spaces = start_word.replace(" ", "")
flipped = no_spaces[::-1]

if (no_spaces == flipped):
      print('{} is a palindrome'.format(start_word))
else:
      print('{} is not a palindrome'.format(start_word))