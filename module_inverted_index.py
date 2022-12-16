def remove_punc_and_lower_case(text):
    """
    removes the punctuation from a text and returns it
    """
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for element in text:
        if element in punc:
            text = text.replace(element, " ")

    return text.lower()

# def lower_case(text):
#     """
#     return the the text in lower case format
#     """
#     return text.lower()