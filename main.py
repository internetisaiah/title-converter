# This program contains a function that takes a string and converts it to the approved format.
# Learn more here: https://www.github.com/analog-isaiah/title-converter

def title_converter(optional_string = ''):
    # imports and variables
    import re
    user_string = ''

    if optional_string == '':
        user_string = ''
    else:
        user_string = optional_string

    # get the user's input and assign it to a variable
    # if input is blank, ask again
    while user_string == '':
        user_string = input("Enter show title:\n")

    # convert the string to lower case
    user_string = user_string.lower()

    # for titles containing C++, C#, .NET etc. replace with custom abbreviation
    # replace c++ with cpp (also works with A++, J++, etc.)
    user_string = re.sub('\+\+', 'pp', user_string)
    
    # replace c# with c-sharp (also works with A#, F#, etc.)
    user_string = re.sub(r'(\b[a-z]*#)', r'\1sharp', user_string)

    # replace asp.net with aspnet
    user_string = re.sub('asp\.net', 'aspnet', user_string)

    # replace ml.net with mlnet
    user_string = re.sub('ml\.net', 'mlnet', user_string)

    # replace .net with dotnet
    user_string = re.sub('\.net', ' dotnet', user_string)
        
    # replacing and removing special characters
    for char in user_string:
        # remove special characters
        if char == ' ':
            continue
        elif char == '-':
            user_string = user_string.replace(char, ' ')
        elif char == '—':
            user_string = user_string.replace(char, ' ')
        elif not char.isalnum():
            user_string = user_string.replace(char, '')

    # remove duplicate spaces
    to_remove = " "
    pattern = "(?P<char>[" + re.escape(to_remove) + "])(?P=char)+"
    user_string = re.sub(pattern, r"\1", user_string)

    # replace spaces with dashes
    new_string = user_string.replace(' ', '-')

    # if the string ends with a dash, remove the last dash
    # note: there will never be more than one dash because we remove duplicate spaces before converting spaces to dashes
    if new_string[-1] == '-':
        new_string = new_string[:-1]

    # if the string begins with a dash, remove the first dash
    if new_string[0] == "-":
        new_string = new_string[1:]

    # returns reformatted title
    return new_string

if __name__ == '__main__':
    print(title_converter())
