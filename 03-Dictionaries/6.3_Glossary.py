programming_words = {
    'tuple': 'a list that cannot be modified',
    'append': 'adding items to a list',
    'index': 'the order of an item in a list, starting from zero',
    'slice': 'only using some elements',
    'sort': 'rearranging a list into numerical or alphabetical order',
    }
print('tuple:'.title(), '\n\t', programming_words['tuple'], '\n')
print('append:'.title(), '\n\t', programming_words['append'], '\n')
print('index:'.title(), '\n\t', programming_words['index'], '\n')
print('slice:'.title(), '\n\t', programming_words['slice'], '\n')
print('sort:'.title(), '\n\t', programming_words['sort'])

programming_words = {
    "append": "adds items to a list",
    "comment": "a line in a program that is not executed, marked by hashtag",
    "variable": "represents a data, defined at the beginning of the program",
    "sort": "a function used to rearrange lists into alphabetical or numerical order",
    "tuple": "a list which cannot be modified"
    }
for key, value in programming_words.items():
    print(key, ":", '\n\t', value, '\n')
