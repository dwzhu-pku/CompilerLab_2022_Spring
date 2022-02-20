# --------------------------------------------
# parser.py
# Used for grammar parsing for SubsetC
# --------------------------------------------

import ply.yacc as yacc
import lexer

tokens = lexer.tokens

def p_function(p):
    '''
    Function : Type IDENT XKHZ XKHY CompoundStmt
             | Type IDENT XKHZ ArgList XKHY CompoundStmt
    '''
    p[0] = 0
    if len(p) == 6:
        print("Parsing function finished!")
    elif len(p) == 7:
        print("Parsing function with arglist finished!")

def p_arglist(p):
    '''
    ArgList : Arg
            | ArgList COMMA Arg
    '''
    print("Parsing arglist")

def p_arg(p):
    'Arg : Type IDENT'
    print("Parsing arg")

def p_declaration(p):
    'Declaration : Type IdentList'
    print("Parsing Declaration")


def p_type(p):
    '''
    Type : INT
    '''
    print("Parsing Type")


def p_identlist(p):
    '''
    IdentList : IDENT COMMA IdentList
              | IDENT
    '''
    print("Parsing IdentList")


def p_stmt(p):
    '''
    Stmt : ForStmt
         | WhileStmt
         | Expr
         | IfStmt
         | CompoundStmt
         | Declaration
         | 
    '''
    print("Parsing Stmt")


def p_forstmt(p):
    '''
    ForStmt : FOR XKHZ Expr SEMI Expr SEMI OptExpr XKHY Stmt
    '''
    print("Parsing ForStmt")


def p_optexpr(p):
    '''
    OptExpr : Expr
            | 
    '''
    print("Parsing OptExpr")


def p_whilestmt(p):
    '''
    WhileStmt : WHILE XKHZ Expr XKHY Stmt
    '''
    print("Parsing WhileStmt")


def p_ifstmt(p):
    '''
    IfStmt : IF XKHZ Expr XKHY Stmt ElsePart
    '''
    print("Parsing IfStmt")


def p_elsepart(p):
    '''
    ElsePart : ELSE Stmt
             |
    '''
    print("Parsing ElsePart")


def p_compoundstmt(p):
    '''
    CompoundStmt : DKHZ StmtList DKHY
    '''
    print("Parsing CompoundStmt")


def p_stmtlist(p):
    '''
    StmtList : StmtList Stmt
             |
    '''
    print("Parsing StmtList")


def p_expr(p):
    '''
    Expr : IDENT ASSIGN Expr
         | Rvalue
    '''
    print("Parsing Expr")


def p_rvalue(p):
    '''
    Rvalue : Rvalue Compare Mag
           | Mag
    '''
    print("Parsing Rvalue")


def p_compare(p):
    '''
    Compare : EQ 
            | LT 
            | GT 
            | LE 
            | GE 
            | NE
    '''
    print("Parsing Compare")


def p_mag(p):
    '''
    Mag : Mag ADD Term
        | Mag SUB Term
        | Term
    '''
    print("Parsing Mag")


def p_term(p):
    '''
    Term : Term MUL Factor
         | Term DIV Factor
         | Factor
    '''
    print("Parsing Term")


def p_factor(p):
    '''
    Factor : XKHZ Expr XKHY
           | SUB Factor
           | ADD Factor
           | IDENT
           | NUMBER
    '''
    print("Parsing Factor")


# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error in input p {p}!")

# Build the parser
parser = yacc.yacc()

with open("../test_subsetc/basic_00_naive", 'r', encoding="utf-8") as fin:
    s = fin.read()
    result = parser.parse(s)
    print(result)