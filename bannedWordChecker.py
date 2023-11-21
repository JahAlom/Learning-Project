from bannedwords import bannedwords


def hasBannedWords(firstWord,secWord):
    for word in bannedwords:
        if firstWord.lower() == word.lower() or secWord.lower() == word.lower():
            return True
    return False

