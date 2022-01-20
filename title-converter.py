# Create function that takes a string and converts to the approved naming convention

def title_converter():
    # variables + get user input
    user_string = input("Enter show title:\n")

    # convert to lower case
    user_string = user_string.lower()

    # remove special characters
    for char in user_string:
        if char == ' ':
            continue
        elif char == '-':
            user_string = user_string.replace(char, ' ')
        elif not char.isalnum():
            user_string = user_string.replace(char, '')

    # remove duplicate spaces
    import re
    to_remove = " "
    pattern = "(?P<char>[" + re.escape(to_remove) + "])(?P=char)+"
    user_string = re.sub(pattern, r"\1", user_string)

    # replace spaces with dashes
    new_string = user_string.replace(' ', '-')

    # if title ends with a dash, remove last dash
    # note: there will never be more than one dash because we remove duplicate spaces before converting spaces to dashes
    if new_string[-1] == '-':
        new_string = new_string[:-1]

    # print reformatted title
    print(new_string)


title_converter()
