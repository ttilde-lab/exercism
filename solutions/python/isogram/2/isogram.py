def is_isogram(string: str) -> bool:
    """
    Receives a string and determines if a word or phrase is an isogram. 
    An isogram is a word or phrase without a repeating letter.
    """
    string = string.lower().replace("-", "").replace(" ", "")
    return True if len(string) == len(set(string)) else False
