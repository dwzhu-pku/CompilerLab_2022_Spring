# --------------------------------------------
# lexer.py
# Used to perform tokenization for SubsetC
# --------------------------------------------

from ply.lex import lex

# All tokens must be named in advance.
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'int' : 'INT'
}

tokens = [ 'IDENT', 'NUMBER',  # 标识符 数字 
        'ADD', 'SUB', 'MUL', 'DIV', 'ASSIGN',  # + - * / =
        'EQ', 'NE', 'LT', 'GT', 'LE', 'GE', # == != < > <= >=
        'XKHZ', 'XKHY', 'ZKHZ', 'ZKHY', 'DKHZ', 'DKHY', # ( ) [ ] { }
        'COMMA', 'SEMI' # , ;
        ] + list(reserved.values())


# Ignored characters
t_ignore = ' \t'

# Helper variables
digit8 = r'[0-7]'
digit10 = r'[0-9]'
digit16 = r'[0-9A-Fa-f]'

# Token matching rules are written as regexs
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_ASSIGN = r'='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_XKHZ = r'\('
t_XKHY = r'\)'
t_ZKHZ = r'\['
t_ZKHY = r'\]'
t_DKHZ = r'\{'
t_DKHY = r'\}'
t_COMMA = r','
t_SEMI = r';'

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'IDENT')    # Check for reserved words
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

# test_function()