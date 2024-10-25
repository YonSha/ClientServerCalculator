import re


def neutralize_keywords(input_string, keywords):
    for keyword in keywords:
        placeholder = f'_{keyword}_'
        input_string = re.sub(r'\b' + re.escape(keyword) + r'\b', placeholder, input_string)

    return input_string


