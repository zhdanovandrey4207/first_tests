def capitalize(text):
    if text == '':
        return ''
    if text == None:
        return None
    if type(text) is int:
        return text
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'
