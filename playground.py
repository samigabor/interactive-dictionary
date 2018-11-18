# playground.py

# import constants
# import utils
# from difflib import get_close_matches
#
#
# def translate():
#     utils.display_intro()
#     dictionary = constants.data
#     while True:
#         word = input('Enter a word("q" to exit the program): ')
#         if word == 'q':
#             break
#         output = None
#         if word in dictionary:
#             pass
#         elif word.capitalize() in dictionary:
#             word = word.capitalize()
#         elif word.lower() in dictionary:
#             word = word.lower()
#         elif word.upper() in dictionary:
#             word = word.upper()
#         else:
#             closest_word = get_close_matches(word, dictionary, n=1, cutoff=0.8)
#             if closest_word:
#                 confirmation = input(f'I\'m not familiar with that word. Did you mean "{closest_word[0]}" instead(y/n)? ')
#                 if confirmation[0] in 'Yy':
#                     word = closest_word[0]
#                 else:
#                     output = 'Sorry I couldn\'t be more helpful.\n'
#             else:
#                 output = 'That\'s not an english word! Try again.'
#         if output:
#             print(output)
#         else:
#             output = dictionary[word]
#             if len(output) == 1:
#                 print(f'"{word}":')
#                 print(f'   {output[0]}')
#                 print()
#             else:
#                 print(f'"{word}" has multiple meanings:')
#                 for i in range(1, len(output)+1):
#                     print(f'   {i}.', output[i-1])
#                 print()
#     print('Thanks! Have a nice day.\n')

# import constants
# import json
# from difflib import get_close_matches


# def is_in_dictionary(word):
#     if word in dictionary:
#         pass
#     elif word.capitalize() in dictionary:
#         word = word.capitalize()
#     elif word.lower() in dictionary:
#         word = word.lower()
#     elif word.upper() in dictionary:
#         word = word.upper()
#     else:
#         word = None
#     return word
#
#
# dictionary = json.load(open(constants.fname, 'r'))
# print('This is an english dictionary.')
#
# while True:
#     user_input = input('Enter a word("q" to exit the program): ')
#     if user_input == 'q':
#         break
#     output = None
#     if is_in_dictionary(user_input):
#         output = dictionary[user_input]
#     else:
#         closest_word = get_close_matches(user_input, dictionary, n=1, cutoff=0.6)
#         if closest_word:
#             confirmation = input(f'I\'m not familiar with that word. Did you mean "{closest_word[0]}" instead(y/n)? ')
#             if confirmation[0] in 'Yy':
#                 user_input = closest_word[0]
#             else:
#                 output = 'Sorry I couldn\'t be more helpful.'
#         else:
#             output = 'That\'s not an english word! Try again.'
#
#     if output:
#         print(output)
#     else:
#         output = dictionary[user_input]
#         if len(output) == 1:
#             print(f'"{user_input}":')
#             print(f'   {output[0]}')
#             print()
#         else:
#             print(f'"{user_input}" has multiple meanings:')
#             for i in range(1, len(output)+1):
#                 print(f'   {i}.', output[i-1])
#             print()
# print('Thanks! Have a nice day.\n')


import constants
import utils
from difflib import get_close_matches


def translate(word):
    output = None
    if word in dictionary:
        pass
    elif word.capitalize() in dictionary:
        word = word.capitalize()
    elif word.lower() in dictionary:
        word = word.lower()
    elif word.upper() in dictionary:
        word = word.upper()
    else:
        closest_word = get_close_matches(word, dictionary, n=1, cutoff=0.8)
        if closest_word:
            confirmation = input(f'I\'m not familiar with that word. Did you mean "{closest_word[0]}" instead(y/n)? ')
            if confirmation[0] in 'Yy':
                word = closest_word[0]
            else:
                output = 'Sorry I couldn\'t be more helpful.\n'
        else:
            output = 'That\'s not an english word! Try again.'
    if output:
        print(output)
    else:
        output = dictionary[word]
        if len(output) == 1:
            print(f'"{word}":')
            print(f'   {output[0]}')
            print()
        else:
            print(f'"{word}" has multiple meanings:')
            for i in range(1, len(output)+1):
                print(f'   {i}.', output[i-1])
            print()


utils.intro_message()
dictionary = constants.data
user_input = input('Enter a word("q" to exit the program): ')
while user_input != 'q':
    translate(user_input)
    user_input = input('Enter another word("q" to exit the program): ')
print('Thanks! Have a nice day.\n')