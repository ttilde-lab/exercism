def is_isogram(word: str) -> bool:
    word_set = "".join(set(word.lower().replace("-", "").replace(" ", "")))
    word = word.lower().replace("-", "").replace(" ", "")
    return True if len(word) == len(word_set) else False
