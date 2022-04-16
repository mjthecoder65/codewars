# Don't do this
letters = ""
document = "lkdjf;quo3erjljdlfq;puro198293iojefjnaljojqorje_lajeljfl  dljfldjqp l;af"
for letter in document:
    if letter.isalpha():
        letters += letter


# Good
temp = []

for letter in document:
    if letter.isalpha():
        temp.append(letter)

letters = "".join(temp)


# Better
letters = "".join([letter for letter in document if letter.isalpha()])

# Best
letters = "".join(letter for letter in document if letter.isalpha())