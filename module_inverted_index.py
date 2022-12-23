def remove_punc_and_lower_case(text):
    """
    removes the punctuation from a text and returns it in lowercase
    """
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for element in text:
        if element in punc:
            text = text.replace(element, " ")

    return text.lower()
