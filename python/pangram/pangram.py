def is_pangram(string):
    import re
    string_sub = re.sub('[^a-zA-Z]+', '', string).lower()
    return len(set(string_sub)) == 26
