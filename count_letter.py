import string

letter_input = input("Type anything: ")

letter_list = list(string.ascii_lowercase) + ["ä", "ö", "ü", "ß"] + list(string.digits) + list(string.punctuation)


for x in range(len(letter_list)):

  one_letter = str(letter_list[x])

  check_letters = letter_input.lower().count(one_letter)

  if check_letters > 0:

    letter_print = print(str(check_letters) + " " + one_letter)