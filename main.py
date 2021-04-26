#dictionary
#Task1
# number of times a character appears in a string
# #
# string = input('Enter string : ')
# value = input('Enter character to be looked for : ')
#
# print(string.count(value))

#Task2
#printing digits into words
#
number = list(input('enter a number to be converted: '))
list_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for x in number:
    print(str(list_words[int(x)])) #square brackets to say i just want this specific position in this list