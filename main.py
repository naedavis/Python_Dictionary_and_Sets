#dictionary
#Task1
# number of times a character appears in a string

string = input('Enter string : ')
value = input('Enter character to be looked for : ')

print(string.count(value)) # counting in the string variable received from the user
                        # the amount of value variable in the string variable


#Task2
#printing digits into words

number = list(input('enter a number to be converted: ')) # convetered to a list so its easier to run through in the loop
list_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for x in number: # x in the input received from the user
     print(str(list_words[int(x)]))
     #converted x to an int because it was returning a string value initially
     # because of the input variable and the postion in a list cant be  a string variable
     # #square brackets to say i just want this specific position in this list







