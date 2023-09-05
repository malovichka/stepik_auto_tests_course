def text_substring(full_string:str, substring:str):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"
    

text_substring('fulltext', 'some_value')