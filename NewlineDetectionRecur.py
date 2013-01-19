def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    cursor = text[lineLength - 1:lineLength]
    if text == '':
        return ''
    else:
        if cursor == '':
            return text
        elif cursor == ' ':
            return text[:lineLength] + '\n' + insertNewlines(text[lineLength:], lineLength)
        else:
            return text[0] + insertNewlines(text[1:], lineLength)