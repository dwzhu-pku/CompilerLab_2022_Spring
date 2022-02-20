# --------------------------------------------
# lexer.py
# Used to perform tokenization for SubsetC
# --------------------------------------------

from ply.lex import lex

# All tokens must be named in advance.
tokens = ( 'identifier', 'number' )

# Ignored characters
t_ignore = ' \t'

# Helper variables
digit8 = r'[0-7]'
digit10 = r'[0-9]'
digit16 = r'[0-9A-Fa-f]'

# Token matching rules are written as regexs
t_identifier = r'[a-zA-Z_][a-zA-Z0-9_]*'

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_number(t):
    # f'[1-9]{digit10}*'
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored token with an action associated with it
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()

def test_function():
    # Test it out
    data = '''
    3 +  4 * 10
    + -20 *2
    '''

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

test_function()