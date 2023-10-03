def is_isogram(string):
    string = string.lower()
    letter_set = set()
    for char in string:
        if char == '-' or char == '_' or char == ' ':
            continue
        if char in letter_set:
            return False
        letter_set.add(char)
    return True