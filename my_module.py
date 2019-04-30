print('Importing Module...')

Test = 'Module String'

def find_in(to_search, target):
    for i, value in enumerate(to_search):
        if value==target:
            return i
    return -1