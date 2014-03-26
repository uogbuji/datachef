import re

def normalize_whitespace(text):
    '''
    text should be a unicode object
    >>> from datachef.text import normalize_whitespace
    >>> normalize_whitespace('  abc  \ndef  \n  ghi  \n  hij')
    ''
    '''
    def repl(match):
        groups = match.groups()
        return u''.join(((g or u'') for g in groups))
    return normalize_whitespace.pattern.sub(repl, text)
normalize_whitespace.pattern = re.compile(ur"(?mxu)(^)\w+|\w+($)|(\w)\w+")

