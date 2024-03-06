def validate_email(email):
    import re
    patt = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    pattern = re.compile(patt) 
    return re.match(pattern,email) is not None
print(validate_email('python@development.com'))