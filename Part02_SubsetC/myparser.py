# --------------------------------------------
# parser.py
# Used for grammar parsing for SubsetC
# --------------------------------------------

from tkinter.messagebox import NO
import ply.yacc as yacc
import lexer
import myast

tokens = lexer.tokens

def p_function(p):
    '''
    Function : Type IDENT XKHZ XKHY CompoundStmt
             | Type IDENT XKHZ ArgList XKHY CompoundStmt
    '''
    if len(p) == 6:
        p[0] = myast.FunDef(p[1], p[2], list(), p[5].content_list)
        print("Parsing function finished!")
    elif len(p) == 7:
        p[0] = myast.FunDef(p[1], p[2], p[4].content_list, p[6].content_list)
        print("Parsing function with arglist finished!")

def p_arglist(p):
    '''
    ArgList : Arg
            | ArgList COMMA Arg
    '''
    if len(p) == 2:
        p[0] = myast.ItemList()
        p[0].append_item(p[1])
    elif len(p) == 3:
        p[0] = p[1].append_item(p[3])
    print("Parsing arglist")

def p_arg(p):
    'Arg : Type IDENT'
    p[0] = myast.Arg(p[1], p[2])
    print("Parsing arg")

def p_declaration(p):
    'Declaration : Type IdentList'
    p[0] = myast.Decl(p[1], p[2].content_list)
    print("Parsing Declaration")


def p_type(p):
    '''
    Type : INT
    '''
    p[0] = p[1]
    print("Parsing Type")


def p_identlist(p):
    '''
    IdentList : IdentList COMMA IDENT
              | IDENT
    '''
    if len(p) == 2:
        p[0] = myast.ItemList()
        p[0].append_item(p[1])
    elif len(p) == 4:
        p[0] = p[1].append_item(p[3])
    print("Parsing IdentList")


def p_stmt(p):
    '''
    Stmt : ForStmt
         | WhileStmt
         | Expr SEMI
         | IfStmt
         | CompoundStmt
         | Declaration
         | SEMI
    '''
    p[0] = myast.ItemList()
    p[0].append_item(p[1])
    print("Parsing Stmt")


def p_forstmt(p):
    '''
    ForStmt : FOR XKHZ OptExpr SEMI OptExpr SEMI OptExpr XKHY Stmt
    '''
    p[0] = myast.ForAst(p[3], p[5], p[7], p[9])
    print("Parsing ForStmt")


def p_optexpr(p):
    '''
    OptExpr : Expr
            | 
    '''
    if len(p) == 1:
        p[0] = None
    elif len(p) == 2:
        p[0] = p[1]
    print("Parsing OptExpr")


def p_whilestmt(p):
    '''
    WhileStmt : WHILE XKHZ Expr XKHY Stmt
    '''
    p[0] = myast.WhileAst(p[3], p[5])
    print("Parsing WhileStmt")


def p_ifstmt(p):
    '''
    IfStmt : IF XKHZ Expr XKHY Stmt ElsePart
    '''
    p[0] = myast.IfAst(p[3], p[5], p[6])
    print("Parsing IfStmt")


def p_elsepart(p):
    '''
    ElsePart : ELSE Stmt
             |
    '''
    if len(p) == 1:
        p[0] = None
    elif len(p) == 3:
        p[0] = p[2]
    print("Parsing ElsePart")


def p_compoundstmt(p):
    '''
    CompoundStmt : DKHZ StmtList DKHY
    '''
    p[0] = p[2]
    print("Parsing CompoundStmt")


def p_stmtlist(p):
    '''
    StmtList : StmtList Stmt
             | 
    '''
    if len(p) == 1:
        p[0] = myast.ItemList()
    elif len(p) == 3:
        print(p[0], p[1], p[2])
        p[0] = p[1].append_item(p[2])
    print("Parsing StmtList")


def p_expr(p):
    '''
    Expr : IDENT ASSIGN Expr
         | Rvalue
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = myast.ExprAst(p[1], p[2], p[3])
    print("Parsing Expr")


def p_rvalue(p):
    '''
    Rvalue : Rvalue Compare Mag
           | Mag
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = myast.ExprAst(p[1], p[2], p[3])
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
    p[0] = p[1]
    print("Parsing Compare")


def p_mag(p):
    '''
    Mag : Mag ADD Term
        | Mag SUB Term
        | Term
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = myast.ExprAst(p[1], p[2], p[3])

    print("Parsing Mag")


def p_term(p):
    '''
    Term : Term MUL Factor
         | Term DIV Factor
         | Factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = myast.ExprAst(p[1], p[2], p[3])
    print("Parsing Term")


def p_factor(p):
    '''
    Factor : XKHZ Expr XKHY
           | SUB Factor
           | ADD Factor
           | IDENT
           | NUMBER
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = myast.ExprAst(None, p[1], p[2])
    elif len(p) == 4:
        p[0] = p[2]
    print("Parsing Factor")


# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error in input p {p}!")

# Build the parser
cparser = yacc.yacc()